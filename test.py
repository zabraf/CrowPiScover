from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()
Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)
Button(fenetre, text ='Bouton 1').pack(side=LEFT, padx=42, pady=5)
Button(fenetre, text ='Bouton 2').pack(side=RIGHT, padx=5, pady=5)

fenetre.mainloop()
