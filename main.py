import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("initializing Black")

MASTER = "io"

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#speak
def speak (text):
    engine.say(text)
    engine.runAndWait()

#function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning " + MASTER)
    elif 12 <= hour < 18:
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)
        speak(" ")

#microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us",)
        print(f"user_said: {query}\n")
    
    except Exception as e:
        print("please repeat again")
        query = None
    return query


#mainprogram
speak ("Hello my name is Black, i can help you")
wishMe()
query = takeCommand()

#logic
if "wikipedia" in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia", "")  # Menghapus kata "wikipedia" dari query
    query = query.strip()  # Menghapus spasi ekstra
    try:
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        # Jika terdapat banyak kemungkinan hasil, Anda dapat menangani disambiguasi di sini
        print("Wikipedia disambiguation found. Please be more specific.")
        speak("Wikipedia disambiguation found. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        # Jika halaman tidak ditemukan
        print(f"Page not found: {query}")
        speak(f"Page not found: {query}")
    except Exception as e:
        print("An error occurred while searching Wikipedia.")
        speak("An error occurred while searching Wikipedia.")

elif "open youtube" in query.lower():
    url = "youtube.com"
    chrome_path = "R:/chrome-win/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif "open google" in query.lower():
    url = "google.com"
    chrome_path = "R:/chrome-win/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

