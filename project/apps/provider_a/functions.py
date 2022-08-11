import json
import os
import time


module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'response_a.json')


def get_flights_data() -> dict:
    with open(file_path, 'r') as f:
        flights = json.load(f)
    time.sleep(60)
    return {'data': flights}
