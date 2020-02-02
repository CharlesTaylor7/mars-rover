from django.http import HttpResponse
import json
from .models import Photo, Camera, Rover
from typing import List
from django.http import JsonResponse
from psycopg2 import sql
from django.db import connection


def safe_SQL_query(rover, camera):
    return sql.SQL("""
        SELECT
            photos_photo.img_src,
            photos_photo.earth_date
        FROM
            photos_photo
        INNER JOIN
            photos_camera ON photos_photo.camera_id = photos_camera.id
        INNER JOIN
            photos_rover ON photos_camera.rover_id = photos_rover.id
        WHERE
            photos_rover.name = '{rover}'
        AND
            photos_camera.name = '{camera}'
        ORDER BY
            photos_photo.earth_date ASC;
    """).format(
        rover=sql.Identifier(rover),
        camera=sql.Identifier(camera),
    )


def get_photos_with_raw_SQL(rover, camera):
    with connection.cursor() as cursor:
        cursor.execute(safe_SQL_query(rover, camera))
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def index(request, rover, camera):
    response = get_photos_with_raw_SQL(rover, camera)
    return JsonResponse(response, safe=False)
