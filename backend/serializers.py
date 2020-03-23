from rest_framework import serializers


class AnswerSerializer(serializers.Serializer):
    message = serializers.TextField()
    delivered_at = serializers.DateTimeField(auto_now_add=True)
    confidence_score = serializers.IntegerField()


class EntrySerializer(serializers.Serializer):
    message = serializers.TextField()
    arrived_at = serializers.DateTimeField(auto_now_add=True)
    sentiment = serializers.TextField()
