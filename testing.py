import speech_recognition
import pyttsx3


while True:

    recognizer = speech_recognition.Recognizer();

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(text)

    except speech_recognition.UnknownValueError:
        print("Couldn't get that can you try again.")
