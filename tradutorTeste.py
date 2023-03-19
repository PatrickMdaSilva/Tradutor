import speech_recognition as sr #https://pypi.org/project/SpeechRecognition/
import pyttsx3 #https://pypi.org/search/?q=pyttsx3
from googletrans import Translator #https://pypi.org/project/googletrans2/
import time

rec = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
trans = Translator()

with sr.Microphone() as mic:
    
    while True:
        print("Pode Falar")
        try:
            rec.adjust_for_ambient_noise(mic)
            audio = rec.listen(mic)
            time.sleep(1)
            if audio != '':
                texto = rec.recognize_google(audio, language="pt-br")
                texto = texto.lower()
                if 'pergunta' in texto:
                    texto = texto.replace('pergunta','')
                    print (trans.translate(f"{texto}", dest='en').text)
                    engine.setProperty('voice', voices[1].id)
                    engine.say(trans.translate(f"{texto}").text)
                    engine.runAndWait()
                    engine.runAndWait()

                elif 'traduza' in texto:
                    print("Deseja continuar")
                    audio = rec.listen(mic)
                    texto = rec.recognize_google(audio, language="pt-br")
                    if 'não' in texto:
                        print("Saindo")
                    else:    
                        texto = input('Quer a tradução só insira o texto! ')
                        print (trans.translate(f"{texto}", dest='en').text)
                        engine.setProperty('voice', voices[1].id)
                        engine.say(trans.translate(f"{texto}").text)
                        engine.runAndWait()
                        engine.runAndWait()

                elif 'inglês' in texto:
                    print("Would you like to continue")
                    audio = rec.listen(mic)
                    texto = rec.recognize_google(audio, language="en") 
                    if 'no' in texto:
                        print("exit")
                    else:       
                        texto = input('Do you want me to do the translation? ')
                        print (trans.translate(f"{texto}", dest='pt').text)
                        engine.setProperty('voice', voices[0].id)
                        engine.say(trans.translate(f"{texto}",dest='pt').text)
                        engine.runAndWait()

                else:
                    texto = rec.recognize_google(audio, language="en")
                    print (trans.translate(f"{texto}", dest='pt').text)
                    engine.setProperty('voice', voices[0].id)
                    engine.say(trans.translate(f"{texto}",dest='pt').text)
                    engine.runAndWait()

        except:
            print("Repita")
            

           
    