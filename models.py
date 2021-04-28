import pickle
import os
import random
from playsound import playsound

class Reminder():
    def __init__(self, text, dueDate):
        self.text = text
        self.dueDate = dueDate

    @staticmethod
    def readReminders(file = "reminder.pkl"):
        try:
            reminders = pickle.load(open(file, 'rb'))
        except FileNotFoundError:
            reminders = []
        return reminders

    @staticmethod
    def writeReminders(reminders, file = 'reminder.pkl'):
        pickle.dump(reminders, open(file, 'wb'))


class Note():
    def __init__(self, text):
        self.note = text

    @staticmethod
    def readNotes(file = "notes.pkl"):
        try:
            notes = pickle.load(open(file, 'rb'))
        except FileNotFoundError:
            notes = []
        return notes

    @staticmethod
    def writeNotes(notes, file = 'notes.pkl'):
        pickle.dump(notes, open(file, 'wb'))

class Music():

    def __init__(self, folderPath):
        self.folderPath = folderPath
        self.musicFiles = None

    def checkFolder(self):
        return os.path.exists(self.folderPath)
    
    def checkMusicExists(self):

        files = os.listdir(self.folderPath)

        if len(files) < 1:
            return False
        elif not any("mp3" in element for element in files):
            return False
        else:
            self.musicFiles = files
            return True

    def shuffleMusic(self):
        file = ""
        while not ("mp3" in file):
            file = self.musicFiles[random.randint(0, len(self.musicFiles))]
        
        if len(file) > 4: # min size of music file name
            playsound(self.folderPath + file, False)
            return True
        else:
            return False
