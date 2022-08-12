from celery import shared_task
from django.utils import timezone
from urllib.error import HTTPError

from typing import Any

from airflow.requests import exchange_rate_get_request
from utils.exception_consts import EXCHANGE_RATE_RESPONSE_NOT_OK


class ExchangeRateResponseError(HTTPError):
    pass


@shared_task()
def exchange_rate_task() -> Any:
    params = {
        'fdate': timezone.now().strftime("%d.%m.%Y")
    }
    response = exchange_rate_get_request(params=params)
    if response.ok:
        pass

    error = ExchangeRateResponseError(
        msg=EXCHANGE_RATE_RESPONSE_NOT_OK,
        url=response.url,
        code=response.status_code,
        hdrs=response.headers,
        fp=None
    )

    return error
