from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.consts import SearchResultStatusChoice
from utils.models import AbstractTimeTrackable


class SearchData(AbstractTimeTrackable):
    search_id = models.UUIDField(
        editable=False,
        verbose_name=_('ID поиска')
    )
    service = models.ForeignKey(
        'airflow.Service',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Сервис')
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


class Service(AbstractTimeTrackable):
    name = models.CharField(
        max_length=20,
        verbose_name=_('Название сервиса')
    )

    class Meta:
        verbose_name = _('Сервис')
        verbose_name_plural = _('Сервисы')

    def __str__(self) -> str:
        return f'{self.name}'
