import speech_recognition as sr
import webbrowser
import pyttsx3
import Music_Library
import requests
# from openai import OpenAI
# import pygame
from gtts import gTTS
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 


def speak(text):
    engine.say(text)
    engine.runAndWait()



# def aiProcess(command):
#     client = OpenAI(api_key="<Your Key Here>",
#     )

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]
#     )

#     return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open AI Mode" in c.lower():
        webbrowser.open("https://www.google.com/search?q=&sxsrf=AE3TifO_--urXo1h1ySmUmWa4fMM0zW8Xw%3A1761411763567&aep=22&udm=50&oq=")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = Music_Library.music[song]
        webbrowser.open(link)






if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Sir?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))