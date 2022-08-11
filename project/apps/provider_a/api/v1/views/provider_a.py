from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request


class ProviderAViewSet(APIView):

    def search(self, request: Request) -> Response:
        pass
