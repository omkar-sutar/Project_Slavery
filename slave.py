import paho.mqtt.client as mqtt
import ast
import os
import subprocess
import threading

slave_id='Slave 1'


slave=mqtt.Client(client_id=f"slave{slave_id}")
broker_address="broker.mqttdashboard.com"
slave.connect(broker_address)

slave.subscribe(topic="from_master",qos=0)

#Messaging master

def message_to_master(message_dict):
    """ message_dict format: {"action":"action_name","data":"data"}\n
    Available actions: "text_message"
    """
    message_dict["from"]=slave_id
    payload=str(message_dict)
    slave.publish(topic="from_slave",qos=0,payload=payload)


#Saving file on slave

def save_file_on_slave(filename,data):
    with open(filename,'wb') as fil:
        fil.write(data)
    print("File "+filename+" received.")
    message_dict={"action":"text_message","data":f"File {filename} received"}
    message_to_master(message_dict)
    
#Execute python script with name 'filename'
def execute_py(filename):
    subprocess.call(f"python {filename}",cwd=os.getcwd(),creationflags=subprocess.CREATE_NEW_CONSOLE)
    message_dict={"action":"text_message","data":f"File {filename} executed"}
    message_to_master(message_dict)
    os.remove(filename)
    print(filename + " executed")


def on_message_from_master(client,userdata,message):
    print("Incoming message")
    message=message.payload.decode()
    message=ast.literal_eval(message)
    action=message["action"]
    if message["to"]=='all' or message["to"]==slave_id:
        if action=='ping':
            message_dict={"action":"text_message","data":f"{slave_id} online"}
            message_to_master(message_dict)
        if action=="save_file":
            save_file_on_slave(message["filename"],message["data"])
        if action=="execute_py":
            filename_on_slave=message["filename"]
            save_file_on_slave(filename_on_slave, message["data"])
            threading.Thread(target=execute_py,args=(filename_on_slave,)).start()
            message_dict={"action":"text_message","data":f"File {filename_on_slave} execution thread started"}
            message_to_master(message_dict)
        

slave.on_message=on_message_from_master


slave.loop_forever()