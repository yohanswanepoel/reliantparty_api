from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from .models import ReliantParty
from .serializers import ReliantPartySerializer
from .decorators import validate_request_reliant_party_data

# Create your views here.
class ListReliantParties(generics.ListAPIView):
    queryset = ReliantParty.objects.all()
    serializer_class = ReliantPartySerializer

class ReliantPartyDetail(generics.RetrieveUpdateDestroyAPIView):
    # GET reliantparties/:id/
    # PUT reliantparties/:id/
    # DELETE reliantparties/:id/

    queryset = ReliantParty.objects.all()
    serializer_class = ReliantPartySerializer

    def get(self, request, *args, **kwargs):
        try:
            a_party = self.queryset.get(pk=kwargs["pk"])
            return Response(ReliantPartySerializer(a_party).data)
        except ReliantParty.DoesNotExist:
            return Response(
                data = {
                    "message": "Reliant party does not exist: ".format(kwargs["pk"])
                }
                status=status.HTTP_404_NOT_FOUND
            )
    
    @validate_request_reliant_party_data
    def put(self, request, *args, **kwargs):
        try:
            a_party = self.queryset.get(pk=kwargs["pk"])
            serializer = ReliantPartySerializer()
            updated_party = serializer.update(a_party, request.data)
            return Response(ReliantPartySerializer(updated_party).data)
        except ReliantParty.DoesNotExist:
            return Response(
                data = {
                    "message": "Reliant party does not exist: ".format(kwargs["pk"])
                }
                status=status.HTTP_404_NOT_FOUND
            )
    
    def delete(self, request, *args, **kwargs):
        try:
            a_party = self.queryset.get(pk=kwargs["pk"])
            a_party.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ReliantParty.DoesNotExist:
            return Response(
                data = {
                    "message": "Reliant party does not exist: ".format(kwargs["pk"])
                }
                status=status.HTTP_404_NOT_FOUND
            )
