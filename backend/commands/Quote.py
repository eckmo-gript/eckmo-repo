import logging
import string
import inspect
from random import randint

logger = logging.getLogger(__name__)
import en_core_web_sm
import requests
from backend.commands.Command import Command


class Quote(Command):
    """
    Return a Quote
    """
    name = 'Quote'

    def respond(self):

        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')

        sentence = string.capwords(self.user_input)
        nlp = en_core_web_sm.load()
        doc = nlp(sentence)
        logger.info(f'Detected entities in user sentence : {[(X.text, X.label_) for X in doc.ents]}')
        logger.info(
            f'Detected verbatim in user sentence : {[(x.orth_, x.pos_, x.lemma_) for x in [y for y in doc if not y.is_stop and y.pos_ != {}]]}'.format(
                'PUNCT'))

        person = None
        for X in doc.ents:
            if (X.label_ == 'PERSON'):
                person = X.text

        noun = None
        for X in [y for y in doc if not y.is_stop and y.pos_ != 'PUNCT']:
            if (X.pos == 'NOUN'):
                noun = X.orth_

        type = True
        url = 'https://quote-garden.herokuapp.com/quotes/random'
        if noun:
            url = 'https://quote-garden.herokuapp.com/quotes/search/{}'.format(noun)
            type = False
        if person:
            url = 'https://quote-garden.herokuapp.com/quotes/author/{}'.format(person)
            type = False

        logger.info(f'Sending request to the following Api url : {url}')

        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json()
        if type:
            quote = '{} - {}'.format(response['quoteText'], response['quoteAuthor'])
        else:
            id = randint(0, len(response['results']))
            quote = '{} - {}'.format(response['results'][id]['quoteText'], response['results'][id]['quoteAuthor'])

        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with response : {quote} ')
        return quote
