import tkinter as tk 
import datetime
import threading

#Window class. Has every widget and functions to control them.
class window:
    def __init__(self,input_event_handler):
        self.root=tk.Tk()
        self.root.wm_attributes("-alpha",0.8)
        self.root.title("Master")
        self.root.geometry("720x480")

        self.textbox=tk.Text(master=self.root,bg='black',fg="#79FF33",border=0,padx=10)
        self.textbox.config(font=("Verdana",10))
        self.textbox.config(state='disabled')
        self.textbox.pack(expand=True,fill='both')

        self.textbox_input=tk.Text(master=self.root,bg='black',fg="#79FF33",border=0,padx=7,height=2,pady=1,insertbackground="#79FF33")
        self.textbox_input.pack(fill='x')
        self.textbox_input.focus_set()

        self.inputs=[]

        self.root.bind("<Button-1>",self.set_input_focus)
        self.show(datetime.datetime.now().strftime("%d %B, %Y  %H:%M:%S \n"))
        self.root.bind('<Return>',self.on_input)
        self.input_event_handler=input_event_handler

    def set_input_focus(self,event):
        self.textbox_input.focus()
    
    #Shows the string in the Output textbox.

    def show(self,string):
        self.textbox.config(state='normal')
        self.textbox.insert(tk.END,str(string))
        self.textbox.config(state='disabled')
        self.textbox.see(tk.END)
    


    def time(self):
        return datetime.datetime.now().strftime("%H:%M:%S ")

    #Trigerred when Enter is pressed.

    def on_input(self,event):
        text=self.textbox_input.get("1.0",tk.END)
        self.show('\n'+self.time()+"$"+text)
        self.textbox_input.delete("1.0",tk.END)
        self.inputs.append(text)
        threading.Thread(target=self.input_event_handler,args=(text,)).start()
