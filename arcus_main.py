import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import os
import random
import requests #pip install requests
from requests import get
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import smtplib #pip install secure-smtplib
import sys
import cv2
from bs4 import BeautifulSoup
import time
import pyautogui #pip install puautogui
import geocoder #pip install geocoder
import operator
import pyjokes #pip install pyjokes
import phonenumbers #pip install phonenumbers

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 5
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("")
        return "none"
    return query

# to wish

def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a73b0e9fb9f442ecaf1bb286ed4b05ca"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"Today's {day[i]} news is: {head[i]}")

def creat_file(filename):
    try:
        with open(filename, 'x') as f:
            speak(f"File name {filename} created successfully!")
    except FileExistsError:
        speak(f"File names {filename} already exists!")
    except Exception as e:
        speak("Error while creating a file")

def view_all_files(filename):
    files = os.listdir()
    if not files:
        speak("No file found!")
    else:
        speak("Files in directory!")
        for file in files:
            speak(file)

def delet_file(filename):
    try:
        os.remove(filename)
        speak(f"Filename {filename} has been deleted successfully!")
    except FileExistsError:
        speak("File not found")
    except Exception:
        speak("Error, can't creat file")

def wish():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
    strime = datetime.datetime.now().strftime("%d/%m/%Y")
    if hour >= 0 and hour < 12:
        speak(f"good morning sir, its {strTime}")
    elif hour >= 12 and hour < 18:
        speak(f"good afternoon sir, its {strTime}")
    else:
        speak(f"good evening sir, its {strTime}")
    speak("i am jaarvis . please tell me how can i help you")

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('charanpratibha3799@gmail.com','SINGH2008')
    server.sendmail('charanpratibha3799@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        # building logics to perform tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("Closing notepad...")
            os.system("taskkill /f /im notepad.exe")

        elif "who are you" in query:
            speak("Allow me to introduce myself. I am jaarvis. the virtual artificial intelligence. I'am here to assist you with a variety of tasks . as best I can 24 hours a day. 7 days a week . importing all preferences from hub interface .your system is about fully operational pleas tell me how can i help you...")

        elif "open vscode" in query:
            apath = "C:\\Users\\PRATIBHA SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(apath)
        elif "open microsoft edge" in query:
            epath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(epath)
        elif "close microsoft edge" in query:
            speak("Closing microsoft edge...")
            os.system("taskkill /f /im msedge.exe")
        elif "open command prompt" in query:
            zpath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(zpath)

        elif "close vscode" in query:
            speak("closing visual studio code...")
            os.system("taskkill /f /im code.exe")

        elif "ok jarvis play a music for me" in query:
            music_dir = "D:\\Songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))

        elif "close command prompt" in query:
            speak("Closing command prompt...")
            os.system("taskkill /f /im cmd.exe")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "wikipedia" in query:
            speak("searching to wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "play youtube shorts" in query:
            urls = [
                "https://www.youtube.com/shorts/"
            ]
            random_url = random.choice(urls)
            webbrowser.open(random_url)
            if "next" in query:
                pyautogui.press('down')

        elif "open python package manager" in query:
            webbrowser.open("pypi.org")

        elif "open physics wala"in query:
            webbrowser.open("https://www.pw.live/study/batches/study")

        elif "open my github repository" in query:
            webbrowser.open("https://github.com/Harsh-cpu113/Arcus")

        elif "next" in query:
            pyautogui.press('right')

        elif "open github" in query:
            webbrowser.open("github.com")

        elif "open python" in query:
            webbrowser.open("www.python.org")

        elif "tell me a joke" in query:
            my_jokes = pyjokes.get_joke(language="en", category="neutral")
            speak(my_jokes)
            
        elif "open app developer" in query:
            speak("Opening android studio...")
            andpath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(andpath)

        elif "close app developer" in query:
            speak("Closing android studio...")
            os.system("taskkill /f /im studio64.exe")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com/")

        elif "open kali" in query:
            webbrowser.open("www.kali.org")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open my website" in query:
            webbrowser.open("D:\webdev\HyDrex\index.html")

        elif "what's my location" in query:
            location = geocoder.ip('me')
            speak(f"Our location is {location.city},{location.state},{location.country}")
            print(f"Latitude : {location.latlng[0]}")
            print(f"Longitude : {location.latlng[1]}")

        elif "search google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open chrome" in query:
            speak("Opening chrome browser...")
            mpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(mpath)

        elif "close chrome" in query:
            speak("Closing chrome...")
            os.system("taskkill /f /im chrome.exe")
        
        elif "open hacker console" in query:
            speak("Opening metasploit framework...")
            slpatth = "C:\\metasploit\\console.bat"
            os.startfile(slpatth)

        elif "close hacker console" in query:
            speak("Cloasing metasploit framework...")
            os.system("taskkill /f /im console.bat")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"Time is : {strTime}")
            if strTime >= "7:15:00 AM":
                speak("Hurry up! sir you have to reach to stop at 7:30 A.M")
            elif strTime == "11:00:00 PM":
                speak("GO to sleep sir")
        elif "send email to sister" in query:
            try:
                speak("What should I say...")
                content = takecommand().lower()
                speak("Sending email to didi...")
                to = "charanpratibha3799@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to didi successfully")
            except Exception as e:
                print(e)
                speak("Sorry sir, cant sent email to didi")

        elif "what is date today" in query:
            strime = datetime.datetime.now().strftime("%d/%m/%Y")
            speak(f"The day is : {strime}")
            if strime == 15/8/2024:
                speak("Happy indepentence day sir")
            elif strime == 26/1/2025:
                speak("Happy republic day sir")
            elif strime == 14/10/2025:
                speak("Happy birthday day sir")

        elif "go to python" in query:
            os.chdir('D:\Python')
            speak("you are in python directory")
        elif f"creat a folder names friday" in query:
                speak(f"making friday...")
                os.mkdir('D:\Python')
        elif "show me all files" in query:
                speak("listing all files or folders...")
                speak(os.listdir('D:\Python'))
        elif "what is my present working directory" in query:
            speak(os.getcwd())
        elif "temprature" in query:
            search = "Temprature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe")
            speak(f"current {search} is {temp}")

        elif "on bakelite" in query:
            speak("Turning on bakelites...")
            pyautogui.hotkey('fn', 'space')

        elif "off bakelite" in query:
            speak("Turning off bakelites...")
            pyautogui.hotkey('fn', 'space')

        elif "open designer" in query:
            speak("Opening QT designer...")
            opath = "C:\\Program Files (x86)\\Qt Designer\\designer.exe"
            os.startfile(opath)

        elif "select all" in query:
            pyautogui.hotkey('Ctrl', 'A')

        elif "copy text" in query:
            pyautogui.hotkey('Ctrl', 'C')

        elif "paste here" in query:
            pyautogui.hotkey('Ctrl', 'V')

        elif "back" in query:
            pyautogui.press('backspace')
        elif "find" in query:
            pyautogui.hotkey('Clrl', 'F')
        elif "back all" in query:
            pyautogui.hotkey('Ctrl', 'backspace')
        elif "execute" in query:
            pyautogui.hotkey('Ctrl', 'right')
        elif "cut" in query:
            pyautogui.hotkey('Ctrl', 'X')
        elif "open play store" in query:
            aslpath = "C:\\Program Files\\Google\\Play Games\\Bootstrapper.exe"
            os.startfile(aslpath)
        elif "close play store" in query:
            speak("Closing Google play games beta...")
            os.system("taskkill /f /im Bootstrapper.exe")
        elif "save it" in query:
            pyautogui.hotkey('Ctrl', 'S')

        elif "call chacha" in query:
            speak("Calling Chacha ji...")
            phone_number = "+918887990722"
            os.system(f"start tel:{phone_number}")

        elif "switch the window" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif "tell me today's news" in query:
            speak("Pleas wait sir, fetching the latest news")
            news()

        elif "deactivate jarvis" in query:
            speak("Ok mister stark, you can call me any time")
            speak("Deactivating jarvis...")
            sys.exit()
        elif "ok jarvis you can sleep now" in query:
            speak("Ok mister stark, you can call me any time")
            speak("Deactivating jarvis...")
            sys.exit()




                
