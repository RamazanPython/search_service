from rest_framework import serializers


class ProviderASerializer(serializers.Serializer):
    data = serializers.JSONField()
