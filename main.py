import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from google import genai
from gtts import gTTS
import pygame
import os


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = genai.Client(api_key="AIzaSyA2K1lJjPQNdEv9XfpJd3bHPoGJTgovKhg")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=command,
        config={
            "system_instruction": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"
        }
    )

    return response.text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open Ai Mode" in c.lower():
        webbrowser.open("https://www.google.com/search?q=&sxsrf=AE3TifO_--urXo1h1ySmUmWa4fMM0zW8Xw%3A1761411763567&aep=22&udm=50&oq=")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open " in c.lower():
        webbrowser.open("")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = Music_Library.music[song]
        webbrowser.open(link)

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    r = sr.Recognizer() # Initialize once outside the loop
    while True:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source) # Helps with accuracy
                    print("Listening for wake word...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=3)
                    word = r.recognize_google(audio)
                    
                    if word.lower() == "jarvis":
                        speak("Yes Sir?")
                        with sr.Microphone() as source:
                            print("Jarvis Active...")
                            audio = r.listen(source)
                            command = r.recognize_google(audio)
                            processCommand(command)
            except sr.WaitTimeoutError:
                pass # Just restart the loop if no speech is detected
            except Exception as e:
                print(f"Error: {e}")