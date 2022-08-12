from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from airflow.models import SearchResult


@api_view(['POST'])
def search(request: Request) -> Response:
    search_result = SearchResult.objects.create()
    return Response({'search_id': search_result.pk}, status=status.HTTP_200_OK)
