from django.urls import path
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from eckmo.utils import chatbot_response


class Predict(views.APIView):
    def post(self, request):
        for entry in request.data['msg']:
            msg = entry
            try:
                answer = chatbot_response(msg)

            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        return Response(answer, status=status.HTTP_200_OK)