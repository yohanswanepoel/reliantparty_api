from django.shortcuts import render
from rest_framework import generics
from .models import ReliantParty
from .serializers import ReliantPartySerializer

# Create your views here.
class ListReliantParties(generics.ListAPIView):
    queryset = ReliantParty.objects.all()
    serializer_class = ReliantPartySerializer