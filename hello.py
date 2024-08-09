from gtts import gTTS
import pygame
import os
import speech_recognition as sr
import webbrowser
import music
import requests

newsapi = "1c455bc7a0974d63bb2d61479b7c4445"

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")  # Save the audio file

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    os.remove("temp.mp3")  # Remove the file after playing
def processCommand(c):
    print (c)
    if c.lower()=='open google':
         webbrowser.open("https://www.google.com")
    elif c.lower()=='how are you':
         speak("I am fine, how about you?")
    elif c.lower().startswith("play"):
         word=c.lower().split(" ")[1]
         link = music.songs[word]
         webbrowser.open(link)
    elif "news" in c.lower():
         r = requests.get(f"https://newsapi.org/v2/everything?q=apple&from=2024-08-07&to=2024-08-07&sortBy=popularity&apiKey=1c455bc7a0974d63bb2d61479b7c4445")
         if r.status_code==200:
              data=r.json()
              articles=data.get('articles',[])
              for article in articles:
                   speak(article['title'])
         else:
              print("error")
    else:
         pass
         
         

if __name__ == '__main__':
    speak("Initializing Siri")
    
    recognizer = sr.Recognizer()
    
    while True:
            try:
                  with sr.Microphone() as source: 
                    print("Adjusting for ambient noise...")
                    recognizer.adjust_for_ambient_noise(source)
                    print("Listening....")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                    command = recognizer.recognize_google(audio)
                    print(command)
                    if (command.lower()=='hey siri'):
                            speak("yes?")
                            print("Siri active")
                            with sr.Microphone() as source: 
                                audio2 = recognizer.listen(source)
                                command = recognizer.recognize_google(audio2)
                                processCommand(command)
            except sr.UnknownValueError:
                print("Google could not understand the audio")
            except sr.RequestError as e:
                print("Google API error; {0}".format(e))
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
