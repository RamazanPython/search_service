from django.apps import apps
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from drf_spectacular.utils import extend_schema

from utils.functions import get_flights_data
from utils.serializers import ProviderSerializer


@extend_schema(responses=ProviderSerializer)
@api_view(['POST'])
def search(request: Request) -> Response:
    file_path = apps.get_app_config('provider_a').path + '/response_a.json'
    flights_data = get_flights_data(
        file_path=file_path,
        sleep_duration=30
    )
    return Response(data=ProviderSerializer(flights_data, many=True).data, status=status.HTTP_200_OK)
