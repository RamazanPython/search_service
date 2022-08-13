from django.conf import settings

from celery import shared_task

from airflow.services import SearchDataService


@shared_task
def send_request_to_provider_a_task(search_id: int) -> None:
    SearchDataService(search_id=search_id).send_request(settings.PROVIDER_A_URL)


@shared_task
def send_request_to_provider_b_task(search_id: int) -> None:
    SearchDataService(search_id=search_id).send_request(settings.PROVIDER_B_URL)
