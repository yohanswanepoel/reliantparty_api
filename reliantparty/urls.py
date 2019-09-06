from django.urls import path
from .views import ListReliantParties


urlpatterns = [
    path('reliantparties/', ListReliantParties.as_view(), name="reliantparties-all"),
]