from django.http import HttpResponse
import json
from .models import Photo, Camera, Rover
from typing import List
from django.http import JsonResponse
from psycopg2 import sql


def get_photos_with_raw_SQL(rover, camera):
    return sql.SQL("""
        SELECT photos_photo.img_src, photos_photo.earth_date
        FROM photos_photo
        INNER JOIN photos_camera
            ON photos_photo.camera_id=photos_camera.id
        INNER JOIN photos_rover
            ON photos_camera.rover_id=photos_rover.id
        WHERE   photos_rover.name='{rover}'
        AND photos_camera.name='{camera}';
    """).format(
        rover=sql.Identifier(rover),
        camera=sql.Identifier(camera),
    )


def index(request, rover, camera):
    print(rover)
    print(camera)
    response = [{
        'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG',
    }, {
        'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG',
    }]
    return JsonResponse(response, safe=False)
