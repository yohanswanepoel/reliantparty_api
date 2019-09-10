import json
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
    
    def make_a_request(self, kind="post", **kwargs):
        """
        Make a post request to create a song
        :param kind: HTTP VERB
        :return:
        """
        if kind == "post":
            return self.client.post(
                reverse(
                    "reliantparties-list-create",
                    kwargs={
                        "version": kwargs["version"]
                    }
                ),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )
        elif kind == "put":
            return self.client.put(
                reverse(
                    "reliantparties-detail",
                    kwargs={
                        "version": kwargs["version"],
                        "pk": kwargs["id"]
                    }
                ),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )
        else:
            return None

    def delete_a_party(self, pk=0):
        return self.client.delete(
            reverse(
                "reliantparties-detail",
                kwargs={
                    "version": "v1",
                    "pk": pk
                }
            )
        )

    def setUp(self):
        self.create_reliant_party("Name1","name@email.com","some abn","active")
        self.create_reliant_party("Name2","name@email.com","some abn 2","testing")
        self.valid_data = {
            "name": "test song",
            "status": "test artist",
            "email": "test song",
            "abn": "test artist"
        }
        self.invalid_data = {
            "name": "test song",
            "abn": "test artist"
        }

class GetAllReliantPartiesTest(BaseViewTest):

    def test_get_all_reliant_parties(self):
        response = self.client.get(
            reverse("reliantparties-list-create",kwargs={"version":"v1"})
        )
        expected = ReliantParty.objects.all()
        serialized = ReliantPartySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AddReliantPartyTest(BaseViewTest):

    def test_create_reliant_party(self):
        response = self.make_a_request(
            kind="post",
            version="v1",
            data=self.valid_data
        )
        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # test with invalid data
        response = self.make_a_request(
            kind="post",
            version="v1",
            data=self.invalid_data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateReliantPartyTest(BaseViewTest):

    def test_update_reliant_party(self):
        response = self.make_a_request(
            kind="put",
            version="v1",
            id=2,
            data=self.valid_data
        )
        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test with invalid data
        response = self.make_a_request(
            kind="put",
            version="v1",
            id=2,
            data=self.invalid_data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteReliantPartyTest(BaseViewTest):

    def test_delete_reliant_party(self):
        response = self.delete_a_party(1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.delete_a_party(100)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)