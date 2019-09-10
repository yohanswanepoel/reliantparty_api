from rest_framework.response import Response
from rest_framework.views import status


def validate_request_reliant_party_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        name = args[0].request.data.get("name", "")
        status = args[0].request.data.get("status", "")
        email = args[0].request.data.get("email", "")
        abn = args[0].request.data.get("abn", "")
        if not name or not status or not email or not abn:
            return Response(
                data={
                    "message": "All fields are mandatory"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated