import pyttsx3
import speech_recognition as sr
import webbrowser  
import datetime  
import wikipedia
import os
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 1
        audio = r.listen(source)
         
        try:
            print("Recognizing")
   
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
             
        except Exception as e:
            print(e)
            print("excuse me sir , say that again")
            return "None"
         
        return Query
def speak(audio):
     
    engine = pyttsx3.init()
   
    voices = engine.getProperty('voices')
     
   
    engine.setProperty('voice', voices[0].id)
     
   
    engine.say(audio)  
     
   
    engine.runAndWait()
def wishMe():
    hour = datetime.datetime.now().hour
    if hour>0 and hour<=12:
        speak("good morning buddy")
        print("good morning buddy".center(150))
    elif hour>12 and hour<18:
        speak("good afternoon buddy")
        print("good afternoon buddy".center(150))
    else:
        speak("good evening buddy")
        print("good evening buddy".center(150))
   

def Hello():
    speak("hey buddy, i am your virtual secretary Dora ")
    print("hey buddy, i am your virtual secretary Dora".center(150))
    speak("tell me how i can help you...?")
    print("tell me how i can help you...?".center(150))
def Take_query():
    wishMe()
    Hello()
   
    while(True):
       
        query = takeCommand().lower()
        if "open google" in query:
            pyttsx3.speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
             
        elif "open notepad" in query:
            pyttsx3.speak("opening notepad")
            os.system("notepad")
            continue
         
        elif "open linkedin" in query:
            pyttsx3.speak("open linkedin")
            webbrowser.open("www.linkedin.com")
            continue
         
        elif "open youtube" in query:
            pyttsx3.speak("open youtube")
            webbrowser.open("www.youtube.com")
            continue
           
        elif "open hackerrank" in query:
            pyttsx3.speak("open hackerrank")
            webbrowser.open("www.hackerrank.com")
            continue
           
        elif "wikipedia" in query:
            pyttsx3.speak("open wikipedia")
            webbrowser.open("www.wikipedia.org")
            continue
           
        elif "open calculator" in query:
            pyttsx3.speak("opening calculator")
            os.system("start calculator:")
            continue
           
           
        elif "twitter" in query:
            pyttsx3.speak("opening twitter")
            os.system(" www.twitter.com")
            continue
           
        elif "facebook" in query:
            pyttsx3.speak("opening facebook")
            webbrowser.open(" www.facebook.com")
            continue
           
        elif "amazon" in query:
            pyttsx3.speak("opening amazon")
            webbrowser.open(" www.amazon.in")
            continue
           
        elif "flipkart" in query:
            speak("opening flipkart")
            webbrowser.open(" www.flipkart.com")
            continue
           
        
        elif "dora" in query:
            speak("yes connection i can help u with are")
            print()
            print("Programs i can help u with are:-".center(125))
            speak("such as window based commands")
            print()
            print(" Window Based Commands".center(125))
            speak("Entertainment")
            print()
            print("Entertainment".center(125))
            speak("Public clouds")
            print()
            print("Public Clouds".center(125))
            speak("emails")
            print()
            print("Emails".center(125))
            speak("Social media")
            print()
            print("Social Media".center(125))
            speak("Shopping")
            print()
            print("Shopping".center(125))
            continue
           
        elif "bye" in query:
            pyttsx3.speak("Bye. Check Out me at any time")
            print("Bye. Check Out me at any time".center(150))
            exit()
         
       
         
        

if _name_ == '_main_':
      Take_query()