import paho.mqtt.client as mqtt
import threading

def on_message(client,userdata,message):
    message=message.payload.decode()
    print(message)
def mqtt_loop(client):
    client.loop_forever()

def mqtt_connect():
    try:
        master=mqtt.Client(client_id="chatappmaster")
        broker_address="broker.mqttdashboard.com"
        master.connect(broker_address)
        master.subscribe(topic="ChatApp99slave",qos=0)
        master.on_message=on_message
        #threading.Thread(target=mqtt_loop,args=(master,)).start()
        return master
    except:
        pass
master=mqtt_connect()
master.loop_start()

def chat(master):
    master_message=str(input("You: "))
    if master_message=="exit":
        master.publish("ChatApp99master",qos=0,payload=master_message)
        return
    master.publish("ChatApp99master",qos=0,payload="Hacker: "+master_message)
    chat(master)

chat(master)
master.loop_stop()