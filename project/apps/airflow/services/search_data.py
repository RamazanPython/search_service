import uuid

from django.conf import settings

from requests.models import Response

from airflow.models import SearchData
from utils.consts import ProvidersUrlNameChoice, SearchResultStatusChoice
from utils.exceptions import SearchResultResponseError, NoDataInResponseError
from utils.functions import send_get


class SearchDataService:

    PROJECT_URL = settings.PROJECT_URL

    def __init__(self, search_id: uuid.uuid4, endpoint: ProvidersUrlNameChoice) -> None:
        self.search_id = search_id
        self.endpoint = endpoint
        self.instance = self.get_instance()

    def get_instance(self) -> SearchData:
        return SearchData.objects.get(pk=self.search_id)

    def send_request(self) -> Response:
        url = f'{SearchDataService.PROJECT_URL}/{self.endpoint}'
        response = send_get(url=url)
        if not response.ok:
            raise SearchResultResponseError(
                url=url,
                code=response.status_code,
                msg=response.text,
                hdrs=response.headers,
                fp=None
            )

        return self._create_search_data(response)

    def _create_search_data(self, response: Response) -> Response:
        if not response.json():
            raise NoDataInResponseError

        data = response.json()
        if self.instance.data:
            saved_data = list(self.instance.data)
            saved_data += list(data)
            self.instance.data = saved_data
            self.instance.status = SearchResultStatusChoice.COMPLETED.value
            self.instance.save(update_fields=['data', 'status'])

        self.instance.data = data
        self.instance.save(update_fields=['data'])
        return response
