import pyttsx3
import os

pyttsx3.speak ("Hello my name is lucie")
print("Hello my name is lucie")
#ceci est un commentaire 
pyttsx3.speak ("what is your name")
print("Enter your name:")
x = input()
print("Hello, " + x)
pyttsx3.speak ("Hello, " + x)
#ceci est un commentaire 
pyttsx3.speak ("what can i do for you" + x)
y = input()
if"firefox" in y :
  os.system("start firefox")
elif"chrome" in y :
  os.system("start chrome")
else:
  pyttsx3.speak ("are you sure that it is an internal command")
  