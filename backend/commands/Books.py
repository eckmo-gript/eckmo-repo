import logging
from random import randint
import requests
import inspect
from backend.commands.Command import Command
logger = logging.getLogger(__name__)

class Books(Command):
    """
    Return a book
    """
    name = 'Books'

    def respond(self):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        id = randint(0, 10000)
        url = 'http://gen.lib.rus.ec/json.php?ids={}&fields=Title,Author,year,MD5,coverurl,topic,commentary,pages'.format(id)
        logger.info(f'Sending request to the following Api url : {url}')
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json()
        print(response)
        book = response[0]['title']
        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with response : {book} ')

        return book