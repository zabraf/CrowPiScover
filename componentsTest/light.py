#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from threading import Timer
import RPi.GPIO as GPIO
import smbus

class LightSensor():

    def __init__(self):

        # Define some constants from the datasheet

        self.DEVICE = 0x5c # Default device I2C address

        self.POWER_DOWN = 0x00 # No active state
        self.POWER_ON = 0x01 # Power on
        self.RESET = 0x07 # Reset data register value

        # Start measurement at 4lx resolution. Time typically 16ms.
        self.CONTINUOUS_LOW_RES_MODE = 0x13
        # Start measurement at 1lx resolution. Time typically 120ms
        self.CONTINUOUS_HIGH_RES_MODE_1 = 0x10
        # Start measurement at 0.5lx resolution. Time typically 120ms
        self.CONTINUOUS_HIGH_RES_MODE_2 = 0x11
        # Start measurement at 1lx resolution. Time typically 120ms
        # Device is automatically set to Power Down after measurement.
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
        # Start measurement at 0.5lx resolution. Time typically 120ms
        # Device is automatically set to Power Down after measurement.
        self.ONE_TIME_HIGH_RES_MODE_2 = 0x21
        # Start measurement at 1lx resolution. Time typically 120ms
        # Device is automatically set to Power Down after measurement.
        self.ONE_TIME_LOW_RES_MODE = 0x23

    def convertToNumber(self, data):

        # Simple function to convert 2 bytes of data
        # into a decimal number
        return ((data[1] + (256 * data[0])) / 1.2)

    def readLight(self):

        data = bus.read_i2c_block_data(self.DEVICE,self.ONE_TIME_HIGH_RES_MODE_1)
        return self.convertToNumber(data)

MAX_VALUE_LIGHT = 54612.5
 # Find the right revision for bus driver
if(GPIO.RPI_REVISION == 1):
    bus = smbus.SMBus(0)
else:
    bus = smbus.SMBus(1)
    
def app_lost_focus(event):
    t.cancel()
    exit()
    
def on_closing():
    t.cancel()
    exit()

window = Tk() # Main form
window.geometry("300x300+400+100")

lblVeryLowLight = Label(window, bg="red", width="2", height="2")
lblLowLight = Label(window, bg="red", width="2", height="4")
lblNormalLight = Label(window, bg="red", width="2", height="6")
lblHighLight = Label(window, bg="red", width="2", height="8")
lblVeryHighLight = Label(window, bg="red", width="2", height="10")

lblVeryLowLight.place(x=80, y=50)
lblLowLight.place(x=110, y=50)
lblNormalLight.place(x=140, y=50)
lblHighLight.place(x=170, y=50)
lblVeryHighLight.place(x=200, y=50)
lblVeryLowLight.bg = "green"
sensor = LightSensor()

def loop():
    global lblVeryLowLight
    print("Light Level : " + str(sensor.readLight()) + " lx")
    value = sensor.readLight()
    if(value < MAX_VALUE_LIGHT / 6):
        lblVeryLowLight.config(bg="red")
        lblLowLight.config(bg="red")
        lblNormalLight.config(bg="red")
        lblHighLight.config(bg="red")
        lblVeryHighLight.config(bg="red")
    elif (value < MAX_VALUE_LIGHT / 6 * 2):
        lblVeryLowLight.config(bg="green")
        lblLowLight.config(bg="red")
        lblNormalLight.config(bg="red")
        lblHighLight.config(bg="red")
        lblVeryHighLight.config(bg="red")
    elif(value < MAX_VALUE_LIGHT / 6 * 3):
        lblVeryLowLight.config(bg="green")
        lblLowLight.config(bg="green")
        lblNormalLight.config(bg="red")
        lblHighLight.config(bg="red")
        lblVeryHighLight.config(bg="red")
    elif(value < MAX_VALUE_LIGHT / 6 * 4):
        lblVeryLowLight.config(bg="green")
        lblLowLight.config(bg="green")
        lblNormalLight.config(bg="green")
        lblHighLight.config(bg="red")
        lblVeryHighLight.config(bg="red")
    elif(value < MAX_VALUE_LIGHT / 6 * 5):
        lblVeryLowLight.config(bg="green")
        lblLowLight.config(bg="green")
        lblNormalLight.config(bg="green")
        lblHighLight.config(bg="green")
        lblVeryHighLight.config(bg="red")
    else:
        lblVeryLowLight.config(bg="green")
        lblLowLight.config(bg="green")
        lblNormalLight.config(bg="green")
        lblHighLight.config(bg="green")
        lblVeryHighLight.config(bg="green")
    t = Timer(0.2, loop)
    t.start()
    
counter = 0
t = Timer(0.2, loop)
t.start()
window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() # Load the form 

