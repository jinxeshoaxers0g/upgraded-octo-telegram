import pyttsx3

engine = pyttsx3.init()
text = input("🗣️ Enter text to convert to speech: ")
engine.say(text)
engine.runAndWait()
