from celery import shared_task

from airflow.services import ExchangeRateService


@shared_task()
def exchange_rate_task() -> None:
    ExchangeRateService.save_exchange_rate()
