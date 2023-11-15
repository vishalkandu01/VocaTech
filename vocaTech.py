import pyttsx3

engine = pyttsx3.init('sapi5') # sapi5 api helps in synthesis and recognition of voice.
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voice[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

if __name__=="__main__" :
    speak("Code With Vishal Kandu")

 