from django.http import HttpResponse
import json
from .models import Photo, Camera, Rover
from typing import List
from django.http import JsonResponse


def get_photos_with_raw_SQL(rover, camera):
    return """
    SELECT photos_photo.img_src, photos_photo.earth_date
        FROM photos_photo
        INNER JOIN photos_camera
            ON photos_photo.camera_id=photos_camera.id
        INNER JOIN photos_rover
            ON photos_camera.rover_id=photos_rover.id
        WHERE photos_camera.name='FHAZ'
        AND photos_rover.name='Curiosity';
    """


def index(request, rover, camera):
    print(rover)
    print(camera)
    response = [{
        'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG',
    }, {
        'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG',
    }]
    return JsonResponse(response, safe=False)
