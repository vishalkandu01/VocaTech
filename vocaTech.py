import pyttsx3
import datetime
import speechRecognition as sr

 


engine = pyttsx3.init('sapi5') # sapi5 api helps in synthesis and recognition of voice.
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voice[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishme():
    hour = int(datetime.datetime.now().hour)

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
 

if __name__=="__main__" :
    speak("Code With Vishal Kandu")

 