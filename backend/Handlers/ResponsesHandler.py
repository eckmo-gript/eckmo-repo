import random
import json
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import os
import logging
import nltk
from nltk.stem import WordNetLemmatizer
from eckmo import settings
import inspect

logger = logging.getLogger(__name__)


class ResponsesHandler:
    """
    The framework that accepts user input and forwards it to the correct response
    """

    # Load Eckmo Model
    model_path = os.path.join(settings.CHATBOT_ROOT, 'chatbot_model.h5')
    # Load intents file
    intents_path = os.path.join(settings.CHATBOT_ROOT, 'intents.json')
    # Load words file
    words_path = os.path.join(settings.CHATBOT_ROOT, 'words.pkl')
    # Load classes file
    classes_path = os.path.join(settings.CHATBOT_ROOT, 'classes.pkl')

    def __init__(self, eckmo):
        try:
            self.eckmo = eckmo
            self.lemmatizer = WordNetLemmatizer()
            self.model = load_model(self.model_path)
            self.intents = json.loads(open(self.intents_path).read())
            self.words = pickle.load(open(self.words_path, 'rb'))
            self.classes = pickle.load(open(self.classes_path, 'rb'))
        except Exception as e:
            raise e
            logger.exception(f'Error initializing {self.__class__.__name__} cause :{str(e)}')

    def clean_up_sentence(self, sentence):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        # tokenize the pattern - split words into array
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word - create short form for word
        sentence_words = [self.lemmatizer.lemmatize(
            word.lower()) for word in sentence_words]
        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with result : {sentence_words} ')
        return sentence_words

    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

    def bow(self, sentence, words, show_details=True):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        # tokenize the pattern
        sentence_words = self.clean_up_sentence(sentence)
        # bag of words - matrix of N words, vocabulary matrix
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)
        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with result : {np.array(bag)} ')
        return (np.array(bag))

    def predict_class(self, sentence, model):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        # filter out predictions below a threshold
        p = self.bow(sentence, self.words, show_details=False)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})
        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with result : {return_list} ')
        return return_list

    def getResponse(self, ints, intents_json):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = {'response': random.choice(i['responses']), 'command': i['context']}
                logger.info(f'Result "{result}" "')
                break
        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with result : {result} ')
        return result

    def chatbot_response(self, msg):
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')
        ints = self.predict_class(msg, self.model)
        res = self.getResponse(ints, self.intents)
        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with result : {res} ')
        return res
