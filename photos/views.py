from django.http import HttpResponse
import json
from .models import Photo, Camera, Rover
from typing import List
from django.http import JsonResponse
from psycopg2 import sql
from django.db import connection
from .methods import get_photos_with_ORM, get_photos_with_raw_SQL

def photos(request, rover, camera):
    limit = 100
    method = request.GET.get('method')
    rows = []
    if method == 'ORM':
        rows = get_photos_with_ORM(rover, camera, limit)
    elif method == 'SQL':
        rows = get_photos_with_raw_SQL(rover, camera, limit)
    else:
        raise Exception('Unrecognized method of %s' % method)

    response = [
        {'url': row[0], 'date': row[1]}
        for row in rows
    ]
    return JsonResponse(response, safe=False)

def cameras(request):
    rover = request.GET.get('rover')
    rows = (
        Camera.objects
        .filter(rover__name=rover)
        .values_list('name', 'full_name')
    )
    response = [
        {'name': row[0], 'full_name': row[1]}
        for row in rows
    ]
    return JsonResponse(response, safe=False)
