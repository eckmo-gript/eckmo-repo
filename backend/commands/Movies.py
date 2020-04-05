import logging
import string
import inspect
from random import randint

from eckmo.settings import MOVIEDB_API_KEY

logger = logging.getLogger(__name__)
import en_core_web_sm
import requests
from backend.commands.Command import Command


class Movies(Command):
    """
    Return a Movie
    """
    name = 'Movies'

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
            if X.label_ == 'PERSON':
                person = X.text

        noun = None
        for X in [y for y in doc if not y.is_stop and y.pos_ != 'PUNCT']:
            if X.pos_ == 'NOUN' and X.orth_ != 'Movie':
                noun = X.orth_

        type = True
        url = 'https://api.themoviedb.org/3/trending/movie/day?api_key={}'.format(MOVIEDB_API_KEY)
        if noun:
            url = 'https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query={}&page=1&include_adult=false'.format(
                self.api_key, noun)
            type = False
        if person:
            url = 'https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query={}&page=1&include_adult=false'.format(
                self.api_key, person)
            type = False

        logger.info(f'Sending request to the following Api url : {url}')

        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json()
        id = randint(0, len(response['results']))

        if type:
            movie = 'I suggest you to watch {} released in {}, here is the complete overview: {} '.format(
                response['results'][id]['title'], response['results'][id]['release_date'],
                response['results'][id]['overview'])
        else:

            movie = 'I suggest you to watch {} released in {}, here is the complete overview: {} '.format(
                response['results'][id]['title'], response['results'][id]['release_date'],
                response['results'][id]['overview'])

        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with response : {movie} ')
        return movie
