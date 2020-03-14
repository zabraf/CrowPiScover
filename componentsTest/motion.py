#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import RPi.GPIO as GPIO
from threading import Timer
# define motion pin
motion_pin = 23
# set GPIO as GPIO.BOARD
GPIO.setmode(GPIO.BCM)
# set pin mode as INPUT
GPIO.setup(motion_pin, GPIO.IN)


def MotionDetected(lbl):
    #Do your shit here
    lbl.config(bg = "green")

def NoMotionDetected(lbl):
    lbl.config(bg="red")

def app_lost_focus(event):
    t.cancel()
    exit()
    
def on_closing():
    t.cancel()
    exit()

window = Tk() # Main form
window.geometry("400x300+400+100")
lblMotion = Label(window, bg="red", height=10, width=30)
lblMotion.place(x=80, y=50)
# Call SoundDetected when there's sound
# Call NoSoundDetected after SoundDetected to reset the label
window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
def loop():
    global counter
    if(GPIO.input(motion_pin) == 0):
        NoMotionDetected(lblMotion)
    else:
        MotionDetected(lblMotion)
    t = Timer(0.1, loop)
    t.start()
counter = 0
t = Timer(0.1, loop)
t.start()
window.mainloop() # Load the form
    





