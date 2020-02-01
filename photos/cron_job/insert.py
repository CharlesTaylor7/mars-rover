from django.http import HttpResponse
import json
from . import api
from .models import Photo, Camera, Rover
from typing import List


def insert_photo(obj: dict) -> Photo:
    photo = Photo(
        id=obj['id'],
        sol=obj['sol'],
        img_src=obj['img_src'],
        earth_date=obj['earth_date'],
        camera=insert_camera(obj['camera']),
    )
    photo.save()
    return photo


def insert_camera(obj: dict) -> Camera:
    camera = Camera(
        id=obj['id'],
        name=obj['name'],
        full_name=obj['full_name'],
        rover=Rover(id=obj['rover_id']),
    )
    camera.save()
    return camera


def insert_rover(obj: dict) -> Rover:
    rover = Rover(
        id=obj['id'],
        name=obj['name'],
        landing_date=obj['landing_date'],
        launch_date=obj['launch_date'],
        status=obj['status'],
        max_sol=obj['max_sol'],
        max_date=obj['max_date'],
        total_photos=obj['total_photos'],
    )
    rover.save()
    return rover


def cron_job():
    rovers = api.get_rovers()
    rover_models = [
        insert_rover(rover)
        for rover in rovers
    ]

    # to get all photos,
    # iterate over all 3 rovers
    # from sol 0 to rover.max_sol
    # from page 1 to n until pages come back with less than 25 photos
    photos = api.get_photos(
        rover='spirit',
        sol=1000,
    )

    photo_models = [
        insert_photo(photo)
        for photo in photos
    ]

    return ((rover_models, photo_models))
