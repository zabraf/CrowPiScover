from tkinter import *
from PIL import Image, ImageTk
import json

class Component:
    def Display(self, componentName):
        componentWindow = Toplevel() 

        bgImage = ImageTk.PhotoImage(Image.open("images/CrowPiDessin.jpg")) # Create a render of the background image

        lblImage = Label(componentWindow, image=bgImage) # Create a label on the root form, the picture and the height
        lblImage.place(x=-1, y=-1) # Change the position of the label

        Button(componentWindow, text ='Go Back', command=componentWindow.destroy).place(x=475, y=50)

        #Get the jsonfile Datas
        with open('componentsData.txt') as json_file:
            data = json.load(json_file)
            dataString = ""
            for i in data:#Go through all the components
                if i == componentName:  #If it reachs the searched component
                    component = data[componentName] #Go through a component datas
                    #Display what is needed
                    lblName = Label(componentWindow, text=component['Name'], font=("courrier", 25))
                    lblName.place(x=30, y=50)
                    
                    lblDescription = Label(componentWindow, text=component['Description'], font=("courrier", 12), wraplength=300)
                    lblDescription.place(x=30, y=100)
                    
                    lblFunctionnementTitle = Label(componentWindow, text="Fonctionnement", font=("courrier", 25))
                    lblFunctionnementTitle.place(x=725, y=50)

                    lblFunctionnement = Label(componentWindow, text=component['Functionnement'], font=("courrier", 12))
                    lblFunctionnement.place(x=725, y=100)
                   
                    global componentImage
                    componentImage = ImageTk.PhotoImage(file = r"images/boutonPad.jpg")
                    lblImage = Label(componentWindow, image=componentImage) # Create a label on the root form, the picture and the height
                    lblImage.place(x=480, y=250) # Change the position of the label

                    Button(componentWindow, text ='Go Back', command=componentWindow.destroy).place(x=475, y=50)

                    lblPins = Label(componentWindow, text=component['Pins'], font=("courrier", 20)) #Should be a picture
                    lblPins.place(x=480, y=450)

                    Button(componentWindow, text ='Test/Description technique', command=componentWindow.destroy).place(x=450, y=500)
        componentWindow.attributes("-fullscreen", True) 
        componentWindow.mainloop()
