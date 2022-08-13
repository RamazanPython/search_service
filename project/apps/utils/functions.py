import json
import time
import requests

from typing import Union


def get_flights_data(file_path: str, sleep_duration: int) -> Union[dict, None]:
    try:
        with open(file_path, 'r') as f:
            flights = json.load(f)
        time.sleep(sleep_duration)
    except FileNotFoundError:
        return None

    return flights


def send_post(url, data=None, params=None, headers=None, files=None, json=None):
    if data:
        response = requests.post(url, data=data, params=params, headers=headers, files=files)
    elif json:
        response = requests.post(url, json=json, params=params, headers=headers, files=files)
    else:
        response = requests.post(url, json=json, params=params, headers=headers, files=files)
    return response


def send_get(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    return response


def send_put(url, data=None, params=None, headers=None, files=None, json=None):
    if data:
        response = requests.put(url, data=data, params=params, headers=headers, files=files)
    elif json:
        response = requests.put(url, json=json, params=params, headers=headers, files=files)
    else:
        raise ValueError('Need to pass the argument data or json')
    return response

