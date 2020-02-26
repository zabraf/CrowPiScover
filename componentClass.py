from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json, os

class Component:
    def Display(self, componentName):
        componentWindow = Toplevel() 
        componentWindow.configure(background='white')
        
        def ExecuteScript(script):
            os.system("python3.8 "+script)

        Button(componentWindow, text ='Go Back', command=componentWindow.destroy).place(x=510, y=50)
        
        #Get the jsonfile Datas
        with open('componentsData.txt') as json_file:
            data = json.load(json_file)
            dataString = ""
            for i in data:#Go through all the components
                if i == componentName:  #If it reachs the searched component
                    component = data[componentName] #Go through a component datas
                    #Display the componenent name
                    lblName = Label(componentWindow, text=component['Name'], font=("courrier", 25))
                    lblName.place(x=30, y=50)
                    
                    #Display the description of the component
                    lblDescription = Label(componentWindow, text=component['Description'], font=("courrier", 12), wraplength=300)
                    lblDescription.place(x=30, y=100)
                    
                    #Display "Fonctionnement"
                    lblFunctionnementTitle = Label(componentWindow, text="Fonctionnement", font=("courrier", 25))
                    lblFunctionnementTitle.place(x=725, y=50)

                    #Display the componenent functionnement
                    lblFunctionnement = Label(componentWindow, text=component['Functionnement'], font=("courrier", 12))
                    lblFunctionnement.place(x=725, y=100)
                   
                    #Display the picture of the element
                    global componentImage
                    componentImage = ImageTk.PhotoImage(file = r"images/"+component['ImageLink'])
                    lblImage = Label(componentWindow, image=componentImage) # Create a label on the root form, the picture and the height
                    lblImage.place(x = 450 + component['ImageX'], y = 250 + component['ImageY']) # Change the position of the label

                    #Display the pins image/value
                    lblPins = Label(componentWindow, text=component['Pins'], font=("courrier", 20)) #Should be a picture
                    lblPins.place(x = 490, y = 450)
                    
                    #Display Test componenent button
                    Button(componentWindow, text ='Test/Description technique', command= lambda: ExecuteScript("componentsTest/"+component['TestLink'])).place(x=458, y=500)
        componentWindow.attributes("-fullscreen", True) 
        componentWindow.mainloop()
