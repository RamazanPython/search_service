from rest_framework import serializers

from airflow.models import SearchData


class SearchDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchData
        fields = (
            'id',
            'status',
            'data',
        )
