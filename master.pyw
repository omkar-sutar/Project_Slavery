import paho.mqtt.client as mqtt
import os
import ast
import threading
import subprocess
import master_gui_widgets
import tkinter as tk
import time

class Master:
    def __init__(self):
        self.messages_from_slaves=[]
        self.functions=[self.message_to_slave,self.on_message_from_slave,self.send_file,self.execute_py,self.ping,self.chat,self.run_code]
        self.window=master_gui_widgets.window(self.on_input)
        self.mqtt_connected=False
        self.window.root.protocol("WM_DELETE_WINDOW", self.on_window_close)
        self.connect_mqtt()
    def on_window_close(self):
        self.window.root.destroy()
        exit()
    def connect_mqtt(self):
        try:
            self.master=mqtt.Client(client_id="Master")
            self.broker_address="broker.mqttdashboard.com"
            self.master.connect(self.broker_address)
            self.master.subscribe(topic="from_slave",qos=0)
            self.master.on_message=self.on_message_from_slave
            self.window.show("MQTT connection established.\n")
            self.mqtt_connected=True
        except:
            print("Error establishing MQTT connection.\n Trying again in 3 secs.\n")
            time.sleep(3)
            self.connect_mqtt()

    #Message to slave
    def message_to_slave(self,message_dict_str):
        """Dont use this function directly, other functions use this function behind the scenes."""
        self.master.publish("from_master",qos=0,payload=message_dict_str)

    
    #On message from slave
    def on_message_from_slave(self,client,userdata,message):
        message=message.payload.decode()
        message=ast.literal_eval(message)
        self.messages_from_slaves.append(message)
        if message["action"]=="text_message":
            message_from=message["from"]
            data=message["data"]
            string=f"Message from: {message_from} | Message: {data}"
            self.window.show(string+'\n')
            print(string)

    #Ping

    def ping(self,slave_id='all'):
        """ Call this function to get status of slaves i.e. whether they are online and listening.\n
        Arguments: slave_id: The id of the slave to ping. Defaults to 'all' i.e. pings everyone."""
        message={"to":slave_id,"action":"ping"}
        self.message_to_slave(str(message))

    #Send file to slave

    def send_file(self,filename_on_master,filename_on_slave,slave_id='all'):
        """Sends a file to the slave(s) """ 
        with open(filename_on_master,'rb') as fil:
            fil=fil.read()
            message={"to":slave_id,"action":"save_file","filename":filename_on_slave,"data":fil}
            self.message_to_slave(str(message))

    #Execute python script on slave

    def execute_py(self,filename_on_master,filename_on_slave,slave_id='all'):
        """Execute a python script on slave(s). The script is first downloaded on slave, executed and then deleted."""
        with open(filename_on_master,'rb') as fil:
            fil=fil.read()
            message={"to":slave_id,"action":"execute_py","filename":filename_on_slave,"data":fil}
            self.message_to_slave(str(message))

    def chat(self,slave_id='all'):
        """Chat function. Master and slave(s) can chat. Enter "exit" to close chat."""
        self.execute_py("custompkgs/chat_slave.py","chat_slave.py",slave_id=slave_id)
        subprocess.call(f"python {os.path.join(os.getcwd(),'custompkgs','chat_master.py')}",creationflags=subprocess.CREATE_NEW_CONSOLE)

    def run_code(self,code_text,slave_id='all'):
        """Run the code present in code_text on the slave(s). The result if any will be returned by the corresponding slaves."""
        message={"to":slave_id,"action":"run_code","code_text":code_text}
        self.message_to_slave(str(message))

    def on_input(self,string):
        if len(string)<3 or '(' not in string or ')' not in string:
            self.window.show("Error: INVALID INPUT\n")
            return
        function_name=string[:string.index('(')]
        if function_name not in [func.__name__ for func in self.functions]:
            self.window.show("Error: INVALID FUNCTION\n")
            return
        for func in self.functions:
            if func.__name__==function_name:
                function_args_str=str(string[string.index('(')+1:string.rindex(')')])
                function_args=function_args_str.rsplit(',')
                if function_args[0]=='':
                    func()
                else:
                    try:
                        func(*function_args)
                    except TypeError:
                        self.window.show("Error: INVALID NUMBER OF ARGUMENT(S) TO FUNCTION")

    def mqtt_loop(self):
        self.master.loop_forever()


if __name__ == '__main__':
    #Set up mqtt object. Handles all mqtt stuff. Also instantiates 'master_gui.window' internally.
    m=Master()
    threading.Thread(target=m.mqtt_loop,daemon=True).start()

    m.window.show("Getting active slaves...\n")
    m.ping()
    m.window.root.mainloop()