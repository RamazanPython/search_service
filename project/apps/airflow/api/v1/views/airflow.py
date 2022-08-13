import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from celery import group
from drf_spectacular.utils import extend_schema

from airflow.api.v1.serializers import SearchDataSerializer, SearchIdSerializer
from airflow.tasks import send_request_to_provider_a_task, send_request_to_provider_b_task
from airflow.services import SearchDataService


@extend_schema(responses=SearchIdSerializer)
@api_view(['POST'])
def search(request: Request) -> Response:
    search_id = uuid.uuid4()
    g = group(
        send_request_to_provider_a_task.s(search_id),
        send_request_to_provider_b_task.s(search_id),
    )
    g()
    result = {'search_id': search_id}
    return Response(SearchIdSerializer(result).data, status=status.HTTP_200_OK)


@extend_schema(responses=SearchDataSerializer)
@api_view(['GET'])
def results(request: Request, search_id: int, currency: str) -> Response:
    result = SearchDataService(search_id=search_id).find_search_data(currency)
    return Response(data=SearchDataSerializer(result).data, status=status.HTTP_200_OK)
