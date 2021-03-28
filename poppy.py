from neuralintents import GenericAssistant
from fx import mappings

assistant = GenericAssistant('intents.json', model_name="test_model", intent_methods=mappings)
assistant.train_model()
assistant.save_model()

done = False

while not done:
    message = input("Enter a message: ")
    if message == "exit":
        done = True
    else:
        assistant.request(message)