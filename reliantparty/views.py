from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_swagger.views import get_swagger_view


from .models import ReliantParty
from .serializers import ReliantPartySerializer
from .decorators import validate_request_reliant_party_data

schema_view = get_swagger_view(title='Pastebin API')

# Create your views here.
class ReliantPartiesAPI(viewsets.ModelViewSet):
    
    queryset = ReliantParty.objects.all()
    serializer_class = ReliantPartySerializer

    def list(self, request):
        queryset = ReliantParty.objects.all()
        serializer = ReliantPartySerializer(queryset, many=True)
        return Response(serializer.data)

    @validate_request_reliant_party_data
    def create(self, request, *args, **kwargs):
        a_party = ReliantParty.objects.create(
            name=request.data["name"],
            status=request.data["status"],
            email=request.data["email"],
            abn=request.data["abn"]
        )
        return Response(
            data=ReliantPartySerializer(a_party).data,
            status=status.HTTP_201_CREATED
        )
    
    def retrieve(self, request, *args, **kwargs):
        try:
            a_party = self.queryset.get(pk=kwargs["pk"])
            return Response(ReliantPartySerializer(a_party).data)
        except ReliantParty.DoesNotExist:
            return Response(
                data = {
                    "message": "Reliant party does not exist: ".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    
    @validate_request_reliant_party_data
    def update(self, request, *args, **kwargs):
        try:
            a_party = self.queryset.get(pk=kwargs["pk"])
            serializer = ReliantPartySerializer()
            updated_party = serializer.update(a_party, request.data)
            return Response(ReliantPartySerializer(updated_party).data)
        except ReliantParty.DoesNotExist:
            return Response(
                data = {
                    "message": "Reliant party does not exist: ".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    
    def destroy(self, request, *args, **kwargs):
        try:
            a_party = self.queryset.get(pk=kwargs["pk"])
            a_party.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ReliantParty.DoesNotExist:
            return Response(
                data = {
                    "message": "Reliant party does not exist: ".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

