import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from celery import group

from airflow.api.v1.serializers import SearchDataSerializer
from airflow.tasks import send_request_to_provider_a_task, send_request_to_provider_b_task
from airflow.services import SearchDataService


@api_view(['POST'])
def search(request: Request) -> Response:
    search_id = uuid.uuid4()
    group(
        send_request_to_provider_a_task.si(search_id),
        send_request_to_provider_b_task.si(search_id),
    ).apply_async()
    return Response(data={'search_id': search_id}, status=status.HTTP_200_OK)


@api_view(['GET'])
def results(request: Request, search_id: int, currency: str) -> Response:
    result = SearchDataService(search_id=search_id).find_search_data()
    return Response(data=SearchDataSerializer(result).data, status=status.HTTP_200_OK)
