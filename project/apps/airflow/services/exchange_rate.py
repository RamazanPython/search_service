from django.utils import timezone

from requests.models import Response

from airflow.requests import exchange_rate_get_request
from airflow.exceptions import ExchangeRateResponseError
from utils.exception_consts import EXCHANGE_RATE_RESPONSE_NOT_OK


class ExchangeRateService:
    
    @staticmethod
    def get_exchange_rate() -> Response:
        params = {
            'fdate': timezone.now().strftime("%d.%m.%Y")
        }
        response = exchange_rate_get_request(params=params)
        if response.ok:
            return response

        error = ExchangeRateResponseError(
            msg=EXCHANGE_RATE_RESPONSE_NOT_OK,
            url=response.url,
            code=response.status_code,
            hdrs=response.headers,
            fp=None
        )
        raise error
