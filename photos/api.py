import requests
import os

def api_key():
  return os.environ['NASA_API_KEY']

def getPhotos(query):
  query = {
    'api_key': api_key(),
    **query,
  }
  payload = requests.get(
    'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos',
    params = query
  ).json()

  return payload['photos']
