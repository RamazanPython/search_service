from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractTimeTrackable


class ExchangeRate(AbstractTimeTrackable):
    """
        Курс валют
    """
    data = models.JSONField(
        null=True,
        blank=True,
        verbose_name=_('Данные курса валют')
    )

    class Meta:
        verbose_name = _('Курс валют')
        verbose_name_plural = _('Курс валют')

    def __str__(self) -> str:
        return f'Курс валют за {self.created_date}'
