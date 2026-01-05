import speech_recognition as sr
import pyttsx3
import config

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    if config.VOICE_ENABLED:
        print(f'{config.NAME}:', text)
        engine.say(text)
        engine.runAndWait()
    else:
        print(f'{config.NAME}:', text)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, 0.5)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ''
    except sr.RequestError:
        speak("Speech recognition service unavailable.")
        return ''
