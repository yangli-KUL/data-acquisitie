
import paho.mqtt.client as mqttclient
import time
import json
import csv

broker_address2="demo.thingsboard.io"
port2=1883
user2="imp"
password2="testmqtt"

def on_connect2(client,userdata,flags,rc):
    if rc==0:
        print("client2 is connected")
        global connected
        connected=True
    else:
        print("Coonection2 failed")

client2 = mqttclient.Client("client")
client2.username_pw_set("XhLJuBoOOObGp45JM2nQ")
client2.on_connect=on_connect2
client2.connect(broker_address2,port2)
# client2.loop_start()

row = ''

def on_connect(client,userdata,flags,rc):
    client.subscribe("mqtt/mil1")
    with open('data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["time", "angle", "distance" ])
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("Coonection failed")

def on_mes(client, userdata, message):
    global row
    row = json.loads(message.payload)
    print(row)
    with open('data.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([row["time"], row["angle"], row["distance"] ])
    client2.publish("v1/devices/me/telemetry",message.payload)
    # asyncio.run(hello())

connected=False
broker_address="mqtt.impcloud.org"
port=8883
user="imp"
password="testmqtt"

client=mqttclient.Client("server")
client.tls_set()
client.username_pw_set(user,password=password)
client.on_connect=on_connect
client.on_message=on_mes
client.connect(broker_address,port=port)

client.loop_forever()

while connected!=True:
    time.sleep(0.2)
