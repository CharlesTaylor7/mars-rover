import asyncio
import json
import itertools
import logging

from asyncio import Queue
from aiohttp import ClientSession

from django.core.management.base import BaseCommand, CommandError
from photos.models import Rover, Camera, Photo

from . import _db as db
from . import _api as api
from ._unbuffered import Unbuffered


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def __init__(self):
        super().__init__()
        self.stdout = Unbuffered(self.stdout)

    def handle(self, *args, **options):
        def write(message):
            self.stdout.write(self.style.SUCCESS(str(message)))


        rate_limit_message = 'Api rate limit has been met; retry in an hour.'


        async def load_photos(session, pool, job):
            async with pool.acquire() as connection:
                max_sol = job['max_sol']
                rover_name = job['rover_name']
                start_sol = job['sol']
                for sol in range(start_sol, max_sol + 1):

                    start_page = 1 if sol > start_sol else job['page']
                    for page in itertools.count(start=start_page):
                        write('rover = %s, sol = %d, page = %d' % (rover_name, sol, page))

                        photos = await api.get_photos(
                            session,
                            rover=rover_name,
                            sol=sol,
                            page=page
                        )

                        if photos == 'RateLimited':
                            write(rate_limit_message)
                            await db.update_job(connection, job['id'],sol, page)
                            return

                        for photo in photos:
                            await db.insert_camera(connection, photo['camera'])
                            await db.insert_photo(connection, photo)

                        if len(photos) < 25:
                            break


        async def get_jobs(session, pool):
            async with pool.acquire() as connection:
                rovers = await api.get_rovers(session)
                if rovers == 'RateLimited':
                    write(rate_limit_message)
                    exit(0)

                jobs = []
                for rover in rovers:
                    await db.insert_rover(connection, rover)
                    job = await db.insert_or_get_job(connection, rover['id'])
                    jobs.append(job)
                return jobs


        async def populate_db():
            async with ClientSession(json_serialize=json.dumps) as session:
                pool = await db.connection_pool()
                jobs = await get_jobs(session, pool)

                await asyncio.gather(*[
                    load_photos(session, pool, job)
                    for job in jobs
                ])

        ignore_all = 51
        logging.getLogger("asyncio").setLevel(ignore_all)

        asyncio.run(populate_db())

        write("Finished")
