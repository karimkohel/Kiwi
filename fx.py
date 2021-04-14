from datetime import datetime
import requests
import random

import speech

def getTime():
    time = datetime.now().time()
    time = time.strftime("%I:%M %p")
    speech.speak("It's " + time)

def getWeather():
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=04a716d70b54bf5c6c24dbb3dfa5db03&units=metric'
    allData = requests.get(api).json()
    weather = allData['weather'][0]['description']
    temp = allData['main']['temp']
    speech.speak(weather, ", ", temp)

def takeNotes():
    speech.speak("Ready to take your notes")
    note = speech.takeCommand()
    with open("note.txt", 'a') as f:
        f.write(note)
        f.write("\n---------------------\n")
    speech.speak("Ok done")

def goodbye():
    l = ["Bye", "Au revoir", "Hope to see you soon", "Talk later", "Ok Goodbye!", "Goodbye then", "Ok I'll go now", "see you later"]
    speech.speak(random.choice(l))
    exit(0)


mappings = {
    'time' : getTime,
    'weather' : getWeather,
    'note' : takeNotes,
    'goodbye': goodbye
}