#Programa de simulacion de colores del asistente por medio de una ventana

import tkinter
import time

mute = '#F26344'
awake = '#6482ED'
listening = '#67d69e'
processing = ['#67d69e', '#67d7a2', '#67d8a7', '#67d9ab', '#67dab0', '#67dbb4', '#67dcb9', '#67ddbd', '#67dec1', '#67dfc6', '#68e0ca', '#68e1cf', '#68e2d3', '#68e3d7', '#68e4dc', '#68e5e0', '#68e6e5', '#68e7e9', '#68e8ee', '#68e9f2', '#68e9f2', '#67e6e9', '#65e2e0', '#64dfd7', '#63dbce', '#62d8c5', '#60d4bc', '#5fd1b3', '#5eceaa', '#5dcaa1', '#5bc799', '#5ac390', '#59c087', '#58bd7e', '#56b975', '#55b66c', '#54b263', '#53af5a', '#51ab51', '#50a848', '#50a848', '#51aa4d', '#52ad51', '#54af56', '#55b25a', '#56b45f', '#57b763', '#58b968', '#5abb6c', '#5bbe71', '#5cc075', '#5dc37a', '#5fc57e', '#60c783', '#61ca87', '#62cc8c', '#63cf90', '#65d195', '#66d499', '#67d69e']
#processing = ['#cc3733', '#c93735', '#c73737', '#c43739', '#c1373b', '#be373d', '#bc373f', '#b93741', '#b63744', '#b43746', '#b13748', '#ae374a', '#ab374c', '#a9374e', '#a63750', '#a33852', '#a13854', '#9e3856', '#9b3858', '#98385a', '#96385c', '#93385e', '#903860', '#8e3863', '#8b3865', '#883867', '#853869', '#83386b', '#80386d', '#7d386f', '#7b3871', '#783873', '#753875', '#733877', '#703879', '#6d387b', '#6a387d', '#683880', '#653882', '#623884', '#603886', '#5d3888', '#5a388a', '#57388c', '#55388e', '#523990', '#4f3992', '#4d3994', '#4a3996', '#473998', '#44399a', '#42399c', '#3f399f', '#3c39a1', '#3a39a3', '#3739a5', '#3439a7', '#3139a9', '#2f39ab', '#2c39ad']
test = tkinter.Tk()
test.title("Test")
test.geometry("320x320")

#Mute
test.config(background=mute)
test.update()
time.sleep(3)

#Awake
test.config(background=awake)
test.update()
time.sleep(5)

#Listening
test.config(background=listening)
test.update()
time.sleep(5)

#Processing
for j in range(4):
    for i in range(60):
        test.config(background=processing[i])
        test.update()
        time.sleep(0.05)
    
test.mainloop()
