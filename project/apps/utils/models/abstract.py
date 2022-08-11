from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractTimeTrackable(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания')
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата обновления')
    )

    class Meta:
        abstract = True
        ordering = ('-created_date', '-updated_date')
