#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import RPi.GPIO as GPIO
import time
from threading import Timer

# define motion pin
motion_pin = 23

# set GPIO as GPIO.BOARD
GPIO.setmode(GPIO.BCM)
# set pin mode as INPUT
GPIO.setup(motion_pin, GPIO.IN)

def ExecuteExemple():
    #Do your shit here
    messagebox.showinfo("BipBip", "I'm a sheep")

def app_lost_focus(event):
    t.cancel()
    exit()
    
def on_closing():
    t.cancel()
    exit()
   
window = Tk() # Main form
window.geometry("460x200+400+100")

lblTitle = Label(window, text="Mouvement(Rouge = aucun, Vert = mouvement) : ", font=("Courier", 12))
lblMovement = Label(window, bg="Red", width="54", height=5)

lblTitle.place(x=10, y=50)
lblMovement.place(x=10, y=70)

def loop():
    if(GPIO.input(motion_pin) == 0):
        lblMovement.config(bg = "red")
    elif(GPIO.input(motion_pin) == 1):
        lblMovement.config(bg = "green")
    t = Timer(0.1, loop)
    t.start()
t = Timer(0.1, loop)
t.start()

window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() # Load the form 

