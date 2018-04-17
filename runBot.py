from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter

from rasa_core.interpreter import RasaNLUInterpreter

import logging


def run_search(serve_forever=True):
    # model_directory = "./model-franken/default/model_20180129-124054/"
    nlu_interpreter = RasaNLUInterpreter("model/default/model_20180415-204746")
    # nlu_interpreter = Interpreter.load(model_directory, RasaNLUConfig("config_spacy.json"))

    agent = Agent.load("models/dialogue", interpreter=nlu_interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    # utils.configure_colored_logging(loglevel="INFO")
    logging.basicConfig(filename="example.log", level="DEBUG")
    run_search()