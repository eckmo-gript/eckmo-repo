from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Game

class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Game
        fields = [
            'game'
        ]
