# Créé par Hana, le 10/03/2022 en Python 3.7

# Import module
from tkinter import *
from winsound import *
import io
import os
from random import randint, shuffle
import subprocess
from random import *





# Create object
fenetre1 = Tk()


fenetre1.geometry("400x350")                            # définie  les dimensions de la fenetre
fenetre1.title("Netry - © 2022 Hana")           # définie le titre de la fenetre



icon=PhotoImage(file="logo.png")
fenetre1.iconphoto(True,icon)

# Add image file
bg = PhotoImage(file = "menue1.png")

# Show image using label
label1 = Label( fenetre1, image = bg)
label1.place(x = -2, y = -2)

test = 0
memorax=0
# Create Frame

def SuperNetry():
    import NetryBros1

def MemoryNetry():
    import NetryMemory

def NetryJunken():
    import junkenNetry


def NetryMineur():
    import NetryMineur

def NetryEchec():
    import main


def reeturn():


    fenetre1.title("Netry - © 2022 Hana")           # définie le titre de la fenetre
    bg2 = PhotoImage(file = "menue1.png")
    label8 = Label( fenetre1, image = bg2)
    label8.place(x = 0, y = 0)
    label8.img=bg2
    label8.pack()

    button10 = Button(text="Start", font="Andalus",bd=4, width=14,command=lambda: [start1(),button10.destroy(), button11.destroy(), button13.destroy(),label8.destroy()])
    button10.pack(pady = 5)
    button10.place(x = 125, y = 165)


    button11 = Button(fenetre1,  text = "Credits", font="Andalus",bd=4, width=14,command=lambda: [credits1(),label8.destroy(),button10.destroy(), button11.destroy(), button13.destroy()])
    button11.pack(pady=5)
    button11.place(x = 125, y = 215)

    button13 = Button(  text = "Exit", font="Andalus",bd=4, width=14, command=fenetre1.destroy)
    button13.pack(pady = 5)
    button13.place(x = 125, y = 265)
    fenetre1.destroy





def credits1():
    global test
    n = randint(1,5)
    if n==3 :
        credits5 = PhotoImage(file = "main1.png")
    else :
        credits5 = PhotoImage(file = "creditss.png")

    fenetre1.title("Netry Credits - © 2022 Hana")          # définie le titre de la fenetre

    label2 = Label( fenetre1, image = credits5)
    label2.place(x = 0, y = 0)
    label2.img=credits5
    label2.pack()
    button4 = Button(  text = "Return", font="Andalus",bd=4, width=6, command=lambda: [reeturn(),button4.destroy(),label2.destroy()])
    button4.pack(pady = 5)
    button4.place(x = 165, y = 305)
    test+=0


def Bonus():

    v = randint(1,5)
    if v==2 :
        start5 = PhotoImage(file = "main2.png")
    else :
        start5 = PhotoImage(file = "menue1.png")
    fenetre1.title("Netry Games - © 2022 Hana")          # définie le titre de la fenetre

    label3 = Label( fenetre1, image = start5)
    label3.place(x = 0, y = 0)
    label3.img=start5
    label3.pack()

    button6 = Button(fenetre1,  text = "Netry Memory", font="Andalus",bd=4, width=14, command=lambda: [fenetre1.destroy(), MemoryNetry()])
    button6.pack(pady=5)
    button6.place(x = 125, y = 140)

    button7 = Button(  text = "Netry Janken", font="Andalus",bd=4, width=14, command=lambda: [fenetre1.destroy(), NetryJunken()])
    button7.pack(pady = 5)
    button7.place(x = 125, y = 180)

    button8 = Button(  text = "Netry Miner", font="Andalus",bd=4, width=14, command=lambda: [fenetre1.destroy(), NetryMineur()])
    button8.pack(pady = 5)
    button8.place(x = 125, y = 220)

    button9 = Button(  text = "Netry Chess", font="Andalus",bd=4, width=14, command=lambda: [fenetre1.destroy(), NetryEchec()])
    button9.pack(pady = 5)
    button9.place(x = 125, y = 260)

    button12 = Button(  text = "Return", font="Andalus",bd=4, width=6, command=lambda: [start1(),button6.destroy(), button7.destroy(), button12.destroy(),label3.destroy()] )
    button12.pack(pady = 5)
    button12.place(x = 165, y = 305)


def start1():
    v = randint(1,5)
    if v==2 :
        start5 = PhotoImage(file = "main2.png")
    else :
        start5 = PhotoImage(file = "menue1.png")
    fenetre1.title("Netry Games - © 2022 Hana")          # définie le titre de la fenetre

    label3 = Label( fenetre1, image = start5)
    label3.place(x = 0, y = 0)
    label3.img=start5
    label3.pack()

    button5 = Button(fenetre1,text="Super Netry Bros", font="Andalus",bd=4, width=14, command=lambda: [fenetre1.destroy(), SuperNetry()])
    button5.pack(pady = 5)
    button5.place(x = 125, y = 165)

    button11 = Button(  text = "Bonus Game", font="Andalus",bd=4, width=14, command=lambda: [Bonus(), button5.destroy(),button8.destroy(),button11.destroy(),label3.destroy()])
    button11.pack(pady = 5)
    button11.place(x = 125, y = 235)

    button8 = Button(  text = "Return", font="Andalus",bd=4, width=6, command=lambda: [reeturn(),button5.destroy(), button11.destroy(), button8.destroy(),label3.destroy() ] )
    button8.pack(pady = 5)
    button8.place(x = 165, y = 305)




# Add buttons
button1 = Button(text="Start", font="Andalus",bd=4, width=14,command=start1)
button1.pack(pady = 5)
button1.place(x = 125, y = 165)


button2 = Button(fenetre1,  text = "Credits", font="Andalus",bd=4, width=14,command=credits1)
button2.pack(pady=5)
button2.place(x = 125, y = 215)


def bye():
    l = randint(1,10)
    if l==5 :
        import Netrybye

button3 = Button(  text = "Exit", font="Andalus",bd=4, width=14, command=lambda: [fenetre1.destroy(), bye()])
button3.pack(pady = 5)
button3.place(x = 125, y = 265)



# Execute tkinter
fenetre1.mainloop()
