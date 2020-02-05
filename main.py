#!/usr/bin/python3
from tkinter import *
from PIL import Image, ImageTk
import componentClass

class Main: 
    def DisplayButton(window, o):
        def Callback(component):
            o.Display(component)
        # Garbage collector delete it, if it's not global.
        global imageBoutonPad
        global imageBoutonsGrid
        global imageBreadBoard
        global imageBreadBoardC
        global imageBuzzer
        global imageHumidityCaptor
        global imageDigitScreen
        global imageIR
        global imageLCD
        global imageLedMatrix
        global imageLight
        global imageMotion
        global imageRaspBerry
        global imageRFID
        global imageSound
        global imageStepMotor
        global imageServ
        global imageTouchCaptor
        global imageUltraSound
        global imageVibrator

        imageBoutonPad = ImageTk.PhotoImage(file = r"images/ButtonsPad.jpg")
        imageBoutonsGrid = ImageTk.PhotoImage(file = r"images/ButtonsGrid.jpg")
        imageBreadBoard = ImageTk.PhotoImage(file = r"images/BreadBoard.jpg")
        imageBreadBoardC = ImageTk.PhotoImage(file = r"images/BreadBoardC.jpg")
        imageBuzzer = ImageTk.PhotoImage(file = r"images/Buzzer.jpg")
        imageHumidityCaptor = ImageTk.PhotoImage(file = r"images/HumidityCaptor.jpg")
        imageDigitScreen = ImageTk.PhotoImage(file = r"images/DigitScreen.jpg")
        imageIR = ImageTk.PhotoImage(file = r"images/IR.jpg")
        imageLCD = ImageTk.PhotoImage(file = r"images/LCD.jpg")
        imageLedMatrix = ImageTk.PhotoImage(file = r"images/LedMatrix.jpg")
        imageLight = ImageTk.PhotoImage(file = r"images/Light.jpg")
        imageMotion = ImageTk.PhotoImage(file = r"images/Motion.jpg")
        imageRaspBerry = ImageTk.PhotoImage(file = r"images/Raspberry.jpg")
        imageRFID = ImageTk.PhotoImage(file = r"images/RFID.jpg")
        imageSound = ImageTk.PhotoImage(file = r"images/Sound.jpg")
        imageStepMotor = ImageTk.PhotoImage(file = r"images/StepMotor.jpg")
        imageServ = ImageTk.PhotoImage(file = r"images/Sever.jpg")
        imageTouchCaptor = ImageTk.PhotoImage(file = r"images/TouchCaptor.jpg")
        imageUltraSound = ImageTk.PhotoImage(file = r"images/Ultrasound.jpg")
        imageVibrator = ImageTk.PhotoImage(file = r"images/Vibrator.jpg")

        Button(window, command= lambda: Callback("Raspberry"), borderwidth=0, image=imageRaspBerry).place(x=75, y=35)
        Button(window, command= lambda: Callback("BoutonPad"), borderwidth=0, image=imageBoutonPad).place(x=248, y=428)
        Button(window, command= lambda: Callback("ButtonsGrid"), borderwidth=0, image=imageBoutonsGrid).place(x=390, y=428)
        Button(window, command= lambda: Callback("BreadBoard"), borderwidth=0, image=imageBreadBoard).place(x=455, y=173)
        Button(window, command= lambda: Callback("BreadBoardC"), borderwidth=0, image=imageBreadBoardC).place(x=580, y=428)
        Button(window, command= lambda: Callback("Buzzer"), borderwidth=0, image=imageBuzzer).place(x=892, y=314)
        Button(window, command= lambda: Callback("HumidityCaptor"), borderwidth=0, image=imageHumidityCaptor).place(x=648, y=428)
        Button(window, command= lambda: Callback("DigitScreen"), borderwidth=0, image=imageDigitScreen).place(x=775, y=173)
        Button(window, command= lambda: Callback("IR"), borderwidth=0, image=imageIR).place(x=710, y=428)
        Button(window, command= lambda: Callback("LCD"), borderwidth=0, image=imageLCD).place(x=456, y=38)
        Button(window, command= lambda: Callback("LedMatrix"), borderwidth=0, image=imageLedMatrix).place(x=618, y=173)
        Button(window, command= lambda: Callback("Light"), borderwidth=0, image=imageLight).place(x=775, y=316)
        Button(window, command= lambda: Callback("Motion"), borderwidth=0, image=imageMotion).place(x=775, y=392)
        Button(window, command= lambda: Callback("RFID"), borderwidth=0, image=imageRFID).place(x=88, y=408)
        Button(window, command= lambda: Callback("Sound"), borderwidth=0, image=imageSound).place(x=775, y=355)
        Button(window, command= lambda: Callback("StepMotor"), borderwidth=0, image=imageStepMotor).place(x=775, y=526)
        Button(window, command= lambda: Callback("Sever"), borderwidth=0, image=imageServ).place(x=865, y=526)
        Button(window, command= lambda: Callback("TouchCaptor"), borderwidth=0, image=imageTouchCaptor).place(x=648, y=507)
        Button(window, command= lambda: Callback("Ultrasound"), borderwidth=0, image=imageUltraSound).place(x=775, y=450)
        Button(window, command= lambda: Callback("Vibrator"), borderwidth=0, image=imageVibrator).place(x=775, y=245)
        return window
    
    root = Tk() # Main form
    bgImage = Image.open("images/CrowPiBG.jpg") # Image background
    render = ImageTk.PhotoImage(bgImage) # Create a render of the background image

    lblImage = Label(root, image=render) # Create a label on the root form, the picture and the height
    lblImage.place(x=-1, y=-1) # Change the position of the label
    
    o = componentClass.Component() # Intialize the function in another file
    root = DisplayButton(root, o) # Call the display button method

    root.attributes("-fullscreen", True) # Resize the form in fullscreen
    root.mainloop() # Load the form 
