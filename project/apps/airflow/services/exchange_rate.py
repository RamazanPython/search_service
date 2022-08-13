from django.conf import settings
from django.utils import timezone

from bs4 import BeautifulSoup
from requests.models import Response

from airflow.models import ExchangeRate
from utils.exceptions import ExchangeRateRequestException
from utils.exception_consts import EXCHANGE_RATE_RESPONSE_NOT_OK
from utils.functions import send_get


class ExchangeRateService:
    
    @staticmethod
    def get_exchange_rate() -> Response:
        params = {
            'fdate': timezone.now().strftime("%d.%m.%Y")
        }
        url = f'{settings.EXCHANGE_RATE_URL}'
        response = send_get(url, params=params)
        if response.ok:
            return response

        raise ExchangeRateRequestException(EXCHANGE_RATE_RESPONSE_NOT_OK)

    @staticmethod
    def save_exchange_rate() -> ExchangeRate:
        response = ExchangeRateService.get_exchange_rate()
        xml = BeautifulSoup(response.text.encode(), features='xml')
        items = xml.find_all('item')
        data = {}
        for item in items:
            currency_code = item.find('title').text
            denomination = item.find('description').text
            data[currency_code] = denomination

        return ExchangeRate.objects.create(data=data)
