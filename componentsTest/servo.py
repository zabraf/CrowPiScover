#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import RPi.GPIO as GPIO
import time
import sys

class sg90:

  def __init__( self, direction):

    self.pin = 25
    GPIO.setmode( GPIO.BCM )
    GPIO.setup( self.pin, GPIO.OUT )
    self.direction = int( direction )
    self.servo = GPIO.PWM( self.pin, 50 )
    self.servo.start(0.0)

  def cleanup( self ):

    self.servo.ChangeDutyCycle(self._henkan(0))
    time.sleep(0.3)
    self.servo.stop()
    GPIO.cleanup()

  def currentdirection( self ):

    return self.direction

  def _henkan( self, value ):

    return 0.05 * value + 7.0

  def setdirection( self, direction, speed ):

    for d in range( self.direction, direction, int(speed) ):
      self.servo.ChangeDutyCycle( self._henkan( d ) )
      self.direction = d
      time.sleep(0.1)
    self.servo.ChangeDutyCycle( self._henkan( direction ) )
    self.direction = direction
s = sg90(0)
def ExecuteExemple():
    s.setdirection( 100, 80 )
    time.sleep(0.5)
    s.setdirection( -100, 80 )

def app_lost_focus(event): 
    exit()
   
window = Tk() # Main form
window.geometry("400x200+300+200")
Button(window, command= lambda: ExecuteExemple(), bg="green", activebackground="darkgreen", width="17", height="5").place(x=100, y=50)
window.bind("<FocusOut>", app_lost_focus)
window.mainloop() # Load the form 


