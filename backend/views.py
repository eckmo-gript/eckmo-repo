import json
import inspect
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
import logging
from backend.Eckmo import Eckmo
from datetime import datetime

logger = logging.getLogger(__name__)


class Chat(views.APIView):
    def post(self, request):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        data = json.loads(request.body.decode('utf-8'))
        message = data['message']
        response = {'status': None}
        try:
            answer = Eckmo().respond(message)
            response['message'] = {'text': answer, 'timestamp': datetime.now(),
                                   'user': False, 'eckmo': True}
            response['status'] = 'ok'

        except Exception as err:
            response['status'] = 'error'
            response['error'] = {'cause': str(err),
                                 'status': status.HTTP_400_BAD_REQUEST}
            logger.exception('Exception :', str(err), status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        logger.info(f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with response : {response}')
        return Response(response, status=status.HTTP_200_OK)
