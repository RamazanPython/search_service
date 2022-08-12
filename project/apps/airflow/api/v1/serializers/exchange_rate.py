from rest_framework import serializers

from airflow.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = (
            'id',
            'data',
            'created_date'
        )
