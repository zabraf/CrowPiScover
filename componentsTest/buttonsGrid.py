#!/usr/bin/python3 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import RPi.GPIO as GPIO
from threading import Timer

class ButtonMatrix():

    def __init__(self):

        GPIO.setmode(GPIO.BOARD)

        # matrix button ids
        self.buttonIDs = [[4,3,2,1],[8,7,6,5],[12,11,10,9],[16,15,14,13]]
        # gpio inputs for rows
        self.rowPins = [13,15,29,31]
        # gpio outputs for columns
        self.columnPins = [33,35,37,22]

        # gpio outputs for columns
        self.columnPins = [33,35,37,22]

        # define four inputs with pull up resistor
        for i in range(len(self.rowPins)):
            GPIO.setup(self.rowPins[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

        # define four outputs and set to high
        for j in range(len(self.columnPins)):
            GPIO.setup(self.columnPins[j], GPIO.OUT)
            GPIO.output(self.columnPins[j], 1)

    def activateButton(self, rowPin, colPin):
        # get the button index
        btnIndex = self.buttonIDs[rowPin][colPin] - 1
        lblValeur.config(text="bouton " + str(btnIndex))

def app_lost_focus(event):
    t.cancel()
    exit()
    
def on_closing():
    t.cancel()
    exit()

window = Tk() # Main form
window.geometry("400x300+400+100")
lblText = Label(window, text="Dernier Bouton appuyé : ", font=("Courier", 20))
lblText.place(x=10, y=50)
lblValeur = Label(window, text="", font=("Courier", 20))
lblValeur.place(x=10, y=80)
# Call SoundDetected when there's sound
# Call NoSoundDetected after SoundDetected to reset the label
window.bind("<FocusOut>", app_lost_focus)
window.protocol("WM_DELETE_WINDOW", on_closing)
buttons = ButtonMatrix()
def loop():
    for j in range(len(buttons.columnPins)):
                # set each output pin to low
                GPIO.output(buttons.columnPins[j],0)
                for i in range(len(buttons.rowPins)):
                    if GPIO.input(buttons.rowPins[i]) == 0:
                        # button pressed, activate it
                        buttons.activateButton(i,j)
                # return each output pin to high
                GPIO.output(buttons.columnPins[j],1)
    t = Timer(0.1, loop)
    t.start()
t = Timer(0.1, loop)
t.start()
window.mainloop() # Load the form
    








