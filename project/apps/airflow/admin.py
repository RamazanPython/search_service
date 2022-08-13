from django.contrib import admin

from airflow.models import ExchangeRate, SearchData


@admin.register(ExchangeRate)
class ExchangeRate(admin.ModelAdmin):
    list_display = (
        'id',
        'data',
        'created_date',
        'updated_date',
    )


@admin.register(SearchData)
class SearchDataAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'search_id',
        'url',
        'status',
        'created_date',
        'updated_date',
    )
