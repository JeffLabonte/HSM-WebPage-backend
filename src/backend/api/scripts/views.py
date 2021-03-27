from rest_framework.views import APIView


class ScriptCreateView(APIView):
    def post(self, request, format=None):
        data = request.data
