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

![master2](https://user-images.githubusercontent.com/78973793/156894772-4d701d58-5b2e-4881-b11a-e2c2cab3836b.jpg)

The terminal on the left is running on master and one on the right is on slave.

After exiting chat: (type exit in chat to quit)

![master3](https://user-images.githubusercontent.com/78973793/156892924-c8c64344-4264-4d19-8f30-84966fcdca0f.jpg)

The slave sends back the status of every commands executed.
The chat command is actually execute_py command which in turn executes chat_slave.py on slave machine.


documentation:

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module master</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>master</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:e%3A%5Cpy%5Cpy%5Cproject_slavery%5Cmaster.pyw">e:\py\py\project_slavery\master.pyw</a></font></td></tr></table>
    <p></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="ast.html">ast</a><br>
<a href="master_gui_widgets.html">master_gui_widgets</a><br>
</td><td width="25%" valign=top><a href="paho.mqtt.client.html">paho.mqtt.client</a><br>
<a href="os.html">os</a><br>
</td><td width="25%" valign=top><a href="subprocess.html">subprocess</a><br>
<a href="threading.html">threading</a><br>
</td><td width="25%" valign=top><a href="time.html">time</a><br>
<a href="tkinter.html">tkinter</a><br>
</td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ee77aa">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Classes</strong></big></font></td></tr>
    
<tr><td bgcolor="#ee77aa"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl>
<dt><font face="helvetica, arial"><a href="builtins.html#object">builtins.object</a>
</font></dt><dd>
<dl>
<dt><font face="helvetica, arial"><a href="master.html#Master">Master</a>
</font></dt></dl>
</dd>
</dl>
 <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="Master">class <strong>Master</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>
    
<tr><td bgcolor="#ffc8d8"><tt>&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="Master-__init__"><strong>__init__</strong></a>(self)</dt><dd><tt>Initialize&nbsp;self.&nbsp;&nbsp;See&nbsp;help(type(self))&nbsp;for&nbsp;accurate&nbsp;signature.</tt></dd></dl>

<dl><dt><a name="Master-chat"><strong>chat</strong></a>(self, slave_id='all')</dt><dd><tt>Chat&nbsp;function.&nbsp;<a href="#Master">Master</a>&nbsp;and&nbsp;slave(s)&nbsp;can&nbsp;chat.&nbsp;Enter&nbsp;"exit"&nbsp;to&nbsp;close&nbsp;chat.</tt></dd></dl>

<dl><dt><a name="Master-connect_mqtt"><strong>connect_mqtt</strong></a>(self)</dt></dl>

<dl><dt><a name="Master-execute_py"><strong>execute_py</strong></a>(self, filename_on_master, filename_on_slave, slave_id='all')</dt><dd><tt>Execute&nbsp;a&nbsp;python&nbsp;script&nbsp;on&nbsp;slave(s).&nbsp;The&nbsp;script&nbsp;is&nbsp;first&nbsp;downloaded&nbsp;on&nbsp;slave,&nbsp;executed&nbsp;and&nbsp;then&nbsp;deleted.</tt></dd></dl>

<dl><dt><a name="Master-message_to_slave"><strong>message_to_slave</strong></a>(self, message_dict_str)</dt><dd><tt>Dont&nbsp;use&nbsp;this&nbsp;function&nbsp;directly,&nbsp;other&nbsp;functions&nbsp;use&nbsp;this&nbsp;function&nbsp;behind&nbsp;the&nbsp;scenes.</tt></dd></dl>

<dl><dt><a name="Master-mqtt_loop"><strong>mqtt_loop</strong></a>(self)</dt></dl>

<dl><dt><a name="Master-on_input"><strong>on_input</strong></a>(self, string)</dt></dl>

<dl><dt><a name="Master-on_message_from_slave"><strong>on_message_from_slave</strong></a>(self, client, userdata, message)</dt><dd><tt>#On&nbsp;message&nbsp;from&nbsp;slave</tt></dd></dl>

<dl><dt><a name="Master-on_window_close"><strong>on_window_close</strong></a>(self)</dt></dl>

<dl><dt><a name="Master-ping"><strong>ping</strong></a>(self, slave_id='all')</dt><dd><tt>Call&nbsp;this&nbsp;function&nbsp;to&nbsp;get&nbsp;status&nbsp;of&nbsp;slaves&nbsp;i.e.&nbsp;whether&nbsp;they&nbsp;are&nbsp;online&nbsp;and&nbsp;listening.<br>
&nbsp;<br>
Arguments:&nbsp;slave_id:&nbsp;The&nbsp;id&nbsp;of&nbsp;the&nbsp;slave&nbsp;to&nbsp;ping.&nbsp;Defaults&nbsp;to&nbsp;'all'&nbsp;i.e.&nbsp;pings&nbsp;everyone.</tt></dd></dl>

<dl><dt><a name="Master-run_code"><strong>run_code</strong></a>(self, code_text, slave_id='all')</dt><dd><tt>Run&nbsp;the&nbsp;code&nbsp;present&nbsp;in&nbsp;code_text&nbsp;on&nbsp;the&nbsp;slave(s).&nbsp;The&nbsp;result&nbsp;if&nbsp;any&nbsp;will&nbsp;be&nbsp;returned&nbsp;by&nbsp;the&nbsp;corresponding&nbsp;slaves.</tt></dd></dl>

<dl><dt><a name="Master-send_file"><strong>send_file</strong></a>(self, filename_on_master, filename_on_slave, slave_id='all')</dt><dd><tt>Sends&nbsp;a&nbsp;file&nbsp;to&nbsp;the&nbsp;slave(s)</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table></td></tr></table>
</body></html>
