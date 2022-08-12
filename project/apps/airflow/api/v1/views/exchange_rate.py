from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from drf_spectacular.utils import extend_schema

from airflow.services import ExchangeRateService


@extend_schema(
    description='Эндпоинт для тестирования запроса на проверку курса валют'
)
@api_view(['GET'])
def exchange_rate(request: Request) -> Response:
    response = ExchangeRateService.get_exchange_rate()
    return Response(response.text)
