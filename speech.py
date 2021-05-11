import speech_recognition as sr
import pyttsx3 as tts
import json
import random

try:
    with open("settings.json") as f:
        settings = json.load(f)
except Exception:
    settings = {'speech_speed': 170, 'voice_number': 1, 'music_folder': ''}
    with open('settings.json', 'w') as f:
            json.dump(settings, f)


speaker = tts.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[settings['voice_number']].id)
speaker.setProperty('rate', settings["speech_speed"])

errorCommands = ["can't take commands with no internet", "i literally can't understand you, there is not internet", "no internet so i can't help you can i", "internet connection error"]

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def takeCommand():
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                return text
        except sr.UnknownValueError:
            speak("Sorry I couldn't get that, can you try again?")
        except Exception as e:
            speak(random.choice(errorCommands))


def waitForWakeupCall(text):

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                audio = recognizer.recognize_google(audio)
                audio = audio.lower()

                if audio.find(text) >= 0:
                    speak("hey nada")
                    break
                else:
                    continue

        except sr.UnknownValueError:
            continue
        except Exception as e:
            speak(random.choice(errorCommands))

def confirmCommand(text = "are you sure you want to confirm your last command"):
    speak(text)
    confirmation = takeCommand()
    if confirmation.find("yes") >= 0:
        return True
    else:
        return False
