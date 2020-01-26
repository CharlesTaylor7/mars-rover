from django.http import HttpResponse
import json
from . import api
from .models import Photo, Camera, Rover
from typing import List

def load_json(photos: List[dict]):
  print(Photo())
  pass

def index(request):
  photos = api.getPhotos({
    'sol': 1000,
    'page': 1
  })
  load_json(photos)
  return HttpResponse(json.dumps(photos))
