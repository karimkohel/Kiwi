import speech_recognition as sr
import pyttsx3 as tts

settings = {
    "speech_speed": 170,
}

def speak(text):
    speaker = tts.init()
    speaker.setProperty('rate', settings["speech_speed"])
    speaker.say(text)
    speaker.runAndWait()

def takeCommand():
    done = False
    recognizer = sr.Recognizer();

    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                return text
        except sr.UnknownValueError:
            speak("Couldn't get that, can you try again?")
        except Exception:
            print("error in take command")
            exit(1)
