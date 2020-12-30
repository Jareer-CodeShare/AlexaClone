import webbrowser
import speech_recognition as sr
import pyjokes
import pyttsx3 as p
import datetime
import wikipedia
import os

engine = p.init()
engine.setProperty("rate", 100)

def text(text):
    engine.say(text)
    engine.runAndWait()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

name = input("Enter your name: ")
engine.say("Hi," + name)
engine.runAndWait()


r = sr.Recognizer()

try:
    print(bcolors.OKBLUE + bcolors.BOLD + "                                                Welcome to Siri" + bcolors.ENDC)
    with sr.Microphone() as source:
        print(bcolors.OKGREEN + bcolors.BOLD + "Say Something..." + bcolors.ENDC)
        voice = r.listen(source)
        command = r.recognize_google(voice)
        print("done..")
        print(command)

    if command == "tell me a joke":
        engine.say(pyjokes.get_joke())
        engine.runAndWait()

    if command == "what is your name":
        engine.say("Oh, did I forget to introduce myself. Well I am Siri.")
        engine.runAndWait()

    if command == "what can you do":
        engine.say("I can tell you a joke, open apps for you, tell you summaries about stuff, tell the time and search google for you.")
        engine.runAndWait()

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        engine.say("The time is " + time)
        engine.runAndWait()
        print(time)

    if "who is" in command:
        person = command.replace("who is", '')
        info = wikipedia.summary(person, 1)
        engine.say(info)
        print(info)
        engine.runAndWait()

    if "what was" in command:
        person = command.replace("what was", '')
        infor = wikipedia.summary(person, 1)
        engine.say(infor)
        print(infor)
        engine.runAndWait()

    if "open" in command:
        app = command.split(" ", 1)[-1]
        text("opening " + app)
        os.startfile(app)

    if "search Google" in command:
        search = text("What do you want to search")
        url = "https://www.google.com/search?safe=strict&sxsrf=ALeKk00D9uvVFHYRFjpH3KOVhTmAljMZfA%3A1609064981017&ei=FWLoX-JM_4GFsg_SgLfIBQ&q=" + str(search)
        webbrowser.get().open(url)
except:
    print("Couldn't hear you...")
    pass
