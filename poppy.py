from neuralintents import GenericAssistant
from fx import mappings
import speech

assistant = GenericAssistant('intents.json', model_name="test_model", intent_methods=mappings)
assistant.train_model()
assistant.save_model()


speech.speak("Hello, how can i help")
while True:
    message = speech.takeCommand()
    assistant.request(message)