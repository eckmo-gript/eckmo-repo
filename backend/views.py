import json
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from backend.utils import chatbot_response
from datetime import datetime


class Chat(views.APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        message = data['message']
        #msg = request.data.get('message')
        response = {'status': None}
        try:
            answer = chatbot_response(message)
            response['message'] = {'text': answer, 'timestamp': datetime.now(),
                                   'user': False, 'chat_bot': True}
            response['status'] = 'ok'

        except Exception as err:
            response['status'] = 'error'
            response['error'] = {'cause': str(err),
                                 'status': status.HTTP_400_BAD_REQUEST}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=status.HTTP_200_OK)
