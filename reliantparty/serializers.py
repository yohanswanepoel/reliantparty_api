from rest_framework import serializers
from .models import ReliantParty

class ReliantPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliantParty
        fields = ("pk","name","status","email",'abn')