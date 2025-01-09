from django.http import HttpResponse
import json
from photos.models import Photo, Camera, Rover
from typing import List
from django.http import JsonResponse
from psycopg2 import sql
from django.db import connection


def photos(request, rover, camera):
    limit = 100
    rows = (
        Photo.objects.filter(camera__name=camera)
        .filter(camera__rover__name=rover)
        .order_by("earth_date")[:limit]
        .values_list("img_src", "earth_date")
    )
    response = [{"url": row[0], "date": row[1]} for row in rows]
    return JsonResponse(response, safe=False)


def cameras(request):
    rover = request.GET.get("rover")
    rows = Camera.objects.filter(rover__name=rover).values_list("name", "full_name")
    response = [{"name": row[0], "full_name": row[1]} for row in rows]
    return JsonResponse(response, safe=False)
