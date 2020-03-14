#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def app_lost_focus(event):
    exit()
    
def on_closing():
    exit()
window = Tk() # Main form
window.geometry("400x200+400+100")
lblTemperature = Label(window, text="Ne fonctionne pas \n malheursement :(", font=("Courier", 20))
lblTemperature.place(x=10, y=50)
window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() # Load the form 


