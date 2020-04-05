import logging
from backend.Handlers.CommandsHandler import CommandsHandler
from backend.Handlers.ResponsesHandler import ResponsesHandler
import inspect

logger = logging.getLogger(__name__)


class Eckmo:

    def __init__(self):
        self.cmd_handler = CommandsHandler(self)
        self.rsp_handler = ResponsesHandler(self)

    def respond(self, request):
        """
        Create a response to a user input through the CommandsHandler
        :param request: Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return : A string response from Eckmo
        """
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')

        response = None

        result = self.rsp_handler.chatbot_response(request)
        cmd = self.cmd_handler.choose_command(result['command'], request)

        if cmd is not None:
            try:
                response = str(cmd.respond())
                logger.info(f'Input "{request}" generates response "{response}" from command "{cmd}"')

            except Exception as ex:
                logger.exception('Error : Failed to load response from command :', str(ex))
        else:
            try:
                response = str(result['response'])
                logger.info(f'Input "{request}" generates response "{response}" from command "{cmd}"')
            except Exception as err:
                logger.exception('Exception :', str(err))

        logger.info(f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with response {response}')
        return response
