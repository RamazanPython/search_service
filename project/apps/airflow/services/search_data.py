import uuid

from django.http import Http404

from requests.models import Response
from typing import Dict

from airflow.models import SearchData
from utils.consts import SearchDataStatusChoice
from utils.exceptions import SearchDataRequestException
from utils.exception_consts import SEARCH_DATA_RESPONSE_NOT_OK, SEARCH_DATA_NOT_FOUND
from utils.functions import send_post


class SearchDataService:

    def __init__(self, search_id: uuid.uuid4) -> None:
        self.search_id = search_id

    def _create_instance(self, url: str) -> SearchData:
        return SearchData.objects.create(
            search_id=self.search_id,
            url=url,
        )

    def _update_instance(self, response: Response, instance: SearchData) -> None:
        if not response.json():
            instance.status = SearchDataStatusChoice.NO_DATA.value
            instance.save(update_fields=['status'])
        else:
            instance.status = SearchDataStatusChoice.COMPLETED.value
            instance.data = response.json()
            instance.save(update_fields=['status', 'data'])

    def send_request(self, url: str) -> None:
        instance = self._create_instance(url)
        response = send_post(url=url)
        if not response.ok:
            instance.status = SearchDataStatusChoice.FAILED.value
            instance.save(update_fields=['status'])
            raise SearchDataRequestException(SEARCH_DATA_RESPONSE_NOT_OK.format(url))

        self._update_instance(response, instance)

    def find_search_data(self) -> Dict:
        queryset = SearchData.objects.filter(search_id=self.search_id)
        if not queryset.exists():
            raise Http404(SEARCH_DATA_NOT_FOUND)

        items = []
        status = SearchDataStatusChoice.COMPLETED.value
        for instance in queryset:
            if instance.status == SearchDataStatusChoice.PENDING.value:
                status = SearchDataStatusChoice.PENDING.value
            items += instance.data

        return {
            'search_id': self.search_id,
            'status': status,
            'items': items
        }
