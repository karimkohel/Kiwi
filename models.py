import pickle


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