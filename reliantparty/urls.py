from django.urls import path
from .views import ListReliantParties, ReliantPartyDetail


urlpatterns = [
    path('reliantparties/', ListReliantParties.as_view(), name="reliantparties-list-create"),
    path('reliantparties/<int:pk>/', ReliantPartyDetail.as_view(), name="reliantparties-detail"),
]