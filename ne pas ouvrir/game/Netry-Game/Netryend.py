# Créé par Hana, le 25/03/2022 en Python 3.7
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

bg = PhotoImage(file = "netryend2.png")

icon=PhotoImage(file="logo.png")
fenetre1.iconphoto(True,icon)


# Show image using label
label1 = Label( fenetre1, image = bg)
label1.place(x = -2, y = -2)

f = font.Font(size=9)


bg2 = PhotoImage(file = "netryend2.png")


def test3():
    bg3 = PhotoImage(file = "comics.png")
    label9 = Label( fenetre1, image = bg3)
    label9.place(x = 0, y = 0)
    label9.img=bg3
    label9.pack()

fenetre1.after(4000, test3)


def bye():
    l = randint(1,10)
    if l==5 :
        import Netrybye


def test2():
    button3 = Button(  text = "Exit", font="Andalus",bd=2, width=5, command=lambda: [fenetre1.destroy(), bye()])
    button3.pack(pady = 5)
    button3.place(x = 170, y = 267)

fenetre1.after(6000, test2)

# Execute tkinter
fenetre1.mainloop()

