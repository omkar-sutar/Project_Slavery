import paho.mqtt.client as mqtt
import os
import signal

exit_app=False
curr_pid=os.getpid()

slave_id='Slave 1'

def on_message(client,userdata,message):
    global exit_app
    global curr_pid
    message=message.payload.decode()
    if message=='exit':
        exit_app=True
        os.kill(curr_pid,signal.SIGINT)
    print("\n"+message)

def mqtt_connect():
    try:
        slave=mqtt.Client(client_id="chatappslave")
        broker_address="broker.mqttdashboard.com"
        slave.connect(broker_address)
        slave.subscribe(topic="ChatApp99master",qos=0)
        slave.on_message=on_message
        slave.loop_start()
        return slave
    except:
        pass

slave=mqtt_connect()
print("$slave")

def chat(slave):
    global exit_app
    if exit_app==True:
        return
    slave_message=str(input(""))
    slave.publish("ChatApp99slave",qos=0,payload=slave_id+": "+slave_message)
    chat(slave)

    
chat(slave)
slave.loop_stop()