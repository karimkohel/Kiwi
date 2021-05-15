from neuralintents import GenericAssistant
from fx import mappings
import speech
from tkinter import *
from PIL import ImageTk,Image
import threading, sys


assistant = GenericAssistant('intents.json', model_name="model", intent_methods=mappings)
assistant.train_model()
assistant.save_model()
# assistant.load_model()


def mainLoop(app):

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
    app.destroy()

root = Tk()
root.title('Kiwi')
root.iconbitmap('icon.ico')
root.resizable(False, False)
my_img1 = ImageTk.PhotoImage(Image.open("kiwi.jpg"))
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


proc = threading.Thread(target=mainLoop, args=(root,))
proc.daemon = True
proc.start()

root.mainloop()
sys.exit(0)