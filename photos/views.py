from django.http import HttpResponse
import json
from .models import Photo, Camera, Rover
from typing import List
from django.http import JsonResponse
from psycopg2 import sql
from django.db import connection

def get_photos_with_raw_SQL(rover, camera):
    with connection.cursor() as cursor:
        cursor.execute("""
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
                photos_rover.name = %(rover)s
            AND
                photos_camera.name = %(camera)s
            ORDER BY
                photos_photo.earth_date ASC;
        """, {'rover': rover, 'camera': camera})
        return [
            { 'url': row[0], 'date': row[1]}
            for row in cursor.fetchall()
        ]


def index(request, rover, camera):
    response = get_photos_with_raw_SQL(rover, camera)
    return JsonResponse(response, safe=False)
