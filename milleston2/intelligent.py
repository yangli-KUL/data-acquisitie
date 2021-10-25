import time, csv
import threading
from grove.grove_servo import GroveServo
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import RPi.GPIO as GPIO
from grove.grove_ryb_led_button import GroveLedButton
from numpy.lib.function_base import angle
import buzz

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzz.BUZZER, GPIO.OUT)

class buzzer(threading.Thread):
    def __init__(self, threadID, name, counter, dis):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.dis = dis
    def run(self):
        buzz.play(self.dis)

def main():
    sensor = GroveUltrasonicRanger(5)
    step_num = 30
    step = 1
    angle = [i*step for i in range(step_num)]
    ledbtn = GroveLedButton(16)
    direction = 1
    # play()
    i=0
    distance_list=[]
    angle_list=[]
    counter_max = 10
    counter = 0
    time_0 = 0
    with open('milleston2/data/intelligent_data.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['time', 'angle', 'distance' ])
    while True:
        if i>=(step_num-1) and direction==1:
            direction = -1
        if i<=0 and direction==-1:
            direction = 1
        angle1=angle[i]
        i += direction
        
        
        distance = sensor.get_distance()
        distance_list.append(distance)
        angle_list.append(angle1)
        
        
        if distance < 40:
            ledbtn.led.light(True)
            counter_max = round(0+distance/4)
            if counter >= counter_max:
                thread1 = buzzer(1, "Thread-1", 1, distance)
                thread1.start()
                counter = 0
            else:
                counter += 1
        if distance >40:
            ledbtn.led.light(False)
        time.sleep(0.2)
        time_0 += 0.2
        print(distance)
        with open('milleston2/data/intelligent_data.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([time_0, angle[i], distance ])

 
    # ledbtn = GroveLedButto
    # i=1
    # time_sleep=2
    # while True and i<4:
    #     ledbtn.led.light(True)
    #     print('turn on LED ')
    #     time.sleep(time_sleep)
        
    #     ledbtn.led.light(False)
    #     print('turn off LED ')
    #     time.sleep(time_sleep)
    #     i=i+1
  
  

if __name__ == '__main__':
    main()
