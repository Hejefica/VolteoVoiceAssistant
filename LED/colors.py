import RPi.GPIO as GPIO
import time

fast_transition = 0.02
slow_transition = 0.05

mute = [100, 7, 8]
awake = [39, 51, 93]
listening = [40, 96, 62]

m_to_a = [[100, 7, 8], [98, 9, 11], [96, 11, 14], [94, 12, 16], [92, 13, 20], [89, 15, 22], [87, 16, 25], [85, 18, 28], [83, 20, 31], [81, 21, 34], [79, 22, 37], [77, 24, 40], [75, 25, 43], [73, 27, 46], [71, 29, 49], [69, 30, 52], [66, 31, 55], [64, 33, 58], [62, 35, 61], [60, 36, 64], [58, 38, 67], [56, 39, 69], [54, 40, 73], [52, 42, 75], [50, 44, 78], [47, 45, 81], [45, 47, 84], [44, 48, 87], [41, 49, 90], [39, 51, 93]]
a_to_l = [[39, 51, 93], [39, 53, 92], [39, 54, 91], [39, 56, 90], [39, 57, 89], [40, 59, 87], [40, 60, 87], [40, 62, 85], [40, 64, 84], [40, 65, 83], [40, 67, 82], [40, 68, 81], [40, 70, 80], [40, 71, 79], [40, 73, 78], [40, 75, 77], [40, 76, 76], [40, 78, 75], [40, 79, 74], [40, 81, 73], [40, 82, 72], [40, 84, 71], [40, 85, 69], [40, 87, 68], [40, 89, 67], [40, 90, 66], [40, 92, 65], [40, 93, 64], [40, 95, 63], [40, 96, 62]]
l_to_m = [[40, 96, 62], [42, 93, 60], [44, 90, 58], [47, 87, 56], [49, 84, 55], [51, 81, 53], [53, 78, 51], [55, 75, 49], [57, 72, 47], [59, 69, 45], [61, 66, 43], [63, 63, 42], [65, 60, 40], [67, 56, 38], [69, 53, 36], [71, 51, 34], [73, 47, 32], [75, 44, 30], [77, 41, 28], [80, 38, 27], [82, 35, 25], [84, 32, 23], [85, 29, 21], [88, 26, 19], [90, 23, 17], [92, 20, 15], [94, 16, 13], [96, 14, 12], [98, 11, 10], [100, 7, 8]]
err = [[80, 22, 20], [79, 22, 21], [78, 22, 22], [77, 22, 22], [76, 22, 23], [75, 22, 24], [74, 22, 25], [73, 22, 25], [71, 22, 27], [71, 22, 27], [69, 22, 28], [68, 22, 29], [67, 22, 30], [66, 22, 31], [65, 22, 31], [64, 22, 32], [63, 22, 33], [62, 22, 34], [61, 22, 35], [60, 22, 35], [59, 22, 36], [58, 22, 37], [56, 22, 38], [56, 22, 39], [55, 22, 40], [53, 22, 40], [52, 22, 41], [51, 22, 42], [50, 22, 43], [49, 22, 44], [48, 22, 44], [47, 22, 45], [46, 22, 46], [45, 22, 47], [44, 22, 47], [43, 22, 48], [42, 22, 49], [41, 22, 50], [40, 22, 51], [38, 22, 52], [38, 22, 53], [36, 22, 53], [35, 22, 54], [34, 22, 55], [33, 22, 56], [32, 22, 56], [31, 22, 57], [30, 22, 58], [29, 22, 59], [28, 22, 60], [27, 22, 60], [26, 22, 61], [25, 22, 62], [24, 22, 63], [23, 22, 64], [22, 22, 65], [20, 22, 65], [19, 22, 66], [18, 22, 67], [17, 22, 68]]
#proccessing = [[40, 84, 62], [40, 84, 64], [40, 85, 65], [40, 85, 67], [40, 85, 69], [40, 86, 71], [40, 86, 73], [40, 87, 74], [40, 87, 76], [40, 87, 78], [41, 88, 79], [41, 88, 81], [41, 89, 83], [41, 89, 84], [41, 89, 86], [41, 90, 88], [41, 90, 90], [41, 91, 91], [41, 91, 93], [41, 91, 95],[41, 91, 95], [40, 90, 91], [40, 89, 88], [39, 87, 84], [39, 86, 81], [38, 85, 77], [38, 83, 74], [37, 82, 70], [37, 81, 67], [36, 79, 63], [36, 78, 60], [35, 76, 56], [35, 75, 53], [35, 74, 49], [34, 73, 46], [33, 71, 42], [33, 70, 39], [33, 69, 35], [32, 67, 32], [31, 66, 28],[31, 66, 28], [32, 67, 30], [32, 68, 32], [33, 69, 34], [33, 70, 35], [34, 71, 37], [34, 72, 39], [35, 73, 41], [35, 73, 42], [36, 75, 44], [36, 75, 46], [36, 76, 48], [37, 77, 49], [38, 78, 51], [38, 79, 53], [38, 80, 55], [39, 81, 56], [40, 82, 58], [40, 83, 60], [40, 84, 62]]
proccessing = [[40, 96, 62], [43, 96, 60], [45, 95, 58], [47, 94, 55], [50, 93, 53], [53, 92, 51], [55, 91, 49], [57, 91, 47], [60, 90, 45], [62, 89, 42], [64, 88, 40], [67, 87, 38], [69, 86, 36], [71, 85, 34], [74, 85, 32], [76, 84, 29], [79, 83, 27], [81, 82, 25], [84, 81, 23], [86, 80, 21], [86, 80, 21], [83, 80, 21], [80, 79, 22], [77, 78, 22], [75, 77, 22], [71, 76, 23], [69, 76, 23], [66, 75, 24], [63, 74, 24], [60, 73, 24], [57, 73, 25], [55, 72, 25], [51, 71, 25], [49, 71, 26], [46, 70, 26], [43, 69, 27], [40, 68, 27], [37, 67, 27], [34, 67, 28], [31, 66, 28], [31, 66, 28], [32, 67, 30], [32, 69, 32], [33, 71, 34], [33, 72, 35], [34, 74, 37], [34, 76, 39], [35, 77, 41], [35, 79, 42], [36, 80, 44], [36, 82, 46], [36, 84, 48], [37, 85, 49], [38, 87, 51], [38, 88, 53], [38, 90, 55], [39, 92, 56], [40, 93, 58], [40, 95, 60], [40, 96, 62]]
freq = 70
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)    #R
GPIO.setup(13, GPIO.OUT)    #G
GPIO.setup(15, GPIO.OUT)    #B

r = GPIO.PWM(11,freq)
g = GPIO.PWM(13,freq)
b = GPIO.PWM(15,freq)

r.start(0)
g.start(0)
b.start(0)

def process():
    
    while(True):
    
        for i in range(60):

            r.ChangeDutyCycle(proccessing[i][0])
            g.ChangeDutyCycle(proccessing[i][1])
            b.ChangeDutyCycle(proccessing[i][2])

            time.sleep(fast_transition)

def muted():
    r.ChangeDutyCycle(mute[0])
    g.ChangeDutyCycle(mute[1])
    b.ChangeDutyCycle(mute[2])

    time.sleep(fast_transition)

def awaked():
    r.ChangeDutyCycle(awake[0])
    g.ChangeDutyCycle(awake[1])
    b.ChangeDutyCycle(awake[2])

    time.sleep(fast_transition)

def listened():
    r.ChangeDutyCycle(listening[0])
    g.ChangeDutyCycle(listening[1])
    b.ChangeDutyCycle(listening[2])

    time.sleep(fast_transition)


def mute_to_awake():
    
    
    for i in range(30):

        r.ChangeDutyCycle(m_to_a[i][0])
        g.ChangeDutyCycle(m_to_a[i][1])
        b.ChangeDutyCycle(m_to_a[i][2])

        time.sleep(fast_transition)

def awake_to_mute():
    
    i = 30
    for j in range(30):

        i-=1
        r.ChangeDutyCycle(m_to_a[i][0])
        g.ChangeDutyCycle(m_to_a[i][1])
        b.ChangeDutyCycle(m_to_a[i][2])

        time.sleep(fast_transition)

def awake_to_listening():
    
    
    for i in range(30):

        r.ChangeDutyCycle(a_to_l[i][0])
        g.ChangeDutyCycle(a_to_l[i][1])
        b.ChangeDutyCycle(a_to_l[i][2])

        time.sleep(fast_transition)

def listening_to_awake():
    
    i = 30 
    for j in range(30):

        i -= 1
        r.ChangeDutyCycle(a_to_l[i][0])
        g.ChangeDutyCycle(a_to_l[i][1])
        b.ChangeDutyCycle(a_to_l[i][2])

        time.sleep(slow_transition)

def listening_to_mute():
    
    
    for i in range(30):

        r.ChangeDutyCycle(l_to_m[i][0])
        g.ChangeDutyCycle(l_to_m[i][1])
        b.ChangeDutyCycle(l_to_m[i][2])

        time.sleep(fast_transition)

muted()

time.sleep(5)

mute_to_awake()

time.sleep(5)

awake_to_mute()

time.sleep(5)

mute_to_awake()

time.sleep(5)

awake_to_listening()

time.sleep(5)

listening_to_awake()

time.sleep(5)

awake_to_listening()

time.sleep(5) 

listening_to_mute()

time.sleep(5)

GPIO.cleanup()