from django.urls import path
from django.conf.urls import url, include
from .views import ReliantPartiesAPI
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register('reliantparties',ReliantPartiesAPI, basename="reliantparty")
schema_view = get_swagger_view(title='Reliant Party API')

urlpatterns = [
    url('^$', schema_view),
    url(r'^', include(router.urls)),
]
