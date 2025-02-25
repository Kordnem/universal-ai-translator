import speech_recognition as sr
import googletrans
from googletrans import Translator
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Sprich jetzt...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language="auto")
        print(f"Erkannter Text: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Sprache konnte nicht erkannt werden")
        return None
    except sr.RequestError:
        print("❌ Fehler bei der Verbindung zum Spracherkennungsdienst")
        return None

def translate_text(text, target_lang="en"):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    print(f"Übersetzung ({target_lang}): {translation.text}")
    return translation.text

def text_to_speech(text, lang="en"):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if lang == "de":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    recognized_text = recognize_speech()
    if recognized_text:
        translated_text = translate_text(recognized_text, target_lang="en")
        text_to_speech(translated_text, lang="en")
