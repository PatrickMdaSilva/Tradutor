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

                elif 'inglês' in texto:
                    print("Deseja continuar com a tradução escrita")
                    audio = rec.listen(mic)
                    texto = rec.recognize_google(audio, language="pt-br")
                    if 'sim' in texto:
                        texto = input('Escreva! ')
                        print (trans.translate(f"{texto}", dest='en').text)
                        engine.setProperty('voice', voices[1].id)
                        engine.say(trans.translate(f"{texto}").text)
                        engine.runAndWait()
                        engine.runAndWait()
                    else:    
                        print("Saindo")

                elif 'português' in texto:
                    print("Would you like to continue with the translation by writing?")
                    audio = rec.listen(mic)
                    texto = rec.recognize_google(audio, language="en") 
                    if 'yes' in texto:
                        texto = input('Write? ')
                        print (trans.translate(f"{texto}", dest='pt').text)
                        engine.setProperty('voice', voices[0].id)
                        engine.say(trans.translate(f"{texto}",dest='pt').text)
                        engine.runAndWait()
                    else:       
                        print("exit")

                else:
                    texto = rec.recognize_google(audio, language="en")
                    print (trans.translate(f"{texto}", dest='pt').text)
                    engine.setProperty('voice', voices[0].id)
                    engine.say(trans.translate(f"{texto}",dest='pt').text)
                    engine.runAndWait()

        except:
            print("Repita")
            

           
    