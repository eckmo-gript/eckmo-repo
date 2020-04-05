import logging

import requests
import inspect
from backend.commands.Command import Command
logger = logging.getLogger(__name__)


class CatsFacts(Command):
    """
    Return a cat fact
    """
    name = 'CatsFacts'

    def respond(self):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1'
        logger.info(f'Sending request to the following Api url : {url}')
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json()
        fact = response['text']
        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with response : {fact} ')

        return fact