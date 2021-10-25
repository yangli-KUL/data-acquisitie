import RPi.GPIO as GPIO
import time


BUZZER = 22
def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
       GPIO.output(BUZZER, True)
       time.sleep(halveWaveTime)
       GPIO.output(BUZZER, False)
       time.sleep(halveWaveTime)

def play(B):
    t=0
    freq_min = 100
    freq_max = 2000
    duration_min = 0
    duration_max = 0.2
    freq = freq_min +(freq_max-freq_min)/20*(20-B)
    dura = duration_min + (duration_max-duration_min)/20*(B)
    notes=[freq for i in range(1)]
    duration=[dura for i in range(1)]
    for n in notes:
        buzz(n, 0.1)
        time.sleep(duration[t])
        t+=1