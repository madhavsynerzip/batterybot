from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)

def train_dialogue(domain_file="data/domain.yml",
                   training_data_file='data/stories.md',
                   model_dir="./models/dialogue"):

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()])

    agent.train(training_data_file,
                max_history = 3,
                epochs = 300)
    agent.persist(model_dir)
    return agent


if __name__ == '__main__':
    train_dialogue()