from photos.models import Photo, Camera, Rover, Job
from os import environ
import asyncpg
from datetime import datetime


async def connection_pool():
    user = environ['POSTGRES_USER']
    password = environ['POSTGRES_PASSWORD']
    database = environ['POSTGRES_DATABASE']
    string = f'postgresql://{user}@localhost/{database}'
    pool = await asyncpg.create_pool(string, password=password)
    return pool


async def insert_photo(connection, obj: dict) -> None:
    await connection.execute(
        """
        INSERT INTO
            photos_photo(id, sol, img_src, earth_date, camera_id)
        VALUES
            ($1, $2, $3, $4, $5)
        ON CONFLICT DO NOTHING
        """,
        obj['id'],
        obj['sol'],
        obj['img_src'],
        datetime.fromisoformat(obj['earth_date']),
        obj['camera']['id'],
    )


async def insert_camera(connection, obj: dict) -> None:
    await connection.execute(
        """
        INSERT INTO
            photos_camera(id, name, full_name, rover_id)
        VALUES
            ($1, $2, $3, $4)
        ON CONFLICT DO NOTHING
        """,
        obj['id'],
        obj['name'],
        obj['full_name'],
        obj['rover_id'],
    )


async def insert_rover(connection, obj: dict) -> None:
    await connection.execute(
        """
        INSERT INTO
            photos_rover(id, name, landing_date, launch_date, status, max_sol, max_date, total_photos)
        VALUES
            ($1, $2, $3, $4, $5, $6, $7, $8)
        ON CONFLICT DO NOTHING
        """,
        obj['id'],
        obj['name'],
        datetime.fromisoformat(obj['landing_date']),
        datetime.fromisoformat(obj['launch_date']),
        obj['status'],
        obj['max_sol'],
        datetime.fromisoformat(obj['max_date']),
        obj['total_photos'],
    )


async def insert_job(connection, rover_id, sol=0, page=1) -> None:
    await connection.execute(
        """
        INSERT INTO
            photos_job(sol, page, rover_id)
        VALUES
            ($1, $2, $3)
        """,
        sol,
        page,
        rover_id,
    )


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
        rover_id
    )


async def insert_or_get_job(connection, rover_id) -> asyncpg.Record:
    job = await get_job(connection, rover_id)
    if job != None: return job

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
        job_id
    )
