import asyncio
import asyncpg
import json
import itertools
import logging

from asyncio import Queue
from aiohttp import ClientSession

from django.core.management.base import BaseCommand, CommandError
from photos.models import Rover, Camera, Photo, Job
from dotenv import load_dotenv

from . import _api as api
from ._unbuffered import Unbuffered














class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def __init__(self):
        super().__init__()
        load_dotenv()
        self.stdout = Unbuffered(self.stdout)

    def handle(self, *args, **options):
        def write(message):
            self.stdout.write(self.style.SUCCESS(str(message)))

        rate_limit_message = "Api rate limit has been met; retry in an hour."

        async def load_photos(session, pool, job):
            async with pool.acquire() as connection:
                for sol in range(job.sol, job.max_sol + 1):
                    start_page = 1 if sol > job.sol else job.page
                    for page in itertools.count(start=start_page):
                        write(
                            "rover = %s, sol = %d, page = %d" % (job.rover.name, sol, page)
                        )

                        photos = await api.get_photos(
                            session, rover=job.rover.name, sol=sol, page=page
                        )

                        if photos == "RateLimited":
                            write(rate_limit_message)
                            job.sol = sol
                            job.page = page
                            await job.asave()
                            return

                        for photo in photos:
                            await Camera(id=photo['camera']['id'], name=photo['camera']['name'], full_name=photo['camera']['full_name'], rover_id=photo['camera']['rover_id']).asave()

                            await Photo(id=photo['id'], sol=photo['sol'], img_src=photo['img_src'], earth_date=photo['earth_date'], camera_id=photo['camera']['id']).asave()

                        if len(photos) < 25:
                            break

        async def get_jobs(session, pool):
            async with pool.acquire() as connection:
                rovers = await api.get_rovers(session)
                if rovers == "RateLimited":
                    write(rate_limit_message)
                    exit(0)

                jobs = []
                for rover in rovers:
                    await Rover(id=rover['id'], name=rover['name'], landing_date=rover['landing_date'], launch_date=rover['launch_date'], status=rover['status'], max_date=rover['max_date'], total_photos=rover['total_photos']).asave()
                    job,_ = await Job.objects.select_related("rover").aget_or_create(rover_id=rover['id'],defaults={'max_sol': rover['max_sol']})
                    jobs.append(job)
                return jobs

        async def populate_db():
            async with ClientSession(json_serialize=json.dumps) as session:
                pool = await db.connection_pool()
                jobs = await get_jobs(session, pool)

                await asyncio.gather(*[load_photos(session, pool, job) for job in jobs])


        asyncio.run(populate_db())

        write("Finished")
