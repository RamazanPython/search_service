import json
import time

from typing import Any


def get_flights_data() -> Any:
    with open('response_a.json') as f:
        flights = json.load(f)
    time.sleep(60)
    return flights
