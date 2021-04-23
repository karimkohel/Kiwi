import pickle


class Reminder():
    def __init__(self, text, dueDate):
        self.text = text
        self.dueDate = dueDate

    @staticmethod
    def readReminders(file = "reminder.p"):
        try:
            reminders = pickle.load(open(file, 'rb'))
        except FileNotFoundError:
            reminders = []
        return reminders

    @staticmethod
    def writeReminders(reminders, file = 'reminder.p'):
        pickle.dump(reminders, open(file, 'wb'))


class note():
    def __init__(self, text):
        self.note = text


    @staticmethod
    def readReminders():
        return pickle.load(open("reminder.p", 'rb'))

    @staticmethod
    def writeReminders(reminders):
        pickle.dump(reminders, open('reminder.p', 'wb'))