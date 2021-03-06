from datetime import datetime
import requests
import random
import webbrowser
import re
from time import sleep
import sys
import pickle
import os
import json
import urllib
import threading
import subprocess

import models
import speech
from pytube import YouTube
from bs4 import BeautifulSoup
import docx

try:
    with open("settings.json") as f:
        settings = json.load(f)
except Exception:
    settings = {'speech_speed': 170, 'voice_number': 1, 'music_folder': ''}
    with open('settings.json', 'w') as f:
            json.dump(settings, f)

def getTime(intent):
    time = datetime.now().time()
    time = time.strftime("%I:%M %p")
    time = time.lstrip("0")
    speech.speak(intent + " " + time)

def getWeather(intent):
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=04a716d70b54bf5c6c24dbb3dfa5db03&units=metric'
    try:
        allData = requests.get(api).json()
        weather = allData['weather'][0]['description']
        temp = allData['main']['temp']
        speech.speak(intent + " " + weather + ", with temperatures around " + str(int(temp)) + " degrees")
    except TimeoutError:
        speech.speak("internet connection error occured, try again later")
    except Exception:
        speech.speak("An error occured, try again later")

def takeNotes(intent):
    speech.speak(intent)
    note = speech.takeCommand()
    with open("notes.txt", 'a') as f:
        f.write(note)
        f.write("\n---------------------\n")
    speech.speak("Note added.")

def search(intent):
    speech.speak(intent)
    searchTopic = speech.takeCommand()
    speech.speak("This is what i found for " + searchTopic)
    webbrowser.open("https://www.google.com.tr/search?q={}".format(searchTopic.replace(" ", "+")), new=2)

def close(intent):
    speech.speak(intent)
    return True

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
    for i, reminder in enumerate(reminders):
        speech.speak(f"reminder {i+1} is, " + reminder.text)
        speech.speak("Due, " + reminder.dueDate)

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
        speech.speak("Ok, done")
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

def downloadMusic(intent):
    speech.speak(intent)
    songName = speech.takeCommand()
    confirmed = speech.confirmCommand()

    if confirmed:
        try:
            
            searchLink = 'https://www.youtube.com/results?search_query={}'.format(songName.replace(" ", "+"))
            htmlPage = urllib.request.urlopen(searchLink)
            video_ids = re.findall(r"watch\?v=(\S{11})", htmlPage.read().decode())
            videoLink = "https://www.youtube.com/watch?v=" + video_ids[0]
            
            video = YouTube(videoLink)
            speech.speak("downloading a song called, {}".format(video.title))
            
            audio = video.streams.last()
            if len(settings['music_folder']) < 1:
                musicPath = os.path.expanduser("~/Desktop")
            else:
                musicPath = settings['music_folder']
            
            audio.download(musicPath)

        except TimeoutError:
            speech.speak("sorry something went wrong, probably the internet connection")
        except Exception as e:
            speech.speak("An error occured, try again later : ", e)
        
        speech.speak("Done downloading.")

    else:
        speech.speak("you did not confirm, canceling song request")

def playMusic(intent):
    speech.speak(intent)
    songName = speech.takeCommand()
    speech.speak("ok, on it")
    try:
        searchLink = 'https://www.youtube.com/results?search_query={}'.format(songName.replace(" ", "+"))
        htmlPage = urllib.request.urlopen(searchLink)
        video_ids = re.findall(r"watch\?v=(\S{11})", htmlPage.read().decode())
        videoLink = "https://www.youtube.com/watch?v=" + video_ids[0]
    except TimeoutError:
        speech.speak("internet connection error occured, try again later")
    webbrowser.open(videoLink, new=2)
    return True

    
def changeVoice(intent):
    confirmed = speech.confirmCommand(intent)
    if confirmed:
        settings['voice_number'] = 0 if settings['voice_number'] == 1 else 1 # switch value of voice between 0,1
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
        speech.speak("ok, done switching my voice but change will take effect after restart")
    else:
        speech.speak("you did not confirm, canceling task")

def startWordProject(intent):
    speech.speak(intent)
    docName = speech.takeCommand()
    speech.speak("ok, creating document")
    doc = docx.Document()
    doc.add_paragraph(docName)
    fileName = os.path.expanduser("~/Desktop") + "\\" + docName + ".docx"
    doc.save(fileName)
    os.startfile(fileName)

def prayerTime(intent):
    """ Legacy function """
    try:
        source = requests.get('https://egypt.timesprayer.com/en/prayer-times-in-cairo.html').text
        soup = BeautifulSoup(source, 'lxml')
        prayer_time = soup.find('div',id='countdown').text
        salah = soup.find('div',class_='info mobile').h3.text
    except:
        try:
            source = requests.get('https://www.prayer-times.info/en/egypt/cairo/').text
            soup = BeautifulSoup(source, 'lxml')
            prayer_time = soup.find('div',id='next_pray').text
            salah = soup.find('div',id='next_pray').h3.text
        except:
            source = None
    if source == None:
        speech.speak("sorry cannot find prayer time right now. Maybe try again later")
    else:
        speech.speak(intent + " " + prayer_time)

    

mappings = {
    'time' : getTime,
    'weather' : getWeather,
    'note' : takeNotes,
    'search' : search,
    'sleep': takeBreak,
    'setreminders' : setReminder,
    'readreminders' : readReminders,
    'clearreminders' : clearReminders,
    'playmusic' : playMusic,
    'downloadmusic' : downloadMusic,
    'voicechange' : changeVoice,
    'startword': startWordProject,
    'prayer': prayerTime,
    'goodbye': close
}
