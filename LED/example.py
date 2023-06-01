import colors_asyncio as leds
from asyncio import gather, run, sleep
import RPi.GPIO as GPIO
import time

mute_pin = 19
status = 'awake'

GPIO.setup(mute_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BOARD)

async def mute_button_pressed():


    if GPIO.input(mute_pin) == 0:

        #print('Pressed')
        leds.listening_to_mute()
        time.sleep(0.02)

        while GPIO.input(mute_pin) == 0:
            #print('muted')
            time.sleep(1)
        
        leds.mute_to_awake()
        leds.awake_to_listening()


# GPIO.add_event_detect(mute_pin, GPIO.RISING, callback=mute_button_pressed,bouncetime=50)

async def main():

    await gather(
        leds.process(),
        mute_button_pressed())


try:
    
    while True:
        run(main())


except KeyboardInterrupt:
    
    GPIO.cleanup()
