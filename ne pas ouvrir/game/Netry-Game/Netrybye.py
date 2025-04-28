# Créé par Hana, le 13/03/2022 en Python 3.7

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
fenetre1.title("Bye Netry - © 2022 Hana")           # définie le titre de la fenetre

icon=PhotoImage(file="logo.png")
fenetre1.iconphoto(True,icon)
# Add image file
bg = PhotoImage(file = "part1.png")

# Show image using label
label1 = Label( fenetre1, image = bg)
label1.place(x = -2, y = -2)


# Create Frame


button1 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button1.destroy(), bye1()] )
button1.pack(pady = 5)
button1.place(x = 165, y = 310)



def bye1():

    part = PhotoImage(file = "part2.png")
    fenetre1.title(" Bye bye Netry - © 2022 Hana")          # définie le titre de la fenetre
    label2 = Label( fenetre1, image = part)
    label2.place(x = 0, y = 0)
    label2.img=part
    label2.pack()
    button2 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button2.destroy(),label2.destroy(),bye2()])
    button2.pack(pady = 5)
    button2.place(x = 165, y = 310)



def bye2():

    part1 = PhotoImage(file = "part3.png")
    fenetre1.title(" Goodbye Netry - © 2022 Hana")          # définie le titre de la fenetre
    label3 = Label( fenetre1, image = part1)
    label3.place(x = 0, y = 0)
    label3.img=part1
    label3.pack()
    button3 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button3.destroy(),label3.destroy(),bye3()])
    button3.pack(pady = 5)
    button3.place(x = 165, y = 310)


def bye3():

    part2 = PhotoImage(file = "part4.png")
    fenetre1.title(" Farewell Netry - © 2022 Hana")          # définie le titre de la fenetre
    label4 = Label( fenetre1, image = part2)
    label4.place(x = 0, y = 0)
    label4.img=part2
    label4.pack()
    button4 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button4.destroy(),label4.destroy(),bye4()])
    button4.pack(pady = 5)
    button4.place(x = 165, y = 310)

def bye4():

    part3 = PhotoImage(file = "part5.png")
    fenetre1.title(" Ciao Netry - © 2022 Hana")          # définie le titre de la fenetre
    label5 = Label( fenetre1, image = part3)
    label5.place(x = 0, y = 0)
    label5.img=part3
    label5.pack()
    button5 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button5.destroy(),label5.destroy(), bye5()])
    button5.pack(pady = 5)
    button5.place(x = 165, y = 310)


def bye5():

    part4 = PhotoImage(file = "part6.png")
    fenetre1.title(" See you Netry - © 2022 Hana")          # définie le titre de la fenetre
    label6 = Label( fenetre1, image = part4)
    label6.place(x = 0, y = 0)
    label6.img=part4
    label6.pack()
    button6 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button6.destroy(),label6.destroy(),bye6()])
    button6.pack(pady = 5)
    button6.place(x = 165, y = 310)

def bye6():

    part5 = PhotoImage(file = "part7.png")
    fenetre1.title(" Later Netry - © 2022 Hana")          # définie le titre de la fenetre
    label7 = Label( fenetre1, image = part5)
    label7.place(x = 0, y = 0)
    label7.img=part5
    label7.pack()
    button7 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button7.destroy(),label7.destroy(),bye7()])
    button7.pack(pady = 5)
    button7.place(x = 165, y = 310)

def bye7():

    part5 = PhotoImage(file = "part8.png")
    fenetre1.title(" Smell you later Netry - © 2022 Hana")          # définie le titre de la fenetre
    label7 = Label( fenetre1, image = part5)
    label7.place(x = 0, y = 0)
    label7.img=part5
    label7.pack()
    button7 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button7.destroy(),label7.destroy(), bye8()])
    button7.pack(pady = 5)
    button7.place(x = 165, y = 310)

def bye8():

    part5 = PhotoImage(file = "part9.png")
    fenetre1.title(" Adios Netry - © 2022 Hana")          # définie le titre de la fenetre
    label7 = Label( fenetre1, image = part5)
    label7.place(x = 0, y = 0)
    label7.img=part5
    label7.pack()
    button7 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button7.destroy(),label7.destroy(),bye9()])
    button7.pack(pady = 5)
    button7.place(x = 165, y = 310)

def bye9():

    part5 = PhotoImage(file = "part10.png")
    fenetre1.title(" Au revoir Netry - © 2022 Hana")          # définie le titre de la fenetre
    label7 = Label( fenetre1, image = part5)
    label7.place(x = 0, y = 0)
    label7.img=part5
    label7.pack()
    button7 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [button7.destroy(),label7.destroy(),bye10()])
    button7.pack(pady = 5)
    button7.place(x = 165, y = 310)


def bye10():

    part5 = PhotoImage(file = "part11.png")
    fenetre1.title(" Sayonara Netry - © 2022 Hana")          # définie le titre de la fenetre
    label7 = Label( fenetre1, image = part5)
    label7.place(x = 0, y = 0)
    label7.img=part5
    label7.pack()
    button7 = Button(  text = "Exit", font="Andalus",bd=4, width=6, command=lambda: [fenetre1.destroy()])
    button7.pack(pady = 5)
    button7.place(x = 165, y = 310)




# Execute tkinter
fenetre1.mainloop()
