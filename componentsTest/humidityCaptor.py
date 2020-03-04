#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def ExecuteExemple():
    #Do your shit here
    messagebox.showinfo("BipBip", "I'm a sheep")

def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("400x200+400+100")

lblTemperature = Label(window, text="Température : ", font=("Courier", 20))
lblHumidity = Label(window, text="Humidité : ", font=("Courier", 20))

lblTemperature.place(x=10, y=50)
lblHumidity.place(x=10, y=80)

window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 

