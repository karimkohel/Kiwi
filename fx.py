from datetime import datetime
import requests
import random
import webbrowser
import re
from time import sleep
import sys
import pickle
import os

import models
import speech

def getTime(intent):
    time = datetime.now().time()
    time = time.strftime("%I:%M %p")
    time = time.lstrip("0")
    speech.speak(intent + " " + time)

def getWeather(intent):
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=04a716d70b54bf5c6c24dbb3dfa5db03&units=metric'
    allData = requests.get(api).json()
    weather = allData['weather'][0]['description']
    temp = allData['main']['temp']
    speech.speak(intent + " " + weather + ", with temperatures around " + str(int(temp)) + " degrees")

def takeNotes(intent):
    speech.speak(intent)
    note = speech.takeCommand()
    with open("notes.txt", 'a') as f:
        f.write(note)
        f.write("\n---------------------\n")
    speech.speak("Ok I added your new note to the notes file")

def search(intent):
    speech.speak(intent)
    searchTopic = speech.takeCommand()
    speech.speak("This is what i found for " + searchTopic)
    webbrowser.open("https://www.google.com.tr/search?q={}".format(searchTopic), new=2)

def close(intent):
    speech.speak(intent)
    sys.exit(0)

def takeBreak(intent):
    speech.speak(intent)
    minutes = speech.takeCommand()
    minutes = re.findall(r'\d+', minutes)
    if minutes:
        speech.speak("ok sleeping for " + minutes[0] + "minutes")
        sleep(int(minutes[0])*60)
        speech.speak("hi, I'm back")
    else:
        speech.speak("Sorry didnt catch that, canceling command")

def readReminders(intent):
    speech.speak(intent)
    reminders = models.Reminder.readReminders("reminder.p")
    for reminder in reminders:
        speech.speak(reminder.text)
        speech.speak(reminder.dueDate)

def setReminder(intent):
    reminders = models.Reminder.readReminders("reminder.p")
    speech.speak(intent)
    text = speech.takeCommand()
    speech.speak("when is this reminder due")
    dueDate = speech.takeCommand()
    reminder = models.Reminder(text, dueDate)
    speech.speak("Reminder set for " + reminder.dueDate)
    if speech.confirmCommand():
        reminders.append(reminder)
        models.Reminder.writeReminders(reminders, "reminder.p")
    else:
        speech.speak("You didn't confirm, canceling command")


def clearReminders(intent):
    speech.speak(intent)
    confirmed = speech.confirmCommand()

    if confirmed:
        if os.path.exists("reminder.p"):
            os.remove("reminder.p")
            speech.speak("ok, cleared all your reminders")
        else:
            speech.speak("you have no reminders")
    else:
        speech("you did not confirm, canceling task")


mappings = {
    'time' : getTime,
    'weather' : getWeather,
    'note' : takeNotes,
    'search' : search,
    'sleep': takeBreak,
    'setreminders' : setReminder,
    'goodbye': close
}
