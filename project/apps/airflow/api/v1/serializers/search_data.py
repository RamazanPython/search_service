from rest_framework import serializers

from utils.serializers import ProviderSerializer
from utils.consts import SearchDataStatusChoice


class SearchIdSerializer(serializers.Serializer):
    search_id = serializers.UUIDField()


class SearchDataSerializer(serializers.Serializer):
    search_id = serializers.UUIDField()
    status = serializers.ChoiceField(
        choices=SearchDataStatusChoice.choices(),
        allow_null=True,
    )
    items = ProviderSerializer(
        many=True,
        allow_null=True,
    )
