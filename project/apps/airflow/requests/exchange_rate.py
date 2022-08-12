from django.conf import settings

from utils.functions import send_get


def exchange_rate_get_request(*, token=None, params=None):
    headers = {'Authorization': f'Bearer {token}'} if token else None
    url = f'{settings.EXCHANGE_RATE_URL}'
    return send_get(url, headers=headers, params=params)
