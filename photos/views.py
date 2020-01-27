from django.http import HttpResponse
import json
from . import api
from .models import Photo, Camera, Rover
from typing import List

def load_photo(obj: dict) -> Photo:

  photo = Photo(
    id=obj['id'],
    sol=obj['sol'],
    img_src=obj['img_src'],
    earth_date=obj['earth_date'],
    camera_id=load_camera(obj['camera']),
  )
  photo.save()
  return photo

def load_camera(obj: dict) -> Camera:
  camera = Camera(
    id=obj['id'],
    name=obj['name'],
    full_name=obj['full_name'],
    rover_id=Rover(id=obj['rover_id']),
  )
  camera.save()
  return camera

def load_rover(obj: dict) -> Rover:
  rover = Rover(
    id=obj['id'],
    name=obj['name'],
    landing_date=obj['landing_date'],
    launch_date=obj['launch_date'],
    status=obj['status'],
    max_sol=obj['max_sol'],
    max_date=obj['max_date'],
    total_photos=obj['total_photos'],
  ).save()
  rover.save()
  return rover

def index(request):
  rovers = api.get_rovers()
  rover_models = [
    load_rover(rover)
    for rover in rovers
  ]

  # to get all photos,
  # iterate over all 3 rovers
  # from sol 0 to rover.max_sol
  # from page 1 to n until pages come back with less than 25 photos
  photos = api.get_photos(
    rover = 'spirit',
    sol = 1000,
  )
  # return HttpResponse(photos)
  photo_models = [
    load_photo(photo)
    for photo in photos
  ]

  return HttpResponse((rover_models, photo_models))
