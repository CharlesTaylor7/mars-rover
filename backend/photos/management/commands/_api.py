import os
import aiohttp
import asyncio
import json
from typing import Union


def base_url():
    return "https://api.nasa.gov/mars-photos/api/v1"


def api_key():
    return os.environ["NASA_API_KEY"]


nasa_api_response = Union[dict, "RateLimited"]


async def fetch(session, relativeUrl, params={}) -> nasa_api_response:
    query_params = {
        "api_key": api_key(),
        **params,
    }
    url = f"{base_url()}/{relativeUrl}"

    async with session.get(url, params=query_params) as response:
        # Http response 429 means we hit the api rate limit
        if response.status == 429:
            return "RateLimited"

        json = await response.json()
        return json


async def get_photos(session, rover="", **query) -> nasa_api_response:
    payload = await fetch(session, f"rovers/{rover}/photos", params=query)

    if "photos" not in payload:
        return payload

    return payload["photos"]


async def get_rovers(session) -> nasa_api_response:
    payload = await fetch(session, f"rovers")

    if "rovers" not in payload:
        return payload

    return payload["rovers"]
