from rest_framework import serializers
from .models import ReliantParty

class ReliantPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliantParty
        fields = ("id","name","status","email",'abn')

class ReliantPartyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliantParty
        fields = '__all__'