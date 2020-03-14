#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

serial = spi(port=0, device=1, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)

def ExecuteExemple():
    msg = "Hello World"
    show_message(device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)

def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("400x200+300+200")
Button(window, command= lambda: ExecuteExemple(), bg="green", activebackground="darkgreen", width="17", height="5").place(x=100, y=50)
window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 



