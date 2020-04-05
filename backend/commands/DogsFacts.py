import logging

import requests
import inspect
logger = logging.getLogger(__name__)
from backend.commands.Command import Command


class DogsFacts(Command):
    """
    Return a dog fact
    """
    name = 'DogsFacts'

    def respond(self):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=dog&amount=1'
        logger.info(f'Sending request to the following Api url : {url}')
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json()
        fact = response['text']
        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with response : {fact} ')

        return fact