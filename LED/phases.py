import colors as leds
import RPi.GPIO as GPIO
import time

import speech_recognition as sr
from gtts import gTTS
import os, subprocess

global process
mute_pin = 19
status = 'awake'

GPIO.setup(mute_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BOARD)

def check():
    if GPIO.input(mute_pin) == 1:
        return True
    else:
        return False

def mute_button_pressed(channel):

    global status
    if GPIO.input(mute_pin) == 0 and status != 'mute':

        print('Pressed')
        print(status)
        if(status=='listening'):
            leds.listening_to_mute()
            status = 'mute'
        elif(status=='awake'):
            leds.awake_to_mute()
            status = 'mute'


    elif GPIO.input(mute_pin) == 1 and status == 'mute':        
        print('unmuted')
        leds.mute_to_awake()
        status = 'awake'

GPIO.add_event_detect(mute_pin, GPIO.BOTH, callback=mute_button_pressed,bouncetime=50)

def process():

    global status
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status ='awake'
        print("Say something!")
        audio = r.listen(source)
        

    try:
        consulta = r.recognize_google(audio, language = "es-MX")
        print("Yo: " + consulta)
        if (consulta in 'Okay Lucy') and (check() == True):
            #print("Lucy: Dime, en que te puedo ayudar?")
            # Here starts the query to ChatGPT
            #subprocess.call(['nvlc',"FirstResponse.mp3",'--play-and-exit'])
            leds.awake_to_listening()
            status = 'listening'
            with sr.Microphone() as source:
                print("Lucy: Dime, en que te puedo ayudar?")
                audio = r.listen(source)
            
            try:
                if check() == True:
                    leds.listening_to_awake()
                    status = 'awake'
                    print('estoy procesando')

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


while True:

    if GPIO.input(mute_pin) == 1:
        status = 'awake'
        leds.awaked()
        process()
    
    else:
        status = 'mute'
        leds.muted()
        time.sleep(1)