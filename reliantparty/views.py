from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_swagger.views import get_swagger_view


from .models import ReliantParty
from .serializers import ReliantPartySerializer, ReliantPartyDetailSerializer
from .decorators import validate_request_reliant_party_data

schema_view = get_swagger_view(title='Reliant Party API')


class HealthAPI(viewsets.ViewSet):

	def list(self, request, format=None):
		data = { "status": "up" }
		return Response(data)	

# Create your views here.
class ReliantPartiesAPI(viewsets.ModelViewSet):
    
    queryset = ReliantParty.objects.all()
    serializer_class = ReliantPartySerializer
    filter_fields = ('status')

    def get_queryset(self, query_params):
        status = self.request.query_params.get('status', None)
        if status is not None:
            return ReliantParty.objects.filter(status=status)
        else:
            return ReliantParty.objects.all()

    @action(detail=False)
    def count(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(request.query_params))
        content = {'count': queryset.count()}
        return Response(content)

    def list(self, request):
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = ReliantParty.objects.filter(status=status)
        else:
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
            data=ReliantPartyDetailSerializer(a_party).data,
            status=status.HTTP_201_CREATED
        )
    
    def retrieve(self, request, *args, **kwargs):
        try:
            a_party = self.queryset.get(pk=kwargs["pk"])
            return Response(ReliantPartyDetailSerializer(a_party).data)
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
            return Response(ReliantPartyDetailSerializer(updated_party).data)
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

