# Créé par Hana, le 20/03/2022 en Python 3.7

# Import module
from tkinter import *
from winsound import *
import io
import os
from random import randint, shuffle
import subprocess
from random import *
import tkinter.font as font

# Create object
fenetre1 = Tk()


fenetre1.geometry("400x350")                            # définie  les dimensions de la fenetre
fenetre1.title("Super Netry Bros  - © 2022 Hana")           # définie le titre de la fenetre


icon=PhotoImage(file="logo.png")
fenetre1.iconphoto(True,icon)
bg = PhotoImage(file = "map1.png")

# Show image using label
label1 = Label( fenetre1, image = bg)
label1.place(x = -2, y = -2)

f = font.Font(size=9)


def NetryBros():
    import NetryBros2


button2 = Button(fenetre1,  text = "let's go", font="Andalus" ,bd=2, width=5, command=lambda: [fenetre1.destroy(), NetryBros()])
button2['font'] = f
button2.pack(pady=5)
button2.place(x = 121, y = 108)


def bye():
    l = randint(1,10)
    if l==5 :
        import Netrybye

button3 = Button(  text = "Exit", font="Andalus",bd=4, width=5, command=lambda: [fenetre1.destroy(), bye()])
button3.pack(pady = 5)
button3.place(x = 168, y = 310)



# Execute tkinter
fenetre1.mainloop()

