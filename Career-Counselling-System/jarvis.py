import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour >=12 and hour<17:
        speak("Good afternoon sir")
    elif hour >= 17 and hour <20:
        speak("Good evening sir")
    else:
        speak("Hi sir. Hope u will enjoy ur night") 

    speak("I am Chatbot. Please tell me how may i help you")           
    
def takeCommand():
    #it takes microphone input from user and returns string output    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n") 
        takeCommand()

    except Exception as e:
        #print(e)
        print("Say that again plzz...")       
        return "None"
    
    return query
if __name__=="__main__":
    wishMe()

    
    query = takeCommand().lower()

    if 'wikipedia' in query:
          speak("Searching wikipedia")
          query = query.replace('wikipedia', '')
          results = wikipedia.summary(query, sentences=2)
          speak('According to wikipedia')
          print(results)
          speak(results)
          takeCommand()

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        takeCommand()
    elif 'open movies' in query:
        webbrowser.open("123gofmovies.com")
        takeCommand()
    elif 'open google' in query:
        speak("Sir, what should i search on google for you")
        ac = takeCommand().lower()
        webbrowser.open(f"{ac}")    
        takeCommand() 

    elif 'play music' in query:
        webbrowser.open("https://wynk.in/music/playlist/weekly-top-20-english/bb_1527140401220")     
        takeCommand()      
    
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Ameya Sir the time is {strTime}")
        takeCommand()

    elif 'open game' in query:
          codepath = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
          os.startfile(codepath)
          takeCommand()
    elif 'thank you' in query:
        speak("your most Welcome sir")  
        takeCommand()
 
    elif 'I love you' in query:
        print("I love you too")
        speak("I love you sir") 
        takeCommand()

    elif 'will you marry me' in query:
        print("sorry. i am an AI created by Ameya Chaudhary. i can't marry you")
        speak("sorry. i am an AI created by Ameya Chaudhary. i can't marry you") 
        takeCommand()

    elif 'i hate you' in query:
        print("I don't care")
        speak("I don't care")     
        takeCommand()

    else:
        takeCommand()      
