import speech_recognition as sp
import pyttsx3
import os

pyttsx3.speak ("Hello my name is lucie")
print("Hello my name is lucie")
#ceci est un commentaire
pyttsx3.speak ("what is your name")
#Ici nous allons entrez(ecrit) notre nom et l'ordinateur va repondre en appelans notre nom
print("Enter your name:")
x = input()
print("Hello, " + x)
pyttsx3.speak ("Hello, " + x)
pyttsx3.speak ("what can i do for you" + x)
#Ici nous allons dire(de maniere vocal) a notre ordinateur d'executer une instruction par exemple lui dire "lucie open firefox" pour cela nous allons attendre qu'il affiche le message "wait for dpeach" avant de parler
r = sp.Recognizer()
with sp.Microphone() as source:
    print("Wait for speach")
    output = r.listen(source)
    print("done")

data = r.recognize_google(output)

print(data)
if"firefox" in y :
  os.system("start firefox")
elif"chrome" in y :
  os.system("start chrome")
else:
  pyttsx3.speak ("are you sure that it is an internal command")
  
