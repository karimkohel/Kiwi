import speech_recognition as sr
import pyttsx3 as tts

settings = {
    "speech_speed": 170,
    "voice_number" : 1
}

speaker = tts.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[settings['voice_number']].id)
speaker.setProperty('rate', settings["speech_speed"])

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
        except Exception:
            print("error in take command")
            exit(1)


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
        except Exception:
            print("error in wait wake up call")
            exit(1)