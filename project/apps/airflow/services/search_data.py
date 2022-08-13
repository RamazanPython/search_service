import uuid

from requests.models import Response
from typing import Union

from airflow.models import SearchData
from utils.consts import SearchResultStatusChoice
from utils.exceptions import SearchDataRequestException
from utils.exception_consts import SEARCH_DATA_RESPONSE_NOT_OK
from utils.functions import send_post


class SearchDataService:

    def __init__(self, search_id: uuid.uuid4) -> None:
        self.search_id = search_id

    def send_request(self, url: str) -> None:
        response = send_post(url=url)
        if not response.ok:
            raise SearchDataRequestException(SEARCH_DATA_RESPONSE_NOT_OK.format(url))

        self._create_search_data(response)

    def _create_search_data(self, response: Response) -> None:
        if not response.json():
            SearchData.objects.create(
                search_id=self.search_id,
                url=response.url,
                status=SearchResultStatusChoice.NO_DATA.value
            )
        else:
            SearchData.objects.create(
                search_id=self.search_id,
                url=response.url,
                data=response.json(),
                status=SearchResultStatusChoice.COMPLETED.value
            )
