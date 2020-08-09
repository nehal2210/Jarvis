import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys 
import pyautogui as auto
import calendar
import requests
import bs4
import pandas as pd
import time
from playsound import playsound
import re
import sys


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150) 
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mail', 'password')
    server.sendmail('mail to send', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        
        
        elif 'jira' in  query:
            speak("Zira taking all the commands of your system")
            engine.setProperty('voice', voices[1].id)
            speak("Sir! I am Zira in Your Service")
        
        
        elif 'david' in query:
            speak("David taking all the commands of your system")
            engine.setProperty('voice', voices[0].id)
            speak("Sir! I am David in Your Service")

        elif 'open robot' in query:
            webbrowser.open("www.http://robotacademy.net.au/")
            speak("Openin Peter Cork robotic courses")

        elif 'open coursera' in query:
            webbrowser.open("https://www.coursera.org/")
            speak("Openin Coursera Website")


        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("opening Youtube")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening Google")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")   
            speak("opening stackoverflow")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")   
            speak("opening facebook")

        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")   
            speak("opening whatsupp")
        
        elif 'temperature of a week' in query:
            url='https://www.timeanddate.com/weather/pakistan/karachi/ext'
            res=requests.get(url)
            try:
                res.raise_for_status()
                soup=bs4.BeautifulSoup(res.content,'html.parser')
                table_head=soup.find_all('tr')[1].find_all('th')
                heading=[head.text for head in table_head if head.text!='\xa0'][:6]
                heading.insert(0,'Date')
                table_day=soup.find_all('tbody')[0].find_all('tr')
                # print(heading)
                day=[day.find_all('th')[0].find('span').text for day in table_day]
                date=[date.find_all('th')[0].text for date in table_day]
                temp=[temp.find_all('td')[1].text.replace('\xa0','-') for temp in table_day]
                weather=[weather.find_all('td')[2].text for weather in table_day]
                feels_like=[feel.find_all('td')[3].text.replace('\xa0','') for feel in table_day]
                wind=[win.find_all('td')[4].text for win in table_day]
                humidity=[hum.find_all('td')[6].text for hum in table_day]
                
                weather_data=pd.DataFrame({
                    heading[0]:date,
                    heading[1]:day,
                    heading[2]:temp,
                    heading[3]:weather,
                    heading[4]:feels_like,
                    heading[5]:wind,
                    heading[6]:humidity,
                })
                speak("Karachi Temperature of a week detected")
                print(weather_data)
                time.sleep(10)
            except :
                speak("Unable to detect temperature becuase of Internet")

        
        elif 'temperature of today' in query:
            
            
            url='https://www.timeanddate.com/weather/pakistan/karachi/ext'
            res=requests.get(url)
            try:
                res.raise_for_status()
                soup=bs4.BeautifulSoup(res.content,'html.parser')
                table_day=soup.find_all('tbody')[0].find_all('tr')
                temp=[temp.find_all('td')[1].text.replace('\xa0','-') for temp in table_day][0]
                weather=[weather.find_all('td')[2].text for weather in table_day][0]
                feels_like=[feel.find_all('td')[3].text.replace('\xa0','') for feel in table_day][0]

                speak(f"Karachi Temperature of today {temp} But feels like {feels_like} and the weather is {weather} ")
                 
            except :
                speak("Unable to detect temperature becuase of Internet")

            
            
            
        elif 'play music' in query:
            music_dir = 'E:\\SONGS'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[20]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            datestr=datetime.date.today().strftime("%B %d, %Y")
            speak(f'date of today is {d2}')
            
        elif 'day' in query:
            
            my_date = datetime.date.today()
            day = calendar.day_name[my_date.weekday()]
            speak(f"Today is {day}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to shabz' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gatshabz221097@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Nehal bhai. I am not able to send this email")
                
        elif 'exit' in query:
            speak("Good By Sir!")
#             raise SystemExit("Stop right there!")
            sys.exit(1)

        elif 'fibre' in query:
            speak("Opening Fiver Account")
            webbrowser.open("https://www.fiverr.com/users/nehal_ahmed_dev/seller_dashboard")
        
        elif 'set' in query:
            speak("Setting Timer")            
            position_of_timer=(1406,46)
            position_of_5mint=(1120, 205)
            position_of_start=(1023,91)
            position_of_escape=(805,308)

            auto.click(position_of_timer,duration=1.5)
            auto.click(position_of_5mint,duration=1.5)
            auto.click(position_of_start,duration=1.5)
            auto.click(position_of_escape,duration=1.5)
        elif 'close all' in query:
            speak("Closing all windows")
            try:
                os.system('taskkill /F /IM notepad.exe')
            except Exception(e):
                speak("Unable to close because of "+ str(e))
        elif 'shutdown' in query:
            speak(" Shutting Down  Your Computer")
            os.system('shutdown /s')
            
            
        elif 'restart' in query:
            speak("Restarting  Your Computer")
            os.system('shutdown /r')
            

        elif 'take snapshot' in query :
            speak("Taking Shot")
            src=auto.screenshot()
            
            f= open("snapcounter.txt",'r')
            counter=int(f.read())
            f.close()
            src.save("C:\\Users\\HD\\Desktop\\"+str(counter)+".png")
            f=open("snapcounter.txt",'w')
            counter+=1
            f.write(counter)
            f.close()
        elif 'reset snapshot' in query:
            speak("resetting snapshot to one")
            counter=1
            f=open("snapcounter.txt",'w')
            f.write(counter)
            f.close()
        
        elif 'set counter' in query:
            Speak("Setting Your Timer sir")
            regex=re.compile(r'\d\d')
            reg=re.search(regex,query)
            count=reg.group()
            while count!=0:
                i=60
                while i!=0:
                    time_left=str(count).zfill(2)+":"+str(i).zfill(2)
                    print(time_left+"\r",end='')
                    time.sleep(1)
                    i-=1
                count-=1

            playsound('Wecker-sound.mp3')

            
