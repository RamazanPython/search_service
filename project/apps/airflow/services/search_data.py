import uuid

from requests.models import Response

from airflow.models import SearchData
from utils.consts import SearchResultStatusChoice
from utils.exceptions import SearchDataRequestException
from utils.exception_consts import SEARCH_DATA_RESPONSE_NOT_OK
from utils.functions import send_post


class SearchDataService:

    def __init__(self, search_id: uuid.uuid4) -> None:
        self.search_id = search_id

    def _create_instance(self, url: str) -> SearchData:
        return SearchData.objects.create(
            search_id=self.search_id,
            url=url,
        )

    def send_request(self, url: str) -> None:
        instance = self._create_instance(url)
        response = send_post(url=url)
        if not response.ok:
            raise SearchDataRequestException(SEARCH_DATA_RESPONSE_NOT_OK.format(url))

        self._create_search_data(response, instance)

    def _create_search_data(self, response: Response, instance: SearchData) -> None:
        if not response.json():
            instance.status = SearchResultStatusChoice.NO_DATA.value
            instance.save(update_fields=['status'])
        else:
            instance.status = SearchResultStatusChoice.COMPLETED.value
            instance.data = response.json()
            instance.save(update_fields=['status', 'data'])
