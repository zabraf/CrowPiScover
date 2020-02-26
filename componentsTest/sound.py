#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def SoundDetected(lbl):
    #Do your shit here
    lbl.config(bg = "green")

def NoSoundDetected(lbl):
    lbl.config(bg="red")

def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("400x300+400+100")

lblSound = Label(window, bg="red", height=10, width=30)
lblSound.place(x=80, y=50)
# Call SoundDetected when there's sound
# Call NoSoundDetected after SoundDetected to reset the label
window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 

