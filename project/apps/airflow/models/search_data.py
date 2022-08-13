from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.consts import SearchResultStatusChoice
from utils.models import AbstractTimeTrackable


class SearchData(AbstractTimeTrackable):
    """
        Данные поиска
    """
    search_id = models.UUIDField(
        editable=False,
        verbose_name=_('ID поиска')
    )
    url = models.URLField(
        verbose_name=_('URL сервиса')
    )
    status = models.CharField(
        max_length=9,
        default=SearchResultStatusChoice.PENDING.value,
        choices=SearchResultStatusChoice.choices(),
        verbose_name=_('Статус')
    )
    data = models.JSONField(
        null=True,
        blank=True,
        verbose_name=_('Результат поиска')
    )

    class Meta:
        verbose_name = _('Результат поиска')
        verbose_name_plural = _('Результаты поиска')

    def __str__(self) -> str:
        return f'{self.search_id}'
