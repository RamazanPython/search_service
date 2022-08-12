from celery import shared_task

from requests.models import Response

from airflow.services import ExchangeRateService


@shared_task()
def exchange_rate_task() -> Response:
    return ExchangeRateService.get_exchange_rate()
