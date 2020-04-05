import logging
logger = logging.getLogger(__name__)
from abc import abstractmethod
from backend.Utilities.RequireAttributes import require_attributes


class Command(metaclass=require_attributes("name")):
    """
    A recognized command accepted by the voithos with a defined response.
    recognized_keywords and help_description must be implemented in all subclasses.
    """
    name = None

    def __init__(self, request, eckmo):
        self.eckmo = eckmo
        self.request = request

    @property
    def user_input(self):
        return self.request

    @abstractmethod
    def respond(self):
        return

    @classmethod
    def help(cls):
        """
        Print the name of the command and the help description for it
        """
        return f'<b>{cls.name}</b>: {cls.help_description}'