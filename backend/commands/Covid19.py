import logging
import string
from datetime import datetime
import inspect
import en_core_web_sm
import requests
from backend.commands.Command import Command
logger = logging.getLogger(__name__)

class Covid19(Command):
    """
    Return an number of cases for an input country
    """
    name = 'Covid19'
    logging.basicConfig(level=logging.INFO)

    def respond(self):

        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')

        sentence = string.capwords(self.user_input)
        nlp = en_core_web_sm.load()
        doc = nlp(sentence)
        logger.info(f'Detected entities in user sentence : {[(X.text, X.label_) for X in doc.ents]}')

        country = None
        for X in doc.ents:
            if(X.label_== 'GPE'):
                country = X.text
        url = 'https://api.covid19api.com/total/country/{}/status/confirmed'.format(country)
        logger.info(f'Sending request to the following Api url : {url}')

        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json()
        cases = 'There is a total of {} confirmed cases in {} by the date of {}.'.format(response[-1]["Cases"], country, datetime.strptime(response[-1]["Date"], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %b %Y'))

        logger.info(f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with response : {cases} ')
        return cases