#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import RPi.GPIO as GPIO
import time
buzzer_pin = 18

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# setup button pin asBu input and buzzer pin as output
GPIO.setup(buzzer_pin, GPIO.OUT)

def ExecuteExemple():
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(buzzer_pin, GPIO.LOW)


def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("400x200+300+200")
Button(window, command= lambda: ExecuteExemple(), bg="green", activebackground="darkgreen", width="17", height="5").place(x=100, y=50)
window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 
