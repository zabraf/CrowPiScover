#!/usr/bin/python3
import sys
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from threading import Timer
import RPi.GPIO as GPIO
import MFRC522
import signal
import time



def app_lost_focus(event):
    global canrun
    canrun = False
    t.cancel()
    sys.exit("Error message")
    exit()
    
def on_closing():
    global canrun
    canrun = False
    t.cancel()
    GPIO.cleanup()
    exit()
   
window = Tk() # Main form
window.geometry("400x200+400+100")

lblTemperature = Label(window, text="Valeur de la carte : ", font=("Courier", 20))
lblRFID = Label(window, text="", font=("Courier", 15))

lblTemperature.place(x=10, y=10)
lblRFID.place(x=10, y=50)

def end_read(signal,frame):
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)
# create the reader object
MIFAREReader = MFRC522.MFRC522()

canrun = True
def loop():
    global canrun
    if canrun:
        # detect touch of the card, get status and tag type
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # Get the RFID card uid and status
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If status is alright, continue to the next stage
        if status == MIFAREReader.MI_OK:
            # Print UID
            lblRFID.config(text="%s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
            time.sleep(2)
        t = Timer(1, loop)
        t.start()
    else :
        exit()
t = Timer(1, loop)
t.start()

window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() # Load the form 

