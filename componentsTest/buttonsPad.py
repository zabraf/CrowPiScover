#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import RPi.GPIO as GPIO
from threading import Timer
# define button pin
button_up_pin = 26
button_do_pin = 13
button_ri_pin = 19
button_le_pin = 25
# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# setup button pin asBu input and buzzer pin as output
GPIO.setup(button_up_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_ri_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_do_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_le_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def app_lost_focus(event):
    t.cancel()
    exit()
    
def on_closing():
    t.cancel()
    exit()

window = Tk() # Main form
window.geometry("400x300+400+100")
lblText = Label(window, text="Bouton appuyé(s) : ", font=("Courier", 20))
lblText.place(x=10, y=50)
lblValeur = Label(window, text="", font=("Courier", 15))
lblValeur.place(x=10, y=80)
# Call SoundDetected when there's sound
# Call NoSoundDetected after SoundDetected to reset the label
window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
def loop():
    text = "";
    if(GPIO.input(button_up_pin) == 0):
        text += "Haut, "
    if(GPIO.input(button_do_pin) == 0):
        text += "Bas, "
    if(GPIO.input(button_le_pin) == 0):
        text += "Gauche, "
    if(GPIO.input(button_ri_pin) == 0):
        text += "Droite, "
    lblValeur.config(text=text)
    t = Timer(0.1, loop)
    t.start()
t = Timer(0.1, loop)
t.start()
window.mainloop() # Load the form
    







