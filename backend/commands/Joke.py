import logging
import inspect
import requests
logger = logging.getLogger(__name__)

from backend.commands.Command import Command


class Joke(Command):
    """
    Return a joke
    """
    name = 'Joke'

    def respond(self):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        url = 'https://icanhazdadjoke.com/'
        logger.info(f'Sending request to the following Api url : {url}')
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json()
        joke = response['joke']
        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with response : {joke} ')

        return joke