from django.http import HttpResponse
import json
from . import api
from .models import Photo, Camera, Rover
from typing import List

def load_photo(obj: dict) -> Photo:
  return Photo(
    id=obj['id'],
    sol=obj['sol'],
    img_src=obj['img_src'],
    earth_date=obj['earth_date'],
    camera_id=load_camera(obj['camera']),
  ).save()

def load_camera(obj: dict) -> Camera:
  return Camera(
    id=obj['id'],
    name=obj['name'],
    full_name=obj['full_name'],
    rover_id=Rover(id=obj['rover_id']),
  ).save()

def load_rover(obj: dict) -> Rover:
  return Rover(
    id=obj['id'],
    name=obj['name'],
    landing_date=obj['landing_date'],
    launch_date=obj['launch_date'],
    status=obj['status'],
    max_sol=obj['max_sol'],
    max_date=obj['max_date'],
    total_photos=obj['total_photos'],
  ).save()

def index(request):
  rovers = api.get_rovers()
  rover_models = [
    load_rover(rover)
    for rover in rovers
  ]

  photos = api.get_photos(
    rover = 'curiosity',
    sol = 1000,
    page = 1,
  )

  photo_models = [
    load_photo(photo)
    for photo in photos
  ]

  return HttpResponse((rover_models, photo_models))
