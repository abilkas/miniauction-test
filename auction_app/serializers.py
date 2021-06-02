from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'cash_balance',)

class AnimalSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = ('species', 'name', 'owner')


class LotSerializer(ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__'

class BetSerializer(ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'


# class SelectBetSerializer(Serializer):
#     bet_id = serializers.IntegerField()
