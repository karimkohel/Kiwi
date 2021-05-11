from neuralintents import GenericAssistant
from fx import mappings
import speech

assistant = GenericAssistant('intents.json', model_name="test_model", intent_methods=mappings)
assistant.train_model()
assistant.save_model()
# assistant.load_model()


while True:

    speech.waitForWakeupCall("hey")
    working = True
    counter = 0

    while working:
        counter += 1
        message = speech.takeCommand()

        if counter > 5:
            message = "enough work for today"
            working = assistant.request(message)
            break
        else:
            working = assistant.request(message)

    if "exit" in message:
        break

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Kiwi')
root.iconbitmap('icon.ico')


my_img1 = ImageTk.PhotoImage(Image.open("kiwi.jpg"))


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

root.mainloop()