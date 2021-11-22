import paho.mqtt.client as mqtt
import time
def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("Connection failed")
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
print("hey2")
while connected!=True:
    time.sleep(0.2)
client.publish("v1/devices/me/telemetry","{'SPAINNN':'FRANCEEEE'}",2)
client.loop_stop()
    
