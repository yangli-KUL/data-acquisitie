#!/usr/bin/env python

import RPi.GPIO as GPIO 
import time
from mraa import getGpioLookup
from upm import pyupm_buzzer as upmBuzzer

from grove.button import Button

from grove.grove_ryb_led_button import GroveLedButton

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

BUZZER = 12

GPIO.setup(BUZZER, GPIO.OUT)



def buzz(noteFreq, duration):

  halveWaveTime = 1 / (noteFreq * 3 )

  waves = int(duration * noteFreq)

  for i in range(waves):

    GPIO.output(BUZZER, True)

    time.sleep(halveWaveTime)

    GPIO.output(BUZZER, False)

    time.sleep(halveWaveTime)

 

def main():

  # Grove - LED Button connected to port D5

  button = GroveLedButton(5)



  def on_event(index, event, tm):
    if event & Button.EV_SINGLE_CLICK:
      print('single click')
      button.led.light(True)
      buzz(262, 1)

    elif event & Button.EV_LONG_PRESS:
      print('long press')
      button.led.light(False)
      buzz(1000, 1)

  button.on_event = on_event
  while True:
    time.sleep(1)

 

if __name__ == '__main__':

  main()









