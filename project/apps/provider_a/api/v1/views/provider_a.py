from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from provider_a.functions import get_flights_data
from provider_a.api.v1.serializers import ProviderASerializer


@api_view(['POST'])
def search(request: Request) -> Response:
    flights_data = get_flights_data()
    return Response(ProviderASerializer(flights_data).data, status=status.HTTP_200_OK)
