import speech_recognition as sr
import requests
import json
from gtts import gTTS
import os, subprocess

global process

sendToChatGPT = "Eres un asistente de Voz llamada Lucy, quiero que respondas como asistente de voz segun el lenguaje en que venga el prompt, el prompt es el siguiente: "

OPENAI_API_KEY = "Bearer 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"



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)


try:
    consulta = r.recognize_google(audio, language = "es-MX")
    print("Yo: " + consulta)
    
    if consulta in 'Okay Lucy':
        #print("Lucy: Dime, en que te puedo ayudar?")
        # Here starts the query to ChatGPT
        subprocess.call(['nvlc',"FirstResponse.mp3",'--play-and-exit'])
        with sr.Microphone() as source:
            print("Lucy: Dime, en que te puedo ayudar?")
            audio = r.listen(source)
        
        try:
            sendToChatGPT2 = r.recognize_google(audio, language = "es-MX")
            print("Yo: " + sendToChatGPT2)
            
            sendToChatGPT = sendToChatGPT + sendToChatGPT2
            
            #print(sendToChatGPT)
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": OPENAI_API_KEY,
            }

            data = {
                "model": "text-davinci-003",
                "prompt": sendToChatGPT,
                "temperature": 0.7,
                "max_tokens": 512,
                "top_p": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
            }
            
            response = requests.post("https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data))
            response_json = response.json()
            text = response_json["choices"][0]["text"]
            mytext = "" + text
            myobj = gTTS(text=mytext, lang='es', slow=False)

            myobj.save("sound.mp3")
            subprocess.call(['nvlc',"sound.mp3",'--play-and-exit'])
            
            # Aquí puedes hacer lo que necesites con la respuesta
            print("Lucy: " + text)
            
        except sr.UnknownValueError:
            print("Lucy: I didnt understand what you said")

        except sr.RequestError as e:
            print("Lucy: I am currently unavailable, {0}".format(e))
    
    
    else:
        print("Lucy: No hay nada")
    
except sr.UnknownValueError:
    print("Lucy: I didnt understand what you said")

except sr.RequestError as e:
    print("Lucy: I am currently unavailable, {0}".format(e))
