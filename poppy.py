from neuralintents import GenericAssistant
from fx import mappings
import speech

assistant = GenericAssistant('intents.json', model_name="test_model", intent_methods=mappings)
assistant.train_model()
assistant.save_model()


while True:

    speech.waitForWakeupCall("hey")
    working = True

    while working:
        message = speech.takeCommand()
        working = assistant.request(message)

    if "exit" in message:
        break
