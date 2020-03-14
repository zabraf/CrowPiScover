#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import RPi.GPIO as GPIO
import time



def ExecuteExemple():
    GPIO.setmode(GPIO.BCM)
    TRIG = 16
    ECHO = 12
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
      pulse_start = time.time()
    while GPIO.input(ECHO)==1:
      pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    lblDistance.config(text="Distance : \n" + str(distance) + "cm")
    GPIO.cleanup()

def app_lost_focus(event): 
    exit()

window = Tk() # Main form
window.geometry("300x300+400+100")
lblDistance = Label(window, text="Distance : ", font=("Courier", 20))
lblDistance.place(x=10, y=150)
Button(window, command= lambda: ExecuteExemple(), bg="green", activebackground="darkgreen", width="17", height="5").place(x=50, y=30)
window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 

