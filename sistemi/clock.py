import tkinter as tk
from tkinter import *
from threading import Thread
import time
from datetime import datetime
class threadOra (Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            l["text"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        
window = tk.Tk()
window.geometry("400x300")
window.title("CLOCK")
window.configure(bg = "yellow")
l = Label(window,text="123",bg="yellow")
l.place(x=200,y=150, anchor="center")
l["text"] = "ciao"
thread_ora = threadOra()
thread_ora.start()
window.mainloop()