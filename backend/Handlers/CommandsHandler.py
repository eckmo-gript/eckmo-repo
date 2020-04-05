import importlib
import logging

logger = logging.getLogger(__name__)
import pkgutil
import os
import inspect

from backend.commands.Command import Command


class CommandsHandler:
    """
    The framework that accepts user input and forwards it to the correct command
    """
    COMMAND_DIR = os.path.join('backend', 'commands')

    def __init__(self, eckmo):
        self.eckmo = eckmo
        self.cmd_list = self.get_commands()

    def get_commands(self):
        """
        Find all commands in the command directory and import them. Then return all of them that are subclasses of
        Command in a list
        :return : A list of classes which are subclasses of Command
        """
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')

        for (module_loader, name, ispkg) in pkgutil.iter_modules([self.COMMAND_DIR]):
            importlib.import_module('backend.commands.' + name, __package__)

        logger.info(
            f'Exiting {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class with result {Command.__subclasses__()}')
        return Command.__subclasses__()

    def choose_command(self, command, request):
        """
        Find the best matching command to respond to a request dictionary
        :param request : Dictionary of parameters associated with a user request, such as input_text, date, etc.
        :return: An instantiated command if one recognizes the input text, else None
        """
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')

        cmd = None
        if command:
            cmd = self.get_cmd_from_name(command)

        if cmd:
            cmd = cmd(request=request, eckmo=self.eckmo)
            logger.info(f'Command {cmd} from packages found and instantiated."')
        else:
            logger.info(f'Command {command} not found in packages. "')
        return cmd

    def get_cmd_from_name(self, cmd_name):
        """
        Find the command class that matches a given command name
        :param cmd_name: String name of a command
        :return: A command class
        """
        logger.info(f'Entring {inspect.currentframe().f_code.co_name} function in {self.__class__.__name__} Class')

        for cmd in self.cmd_list:
            if cmd.name == cmd_name:
                return cmd
