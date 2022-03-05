# Project_Slavery

A python project to control multiple PCs remotely (kinda virus)

Communication is based on MQTT.

![master1](https://user-images.githubusercontent.com/78973793/156892629-92e0cf62-dd77-4ec5-aca4-ffb7c2b062a9.jpg)

Usage info:

master.py runs on the controller machine and slave.py on the slaves.
It is expected to give unique ids to slaves (edit the variable in slave.py), though a common id will still work but then commands cannot be directed to a particular slave.

To issue a command, type the name of the command followed by the arguments inside parenthesis.
E.g. ping is a command which pings all online slaves. It can be used in following ways:
  ping(Slave id)    # "Slave id" is the id of the target slave.
  ping(all)         #To ping all slaves
  ping()            #Same as above. If no target slave is specified (all or Slave id) the default is all.
  
The other commands can be used in same way. Refer function docs in documentation.html. The command format is function(args).
(Omit self keyword from the arguments).

All available commands:
1. message_to_slave,
2. send_file
3. execute_py
4. ping
5. chat
6. run_code

Refer docs for argument(s) information.

send_file can send any file to the slave. The path where the file is to be saved is an argument.
execute_py executes any python script on the slave provided the required packages are present.
run_code runs the code supplied in text format as the argument on the slave(s) (Uses builtin eval() on slave(s)).

Commands usage and results:

1. run_code(3+5)

![master4](https://user-images.githubusercontent.com/78973793/156894427-d0276621-6075-4e17-9e26-b22619bd8d1a.jpg)

3+5 is evaluated on slave.

2. chat(Slave 1)

![master2](https://user-images.githubusercontent.com/78973793/156892704-8c0f948f-36d6-4db9-ac41-f6ac8f275de2.jpg)

The terminal on the left is running on master and one on the right is on slave.

After exiting chat: (type exit in chat to quit)

![master3](https://user-images.githubusercontent.com/78973793/156892924-c8c64344-4264-4d19-8f30-84966fcdca0f.jpg)

The slave sends back the status of every commands executed.
The chat command is actually execute_py command which in turn executes chat_slave.py on slave machine.


