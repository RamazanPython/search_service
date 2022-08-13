from django.contrib import admin
from django.db import models

from django_json_widget.widgets import JSONEditorWidget

from airflow.models import ExchangeRate, SearchData


@admin.register(ExchangeRate)
class ExchangeRate(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    list_display = (
        'id',
        'created_date',
        'updated_date',
    )
    list_filter = (
        'created_date',
    )


@admin.register(SearchData)
class SearchDataAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    list_display = (
        'id',
        'search_id',
        'url',
        'status',
        'created_date',
        'updated_date',
    )
    list_filter = (
        'status',
        'created_date',
    )
