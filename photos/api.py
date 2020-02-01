import requests
import os


def api_key():
    return os.environ['NASA_API_KEY']


def get_photos(rover='', **query):
    query_params = {
        'api_key': api_key(),
        **query,
    }
    payload = requests.get(
        f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos',
        params=query_params
    ).json()

    return payload['photos']


def get_rovers():
    query_params = {
        'api_key': api_key(),
    }
    payload = requests.get(
        f'https://api.nasa.gov/mars-photos/api/v1/rovers',
        params=query_params
    ).json()

    return payload['rovers']
