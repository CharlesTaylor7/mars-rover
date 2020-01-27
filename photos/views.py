from django.http import HttpResponse
import json
from . import api
from .models import Photo, Camera, Rover
from typing import List
from django.utils.dateparse import parse_date

def load_json(photos: List[dict]) -> List[Photo]:
  def load_photo(obj: dict) -> Photo:
    return Photo(
      id=obj['id'],
      sol=obj['sol'],
      img_src=obj['img_src'],
      earth_date=parse_date(obj['earth_date']),
      camera_id=load_camera(obj['camera']),
    )

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
      landing_date=parse_date(obj['landing_date']),
      launch_date=parse_date(obj['launch_date']),
      status=obj['status'],
      max_sol=obj['max_sol'],
      total_photos=obj['total_photos']
    )

  return [
    load_photo(obj).save()
    for obj in photos
  ]
  pass

def index(request):
  photos = api.getPhotos({
    'sol': 1000,
    'page': 1
  })
  loaded = load_json(photos)
  return HttpResponse( loaded)
