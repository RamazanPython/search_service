import uuid

from requests.models import Response

from airflow.models import SearchData
from utils.consts import SearchResultStatusChoice
from utils.exceptions import SearchResultResponseError, NoDataInResponseError
from utils.functions import send_get


class SearchDataService:

    def __init__(self, search_id: uuid.uuid4, url: str) -> None:
        self.search_id = search_id
        self.url = url
        self.instance = self._create_instance()

    def _create_instance(self) -> SearchData:
        return SearchData.objects.create(pk=self.search_id)

    def send_request(self) -> None:
        response = send_get(url=self.url)
        if not response.ok:
            raise SearchResultResponseError(
                url=self.url,
                code=response.status_code,
                msg=response.text,
                hdrs=response.headers,
                fp=None
            )

        self._create_search_data(response)

    def _create_search_data(self, response: Response) -> None:
        if not response.json():
            self.instance.status = SearchResultStatusChoice.NO_DATA.value
            self.instance.save(update_fields=['status'])

        self.instance.data = response.json()
        self.instance.url = self.url
        self.instance.status = SearchResultStatusChoice.COMPLETED.value
        self.instance.save(update_fields=['data', 'status', 'url'])
