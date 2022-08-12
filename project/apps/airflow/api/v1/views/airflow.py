import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from airflow.models import SearchData


@api_view(['POST'])
def search(request: Request) -> Response:
    search_id = uuid.uuid4()

    return Response(status=status.HTTP_200_OK)
