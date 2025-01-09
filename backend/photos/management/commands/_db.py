from photos.models import Photo, Camera, Rover, Job
from os import environ
import asyncpg
from datetime import datetime


async def connection_pool():
    user = environ["POSTGRES_USER"]
    password = environ["POSTGRES_PASSWORD"]
    database = environ["POSTGRES_DATABASE"]
    string = f"postgresql://{user}@localhost/{database}"
    pool = await asyncpg.create_pool(string, password=password)
    return pool


async def insert_photo(connection, obj: dict) -> None:
    await Photo(id=obj['id'], sol=obj['sol'], img_src=obj['img_src'], earth_date=obj['earth_date'], camera_id=obj['camera']['id']).asave()


async def insert_camera(connection, obj: dict) -> None:
    await Camera(id=obj['id'], name=obj['name'], full_name=obj['full_name'], rover_id=obj['rover_id']).asave()


async def insert_rover(connection, obj: dict) -> None:
    await Rover(id=obj['id'], name=obj['name'], landing_date=obj['landing_date'], launch_date=obj['launch_date'], status=obj['status'], max_sol=obj['max_sol'], max_date=obj['max_date'], total_photos=obj['total_photos']).asave()

async def insert_job(connection, rover_id, sol=0, page=1) -> None:
    await Job(sol=sol,page=page,rover_id=rover_id).asave()


async def get_job(connection, rover_id) -> asyncpg.Record:
    return await connection.fetchrow(
        """
        SELECT
            photos_job.id,
            sol,
            page,
            photos_rover.max_sol,
            photos_rover.name as rover_name
        FROM
            photos_job
        INNER JOIN
            photos_rover ON photos_job.rover_id = photos_rover.id
        WHERE
            photos_job.rover_id = $1
        """,
        rover_id,
    )


async def insert_or_get_job(connection, rover_id) -> asyncpg.Record:
    job = await get_job(connection, rover_id)
    if job != None:
        return job

    await insert_job(connection, rover_id=rover_id)
    job = await get_job(connection, rover_id)

    return job


async def update_job(connection, job_id, sol, page) -> None:
    await connection.fetchrow(
        """
        UPDATE
            photos_job as job
        SET
            sol = $1,
            page = $2
        WHERE
            job.id = $3
        """,
        sol,
        page,
        job_id,
    )
