import pyttsx
import time
import os
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-50)
engine.say('Hello aswin what can I do for you')
engine.runAndWait()

with sr.Microphone() as source:
            audio = r.listen(source)

try:
    
    command = r.recognize_google(audio)
    print command
    if('VLC' in command):
        engine.say("command recieved",command)
        time.sleep(1)
        os.system("vlc")
    elif('terminal' in command):
        engine.say("command recived",command)
        time.sleep(1)
        os.system("xfce4-terminal")
    elif('Facebook' in command):
        engine.say("command recived",command)
        time.sleep(1)
        os.system("iceweasel facebook.com")
    elif('YouTube' in command):
        engine.say("command recived",command)
        time.sleep(1)
        os.system("iceweasel youtube.com")
    elif('power off' in command):
        engine.say("command recived")
        time.sleep(1)
        os.system("poweroff")
    elif('mail' in command):
        engine.say("command recieved")
        time.sleep(1)
        os.system("iceweasel mail.google.com")
except:
    pass
