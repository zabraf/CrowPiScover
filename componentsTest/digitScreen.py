#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment(address=0x70)
from Adafruit_LED_Backpack import SevenSegment

# Initialize the display. Must be called once before using the display.
segment.begin()

def ExecuteExemple():
    number = 0
    while (number <= 20):
        segment.clear()
        segment.set_digit(0, 0)     
        segment.set_digit(1, 0)          
        # Set minutes
        segment.set_digit(2, int(number / 10))   
        segment.set_digit(3, int(number % 10))        
        number += 1
        segment.set_colon(number % 2)  
        segment.write_display()
        # Wait a quarter second (less than 1 second to prevent colon blinking getting$
        time.sleep(0.25)
    segment.clear()
    segment.write_display()

def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("400x200+300+200")
Button(window, command= lambda: ExecuteExemple(), bg="green", activebackground="darkgreen", width="17", height="5").place(x=100, y=50)
window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 


