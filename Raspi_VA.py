import subprocess
from subprocess import call
import wolframalpha
import tkinter
import random
import vlc
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import math
import os
from gtts import gTTS
import sounddevice as sd
from scipy.io.wavfile import write
import pytz
import smtplib
import sys
import re
import ctypes
from pygame import mixer
import time
from time import strftime
import requests, json
import shutil
from bs4 import BeautifulSoup
from urllib.request import urlopen



def speak(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()



def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")

    else:
        speak("Good evening")

    time.sleep(3)
    speak("How may I help you?")
    time.sleep(3)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        time.sleep(4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to recognizing your voice...")
        return "None"
    return query

    


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any command before execution of this python file 
    clear()
    greeting()

    while True:
        query = take_command().lower()

        # All the commands said by user will be stored in 'query' and
        # converted to lower case for easy recognition of command
        
        if 'what time is it' in query or 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {strTime}")
            print(strTime)

        if "what is today's date" in query:
            date = datetime.datetime.now().strftime('%m/%d/%Y')
            speak(f"Today's date is {date}")
            print(date)
            
        if 'how are you' in query:
            speak("I am fine, Thank you")
            time.sleep(3)
            speak("How are you?")
            time.sleep(3)

        if 'good' in query or "I'm well" in query:
            speak("It's good to know that your fine")
            time.sleep(3)

        if "who made you" in query or "who created you" in query:
             speak("I have been created by you")

        if "who am i" in query:
            speak("If you talk then definitely your human.")


        if "who are you" in query:
            speak("I am your virtual assistant")

        if 'reason for being' in query:
            speak("I was created as a helping tool")

        if 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia (.+)', query)
            #use the “wikipedia.set_lang()” function: fr for French, es for Spanish, zh for Chinese, de for german
            #wikipedia.set_lang("es")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if "calculate" in query:
            app_id = #"Your app id"
            client = wolframalpha.Client(app_id)
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        if "make a note" in query or "take a note" in query:
            speak("What would you like me to write?")
            time.sleep(2)
            note = take_command()
            f = open("new.txt", "w")
            speak("Should i include date and time")
            time.sleep(2)
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S')
                f.write(strTime)
                f.write(" :- ")
                f.write(note)
                f.close()
            speak("It has been noted")

        if "show note" in query:
            speak("Showing note")
            f = open("new.txt", "r")
            print(f.read())
            speak(f.readline())

        if "add to the note" in query:
            speak("What would you like me to add?")
            time.sleep(3)
            note = take_command()
            f = open("new.txt", "a")
            speak("Should i include date and time")
            time.sleep(2)
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S')
                f.write("\n")
                f.write(strTime)
                f.write(" :- ")
                f.write(note)
                f.close()
            speak("It has been noted")


        if "search" in query:
            speak("What would you like to search for?")
            search = take_command()
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            print("Here is what I found for " + search)
            speak("Here is what I found for " + search)
            time.sleep(5)

        if "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("In google maps, here is the location of...")
            time.sleep(3)
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        if 'from youtube play' in query:
            query = query.replace("from youtube play", "")
            video = query
            speak("Here you go to Youtube")
            webbrowser.open("https://www.youtube.com/results?search_query=" + video.replace(' ', '+'))
            time.sleep(5)

        elif 'open google in browser' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.google.com/")

        elif 'open presearch in browser' in query:
            speak("Here you go to Presearch\n")
            webbrowser.open("https://www.presearch.org/")

        elif 'open stackoverflow in browser' in query:
            speak("Here you go to Stack Over flow.Happy coding\n")
            webbrowser.open("https://stackoverflow.com/")

        elif 'open github in browser' in query:
            speak("Here you go to Github\n")
            webbrowser.open("https://github.com/")

        if 'play music in vlc' in query or "play song in vlc" in query:
            speak("Playing music from your folder collection")
            player = vlc.MediaPlayer()
            music = vlc.Media("/home/pi/Desktop/Virtual Assistant/Music/")
            player.set_media(music)
            player.play()
            print(music)
        elif 'pause music' in query:
            player.pause()
        elif 'continue song' in query:
            player.play()
        elif 'next song' in query:
            player.next()
        elif 'previous song' in query:
            player.previous()

        if 'play a movie in vlc' in query:
            speak("Playing a movie from your folder collection")
            media_player = vlc.MediaPlayer()
            media = vlc.Media("/home/pi/Desktop/Master/Media/Video/MKV Video/9 (Nine) 2009.mpg")
            media_player.set_media(media)
            media_player.play()
            time.sleep(5)
        elif 'pause movie' in query:
            media_player.pause()
        elif 'continue movie' in query:
            media_player.play()
        elif 'stop movie' in query:
            media_player.stop()


        if "shutdown computer" in query:
            speak("Make sure all the applications are saved and closed before I take close")
            time.sleep(10)
            speak("Your system is shutting down")
            call("sudo shutdown -h now", shell=True)

        if "restart the computer" in query:
            speak("I will restart in 10 seconds")
            time.sleep(5)
            speak("Ready?")
            snfm = take_command()
            if 'yes' in snfm:
                print("Restarting  the computer")
                speak("Restarting the computer")
                call("sudo reboot -h now", shell=True)
            if "no" in snfm:
                print("Do you have any other requests")
                speak("May I help you with anything else?")

        elif 'exit' in query:
            speak("Thank you for your time")
            exit()
            


time.sleep(2)
speak("How may I help you?")
listening = True
while listening == True:
    query = take_command()
    speak = query()

    

# elif "" in query:
# Command goes here
# For adding more commands

