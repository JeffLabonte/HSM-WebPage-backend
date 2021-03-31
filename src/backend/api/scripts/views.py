from backend.api.scripts.serializers import ScriptWriteSerializer

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class ScriptCreateView(APIView):
    def post(self, request, format=None):
        payload = {
            "method": request.method,
            "data": request.data,
        }
        serializer = ScriptWriteSerializer(data=payload)
        if serializer.is_valid():
            # TODO Change for something like `audited_send` so it is implicit that I am saving and sending
            serializer.save()
            # TODO Add call to get return
            # Use something else to save()?
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
