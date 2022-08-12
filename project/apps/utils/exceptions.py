from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status

from urllib.error import HTTPError


class ExchangeRateResponseError(HTTPError):
    pass


class SearchResultResponseError(HTTPError):
    pass


class NoDataInResponseError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('По данному search_id данных не найдено')
