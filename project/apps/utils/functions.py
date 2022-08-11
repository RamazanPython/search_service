import json
import time

from typing import Union


def get_flights_data(file_path: str, sleep_duration: int) -> Union[dict, None]:
    try:
        with open(file_path, 'r') as f:
            flights = json.load(f)
        time.sleep(sleep_duration)
    except FileNotFoundError:
        return None

    return flights
