#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import RPi.GPIO as GPIO
import time
from threading import Timer
# define sound pin
sound_pin = 24
flag = True
# set GPIO mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)
# setup pin as INPUT
GPIO.setup(sound_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def SoundDetected(lbl):
    #Do your shit here
    lbl.config(bg = "green")

def NoSoundDetected(lbl):
    lbl.config(bg="red")

def app_lost_focus(event):
    t.cancel()
    exit()
    
    
def on_closing():
    t.cancel()
    exit()

window = Tk() # Main form
window.geometry("400x300+400+100")
lblSound = Label(window, bg="red", height=10, width=30)
lblSound.place(x=80, y=50)
# Call SoundDetected when there's sound
# Call NoSoundDetected after SoundDetected to reset the label
window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
def loop():
    global counter
    if(GPIO.input(sound_pin)==GPIO.LOW):
        print ("hello, world s")
        SoundDetected(lblSound)
        counter = 0
    else:
        print ("hello, world ns")
        if counter == 5:
            NoSoundDetected(lblSound)
        else:
            counter += 1
    print ("hello, world")
    t = Timer(0.1, loop)
    t.start()
counter = 0
t = Timer(0.1, loop)
t.start()
window.mainloop() # Load the form
    




