from tkinter import *
from PIL import Image, ImageTk
import componentClass

class Main: 
    def DisplayButton(window, o):
        def Callback():
            o.Display()
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
        global imageTouchCaptor
        global imageUltraSound
        global imageVibrator

        imageBoutonPad = ImageTk.PhotoImage(file = r"images/boutonPad.jpg")
        imageBoutonsGrid = ImageTk.PhotoImage(file = r"images/boutonsGrille.jpg")
        imageBreadBoard = ImageTk.PhotoImage(file = r"images/BreadBoard.jpg")
        imageBreadBoardC = ImageTk.PhotoImage(file = r"images/BreadBoardC.jpg")
        imageBuzzer = ImageTk.PhotoImage(file = r"images/buzzer.jpg")
        imageHumidityCaptor = ImageTk.PhotoImage(file = r"images/capteurHumidite.jpg")
        imageDigitScreen = ImageTk.PhotoImage(file = r"images/ecranDigit.jpg")
        imageIR = ImageTk.PhotoImage(file = r"images/IR.jpg")
        imageLCD = ImageTk.PhotoImage(file = r"images/LCD.jpg")
        imageLedMatrix = ImageTk.PhotoImage(file = r"images/LedMatrix.jpg")
        imageLight = ImageTk.PhotoImage(file = r"images/light.jpg")
        imageMotion = ImageTk.PhotoImage(file = r"images/motion.jpg")
        imageRaspBerry = ImageTk.PhotoImage(file = r"images/RaspberryDessin.jpg")
        imageRFID = ImageTk.PhotoImage(file = r"images/RFID.jpg")
        imageSound = ImageTk.PhotoImage(file = r"images/sound.jpg")
        imageStepMotor = ImageTk.PhotoImage(file = r"images/stepMotor.jpg")
        imageTouchCaptor = ImageTk.PhotoImage(file = r"images/touchCaptor.jpg")
        imageUltraSound = ImageTk.PhotoImage(file = r"images/ultrason.jpg")
        imageVibrator = ImageTk.PhotoImage(file = r"images/vibreur.jpg")

        Button(window, command=Callback, borderwidth=0, image=imageRaspBerry).place(x=75, y=35)
        Button(window, command=Callback, borderwidth=0, image=imageBoutonPad).place(x=248, y=428)
        Button(window, command=Callback, borderwidth=0, image=imageBoutonsGrid).place(x=390, y=428)

        Button(window, command=Callback, borderwidth=0, image=imageBreadBoard).place(x=1000, y=1000)

        Button(window, command=Callback, borderwidth=0, image=imageBreadBoardC).place(x=580, y=428) #mon sac est fait
        Button(window, command=Callback, borderwidth=0, image=imageBuzzer).place(x=1000, y=1000)
        Button(window, command=Callback, borderwidth=0, image=imageHumidityCaptor).place(x=1000, y=1000)
        Button(window, command=Callback, borderwidth=0, image=imageDigitScreen).place(x=1000, y=1000)

        Button(window, command=Callback, borderwidth=0, image=imageIR).place(x=710, y=428) #mon sac est fait
        
        Button(window, command=Callback, borderwidth=0, image=imageLCD).place(x=1000, y=1000)
        Button(window, command=Callback, borderwidth=0, image=imageLedMatrix).place(x=1000, y=1000)
        Button(window, command=Callback, borderwidth=0, image=imageLight).place(x=1000, y=1000)
        Button(window, command=Callback, borderwidth=0, image=imageMotion).place(x=1000, y=1000)
        Button(window, command=Callback, borderwidth=0, image=imageRFID).place(x=1000, y=1000)
        Button(window, command=Callback, borderwidth=0, image=imageSound).place(x=1000, y=1000)

        Button(window, command=Callback, borderwidth=0, image=imageStepMotor).place(x=775, y=526) #

        Button(window, command=Callback, borderwidth=0, image=imageTouchCaptor).place(x=648, y=507) #mon sac est fait
        
        Button(window, command=Callback, borderwidth=0, image=imageUltraSound).place(x=1000, y=1000)
        Button(window, command=Callback, borderwidth=0, image=imageVibrator).place(x=1000, y=1000)
        return window
    
    root = Tk() # Main form
    bgImage = Image.open("images/CrowPiDessin.jpg") # Image background
    render = ImageTk.PhotoImage(bgImage) # Create a render of the background image

    lblImage = Label(root, image=render) # Create a label on the root form, the picture and the height
    lblImage.place(x=-1, y=-1) # Change the position of the label
    
    o = componentClass.Component() # Intialize the function in another file
    root = DisplayButton(root, o) # Call the display button method

    root.attributes("-fullscreen", True) # Resize the form in fullscreen
    root.mainloop() # Load the form
    

 
