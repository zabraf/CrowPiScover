#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import RPi.GPIO as GPIO
import time
from threading import Timer
# define touch pin
touch_pin = 17

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# set GPIO pin to INPUT
GPIO.setup(touch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def TouchDetected(lbl):
    #Do your shit here
    lbl.config(bg = "green")

def NoToucheDetected(lbl):
    lbl.config(bg="red")

def app_lost_focus(event):
    t.cancel()
    exit()
    
def on_closing():
    t.cancel()
    exit()

window = Tk() # Main form
window.geometry("400x300+400+100")
lblTouch = Label(window, bg="red", height=10, width=30)
lblTouch.place(x=80, y=50)
# Call SoundDetected when there's sound
# Call NoSoundDetected after SoundDetected to reset the label
window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
def loop():
    global counter
    if(GPIO.input(touch_pin)):
        TouchDetected(lblTouch)        
    else:
        NoToucheDetected(lblTouch)
    t = Timer(0.1, loop)
    t.start()
t = Timer(0.1, loop)
t.start()
window.mainloop() # Load the form
    





