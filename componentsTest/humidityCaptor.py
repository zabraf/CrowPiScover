#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sys
import Adafruit_DHT
import time
from threading import Timer

# set type of the sensor
sensor = 11
# set pin number
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
def loop():
    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    t = Timer(0.1, loop)
    t.start()
counter = 0
t = Timer(0.1, loop)
t.start()

def app_lost_focus(event):
    t.cancel()
    exit()
    
def on_closing():
    t.cancel()
    exit()
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
window = Tk() # Main form
window.geometry("400x200+400+100")

lblTemperature = Label(window, text="Température : ", font=("Courier", 20))
lblHumidity = Label(window, text="Humidité : ", font=("Courier", 20))

lblTemperature.place(x=10, y=50)
lblHumidity.place(x=10, y=80)

window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop() # Load the form 

