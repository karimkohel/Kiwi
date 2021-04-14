from neuralintents import GenericAssistant
from fx import mappings
import speech

assistant = GenericAssistant('intents.json', model_name="test_model", intent_methods=mappings)
assistant.train_model()
assistant.save_model()

done = False

speech.speak("Hello, how can i help")
while not done:
    message = speech.takeCommand()
    if message == "exit":
        speech.speak("Ok, goodbye!")
        done = True
    else:
        assistant.request(message)