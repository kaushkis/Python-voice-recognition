import google.generativeai as genai
import speech_recognition as sr 
import os
from gtts import gTTS
import pygame

# speech Recognise

recognizer=sr.Recognizer()

# step 1
with sr.Microphone() as source:
  print("Speak Something")
  audio=recognizer.listen(source)
  
try:
    print("Reconizing...")
    text=recognizer.recognize_google(audio)
    print("you said:", text)

except sr.UnknownValueError:
    print("Sorry,Couldn't understand audio")
except sr.RequestError as e:
    print("Error Occured; {0}".format(e))
    
  # step 2
genai.configure(api_key="AIzaSyDeHKimdaHh8DiKoc3MrYC6BZcDOlTjWhQ")
  
generation_config={"temperature":0.9 , "top_p":1, "top_k":1, "max_output_tokens":2048 }

model=genai.GenerativeModel("models/gemini-2.5-pro-exp-03-25", generation_config=generation_config)

response=model.generate_content(text)
ans=response.text

print(ans)

# step 3

language="en"
tts=gTTS(text=ans, lang=language, slow=False)
tts.save("output.mp3")

pygame.mixer.init()

pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

# remove output file from system
os.remove("output.mp3") 