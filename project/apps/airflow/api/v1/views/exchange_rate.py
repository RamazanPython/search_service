from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from drf_spectacular.utils import extend_schema

from airflow.services import ExchangeRateService
from airflow.api.v1.serializers import ExchangeRateSerializer


@extend_schema(
    description='Получить данные по курсу валют вручную',
    responses=ExchangeRateSerializer
)
@api_view(['GET'])
def get_exchange_rate_manually(request: Request) -> Response:
    instance = ExchangeRateService.save_exchange_rate()
    return Response(ExchangeRateSerializer(instance).data, status=status.HTTP_200_OK)
