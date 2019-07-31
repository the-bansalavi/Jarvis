import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init('sapi5') 
voices=engine.getProperty('voices')
#print(voices)
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good Morning!")
    elif(hour>=12 and hour<=18):
        speak("good afternoon")
    else:
        speak("good evening")
        
    speak("I am jarvis sir. please tell me how may i help you")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.eclo()
    server.starttls()
    server.login('myemail@gmail.com','you-password')
    server.sendmail('youemail@gmail.com',to,content)
    server.close()

    
if __name__ == "__main__":
    #speak("harry is a good boy")
    #wishme()
    while True:
        query = takeCommand().lower()


        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "F:\\Songs\\Punjabi"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(1,10)]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is: {strTime}")

        elif "open code" in query:
            code_path="C:\\Users\\Avi Bansal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif "email to harry" in query:
            try:
                speak("what should i say")
                content=takeCommand()
                to = "pbbansal97@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry bhai email not sent")
        

