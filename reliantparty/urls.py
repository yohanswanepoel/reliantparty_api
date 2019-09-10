from django.urls import path
from django.conf.urls import url, include
from .views import ReliantPartiesAPI, schema_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('reliantparties',ReliantPartiesAPI, basename="reliantparty")

urlpatterns = [
    url('^$', schema_view),
    url(r'^', include(router.urls)),
]
