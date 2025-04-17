import requests
from requests.models import Response

from src.core.link_config import link_config

url_fast_api = link_config.fast_api_link

def make_request(idx: int, q: str) -> Response:
    response = requests.get(url=f"{url_fast_api}/v1/methods/items/{idx}?q={q}")
    return response