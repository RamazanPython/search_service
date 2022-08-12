import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.consts import SearchResultStatusChoice
from utils.models import AbstractTimeTrackable


class SearchData(AbstractTimeTrackable):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_('ID поиска')
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
        return f'Данные поиска {self.id}'
