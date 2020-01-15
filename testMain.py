from tkinter import *
from tkinter import messagebox
import tkinter as tk
import testClass
from PIL import Image, ImageTk
from pynput import mouse

class Main: 
    def DisplayButton(window, o):
        label = Label(window, text="Hello World")
        label.pack()
        def Callback():
            o.Display()
        #Canvas(window, width=1024, height=600, bg='red').pack(side=TOP, padx=5, pady=5)
        Button(window, text ='Display', command=Callback, borderwidth=0).place(x=100, y=100)
        Button(window, text ='Quit', command=window.destroy, borderwidth=0).place(x=1500, y=1000)
        return window
    
    def OnClick(x, y, button, pressed):
        if pressed: # If the mouse click is pressed
            messagebox.showinfo("title", "{0}{1}".format('pressed' if pressed else null, (x,y))) # Display a messageBox containing the x and y of the mouse
            if x < 50 and x > 0 and y < 50 and y > 0: # If clicked in a zone.
                messagebox.showinfo("title", "{0}{1}".format('YOS' if pressed else null, (x,y)))
    

    root = Tk() # Main form
    bgImage = Image.open("city_sun_sunset_143693_1920x1080.jpg") # Image background
    render = ImageTk.PhotoImage(bgImage) # Create a render of the background image

    listener = mouse.Listener( # Create an event of the mouse click
        on_click=OnClick
    )
    listener.start() # Start the listener

    lblImage = Label(root, image=render, height=1000) # Create a label on the root form, the picture and the height
    lblImage.place(x=-1, y=-1) # Change the position of the label
    
    txtZone = tk.Text(root, height=20, width=100)
    txtZone.pack()
    quote = """Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker. """

    txtZone.insert(tk.END, quote)
    o = testClass.TestObject() # Intialize the function in another file
    root = DisplayButton(root, o) # Call the display button method
    root.attributes("-fullscreen", True) # Resize the form in fullscreen
    root.mainloop() # Load the form
    

  
