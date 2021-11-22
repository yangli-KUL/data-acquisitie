import time, csv
import threading
import paho.mqtt.client as mqtt
from grove import motor
from grove.grove_servo import GroveServo
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import RPi.GPIO as GPIO
from grove.grove_ryb_led_button import GroveLedButton
from numpy.lib.function_base import angle
import buzz
import motor
import json

import paho.mqtt.client as mqttclient
import time
def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("Coonection failed")
connected=False

broker_address="demo.thingsboard.io"
port=1883
user="imp"
password="testmqtt"

client = mqtt.Client()
client.username_pw_set("XhLJuBoOOObGp45JM2nQ")
client.on_connect=on_connect
client.connect(broker_address,port)
client.loop_start()
while connected!=True:
    time.sleep(0.2)



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzz.BUZZER, GPIO.OUT)
motor.motor_init()
class buzzer(threading.Thread):
    def __init__(self, threadID, name, counter, dis):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.dis = dis
    def run(self):
        buzz.play(self.dis)

Ultrasonic = GroveUltrasonicRanger(5)
step = 1
init_angle = 40
end_angle = 160
step_num = round((end_angle - init_angle)/step)
angle = [i*step+init_angle for i in range(step_num)]
ledbtn = GroveLedButton(16)


def main():
    i=0
    time_0 = 0
    direction = 1
    distance_list=[]
    angle_list=[]
    counter_max = 10
    counter = 0
    time_step = 0.1
    with open('data/intelligent_data.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'angle', 'distance' ])
    while True:
        
        if i>=(step_num-1) and direction==1:
            direction = -1
        if i<=0 and direction==-1:
            direction = 1
        angle1=angle[i]
        i += direction
        motor.motor_angle(angle1)
        time.sleep(time_step)
        time_0 += time_step

        distance = Ultrasonic.get_distance()
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
        
        
        
        print(distance)
        with open('data/intelligent_data.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([time_0, angle[i], distance ])
            x={
                "time":time_0,
                "angle":angle[i],
                "distance":distance
                }
            y=json.dumps(x)
    #         client.publish("mqtt/mil1",str([time_0, angle[i], distance ]))
            client.publish("v1/devices/me/telemetry",y)
            

 
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
