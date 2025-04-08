import requests
from src.core.link_config import link_config

url_fast_api = link_config.fast_api_link

def make_request(idx: int, q: str) -> dict:
    response = requests.get(url=f"{url_fast_api}/v1/methods/items/{idx}?q={q}").json()
    return response