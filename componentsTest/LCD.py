#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import Adafruit_CharLCD as LCD

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

def ExecuteExemple():
    lcd.set_backlight(0)
    message = 'Hello\nworld!'
    lcd.message(message)
    #for i in range(lcd_columns-len(message)):
        #time.sleep(0.5)
        #lcd.move_right()
    #for i in range(lcd_columns-len(message)):
        #time.sleep(0.5)
        #lcd.move_left()
    time.sleep(5.0)
    lcd.clear()
    lcd.set_backlight(1)

def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("400x200+300+200")
Button(window, command= lambda: ExecuteExemple(), bg="green", activebackground="darkgreen", width="17", height="5").place(x=100, y=50)
window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 

