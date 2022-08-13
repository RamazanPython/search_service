from rest_framework import serializers


class PricingSerializer(serializers.Serializer):
    total = serializers.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    base = serializers.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    taxes = serializers.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    currency = serializers.CharField()


class DepArrSerializer(serializers.Serializer):
    at = serializers.DateTimeField()
    airport = serializers.CharField()


class SegmentsSerializer(serializers.Serializer):
    operating_airline = serializers.CharField()
    marketing_airline = serializers.CharField()
    flight_number = serializers.IntegerField()
    equipment = serializers.CharField()
    dep = DepArrSerializer()
    arr = DepArrSerializer()
    baggage = serializers.CharField()


class FlightSerializer(serializers.Serializer):
    duration = serializers.IntegerField()
    segments = SegmentsSerializer(many=True)


class ConvertedPriceSerializer(serializers.Serializer):
    amount = serializers.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    currency = serializers.CharField()


class ProviderSerializer(serializers.Serializer):
    flights = FlightSerializer(many=True)
    refundable = serializers.BooleanField()
    validating_airline = serializers.CharField()
    pricing = PricingSerializer()
    price = ConvertedPriceSerializer(allow_null=True)
