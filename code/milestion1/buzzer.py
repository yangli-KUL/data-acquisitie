import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER = 12
GPIO.setup(BUZZER, GPIO.OUT)

def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
       GPIO.output(BUZZER, True)
       time.sleep(halveWaveTime)
       GPIO.output(BUZZER, False)
       time.sleep(halveWaveTime)

def play():
    t=0
    notes=[3000+i*30 for i in range(3)]
    duration=[1 for i in range(3)]
    for n in notes:
        buzz(n, duration[t])
        time.sleep(duration[t])
        t+=1

#buzz(262, 0.5)

play()