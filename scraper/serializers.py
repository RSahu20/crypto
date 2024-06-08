from rest_framework import serializers

class ScrapCoinSerializer(serializers.Serializer):
    coins = serializers.ListField(
        child=serializers.CharField(max_length=100)
    )

class ScrapCoinStatusSerializer(serializers.Serializer):
    job_id = serializers.CharField()