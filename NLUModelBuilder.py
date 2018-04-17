from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer


class NLUModelBuilder:

    def build_model(self, path):
        #training_data = load_data('data/batteryBoss_train.json')
        training_data = load_data(path)
        trainer = Trainer(RasaNLUConfig("config/config_spacy.json"))
        trainer.train(training_data)
        model_directory = trainer.persist('./model/')
        return model_directory


    def test_model(self, utterance):
        model_directory = './model/default/model_20180319-154224'
        from rasa_nlu.model import Interpreter
        interpreter = Interpreter.load(model_directory,
                                       RasaNLUConfig("train/config_spacy.json"))

        interpreter.parse(utterance)


path = input('Enter Training File Path::>')
print ("Path Provided : " + path)

if path != "":
    nlu_builder = NLUModelBuilder()
    model_dir = nlu_builder.build_model(path)
else:
    model_dir = "./model/default/model_20180412-183805"

#model_dir = "./model/default/model_20180411-174546"
print("Saved Model : "+ model_dir)

from rasa_nlu.model import Interpreter
interpreter = Interpreter.load(model_dir,RasaNLUConfig("config/config_spacy.json"))

print("Loaded Model; Enter Utterance")

while True:
        x=input('::>')
        output=interpreter.parse(x)
        print(output.get('intent'))
        print(output.get('entities'))