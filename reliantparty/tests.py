from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import ReliantParty
from .serializers import ReliantPartySerializer

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_reliant_party(name="", email="", abn="", status=""):
        if name != "" and email != "" and abn != "" and status != "":
            ReliantParty.objects.create(name=name, email=email, abn=abn, status=status)
        
    def setUp(self):
        self.create_reliant_party("Name1","name@email.com","some abn","active")
        self.create_reliant_party("Name2","name@email.com","some abn 2","testing")

class GetAllReliantPartiesTest(BaseViewTest):

    def test_get_all_reliant_parties(self):
        response = self.client.get(
            reverse("reliantparties-all",kwargs={"version":"v1"})
        )
        expected = ReliantParty.objects.all()
        serialized = ReliantPartySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)