# Créé par Hana, le 19/03/2022 en Python 3.7
# Créé par Hana, le 19/02/2022 en Python 3.7
''' programme jeu mario avec cibles et carapace, décors en mouvement avec nuages,
insertion de colision pour les cibles et carapace et mouvement des cibles,
score personalisé qui augmente a chaque cibles'''



from tkinter import *
from winsound import *

def jouerPartie():

    c1.move(decor, -10, 0)                             # déplacer le décor à la position x

    c1.move(trans, -10, 0)
    c1.move(trans2, -10, 0)

    c1.move(carapace, -29, 0 )
    c1.move(carapace2, -29, 0 )
    c1.move(carapace3, -29, 0 )
    c1.move(carapace4, -29, 0 )
    c1.move(carapace5, -29, 0 )

    c1.move(carapace6, -29, 0 )
    c1.move(carapace7, -29, 0 )
    c1.move(carapace8, -29, 0 )
    c1.move(carapace9, -29, 0 )
    c1.move(carapace10, -29, 0 )

    c1.move(boss, -29, 0 )

    c1.move(cible1, -20, 0)
    c1.move(cible2, -20, 0)
    c1.move(cible3, -20, 0)
    c1.move(cible4, -20, 0)
    c1.move(cible5, -20, 0)
    c1.move(cible6, -20, 0)
    c1.move(cible7, -20, 0)
    c1.move(cible8, -20, 0)
    c1.move(cible9, -20, 0)
    c1.move(cible10, -20, 0)
    c1.move(cible11, -20, 0)
    c1.move(cible12, -20, 0)
    c1.move(cible13, -20, 0)
    c1.move(cible14, -20, 0)
    c1.move(cible15, -20, 0)
    c1.move(cible16, -20, 0)
    c1.move(cible17, -20, 0)

    c1.move(cible18, -20, 0)
    c1.move(cible19, -20, 0)
    c1.move(cible20, -20, 0)
    c1.move(cible21, -20, 0)
    c1.move(cible22, -20, 0)
    c1.move(cible23, -20, 0)
    c1.move(cible24, -20, 0)
    c1.move(cible25, -20, 0)
    c1.move(cible26, -20, 0)
    c1.move(cible27, -20, 0)
    c1.move(cible28, -20, 0)
    c1.move(cible29, -20, 0)
    c1.move(cible30, -20, 0)

    c1.move(coeur, -20, 0)

    c1.move(epee, -20, 0)

    c1.move(fin1, -20, 0)
    c1.move(fin2, -20, 0)
    c1.move(chateau, -20, 0)



    print("Voilà c'est à vous de jouer maintenant!")   # affiche Voilà c'est à vous de jouer maintenant! dans la onsole python
    fenetre.after( 133, jouerPartie )                  # actualiser l'affichage toutes les 0,133s convient car cela crée une illusion du mouvement de l'image cela permet d'observer un mouvement continu alors qu'il ne l'est pas

    gererCollision(mario1,cible1)                        # exécuter la fonction gererCollision
    gererCollision(mario2,cible1)
    gererCollision(mario1,cible2)
    gererCollision(mario2,cible2)
    gererCollision(mario1,cible3)
    gererCollision(mario2,cible3)
    gererCollision(mario1,cible4)
    gererCollision(mario2,cible4)
    gererCollision(mario1,cible5)
    gererCollision(mario2,cible5)
    gererCollision(mario1,cible6)
    gererCollision(mario2,cible6)
    gererCollision(mario1,cible7)
    gererCollision(mario2,cible7)
    gererCollision(mario1,cible8)
    gererCollision(mario2,cible8)
    gererCollision(mario1,cible9)
    gererCollision(mario2,cible9)
    gererCollision(mario1,cible10)
    gererCollision(mario2,cible10)
    gererCollision(mario1,cible11)
    gererCollision(mario2,cible11)
    gererCollision(mario1,cible12)
    gererCollision(mario2,cible12)
    gererCollision(mario1,cible13)
    gererCollision(mario2,cible13)
    gererCollision(mario1,cible14)
    gererCollision(mario2,cible14)
    gererCollision(mario1,cible15)
    gererCollision(mario2,cible15)
    gererCollision(mario1,cible16)
    gererCollision(mario2,cible16)
    gererCollision(mario1,cible17)
    gererCollision(mario2,cible17)

    gererCollision(mario1,cible18)                        # exécuter la fonction gererCollision
    gererCollision(mario2,cible18)
    gererCollision(mario1,cible19)
    gererCollision(mario2,cible19)
    gererCollision(mario1,cible20)
    gererCollision(mario2,cible20)
    gererCollision(mario1,cible21)
    gererCollision(mario2,cible21)
    gererCollision(mario1,cible22)
    gererCollision(mario2,cible22)
    gererCollision(mario1,cible23)
    gererCollision(mario2,cible23)
    gererCollision(mario1,cible24)
    gererCollision(mario2,cible24)
    gererCollision(mario1,cible25)
    gererCollision(mario2,cible25)
    gererCollision(mario1,cible26)
    gererCollision(mario2,cible26)
    gererCollision(mario1,cible27)
    gererCollision(mario2,cible27)
    gererCollision(mario1,cible28)
    gererCollision(mario2,cible28)
    gererCollision(mario1,cible29)
    gererCollision(mario2,cible29)
    gererCollision(mario1,cible30)
    gererCollision(mario2,cible30)

    Carapace2(mario1,carapace)

    Carapace2(mario1,carapace2)

    Carapace2(mario1,carapace3)

    Carapace2(mario1,carapace4)

    Carapace2(mario1,carapace5)

    Carapace2(mario1,carapace6)

    Carapace2(mario1,carapace7)

    Carapace2(mario1,carapace8)

    Carapace2(mario1,carapace9)

    Carapace2(mario1,carapace10)

    Epee(mario1, epee)
    Epee(mario2, epee)

    Boss(mario3, boss)
    Boss(mario4, boss)
    Boss(mario1, boss)
    Boss(mario2, boss)


    Fin(mario1,chateau)
    Fin(mario2,chateau)

    CollisionCoeur(mario1,coeur)
    CollisionCoeur(mario2,coeur)


fenetre = Tk()                                         # créer la fenêtre
fenetre.geometry("400x350")                            # définie les dimensions de la fenetre
fenetre.title("Super Netry Bros  - © 2022 Hana")           # définie le titre de la fenetre
c1 = Canvas(fenetre, height=300,  width=400)           # définie la zone de dessin de la fenetre
c1.pack()                                              # definie affichage de c1

PlaySound("debut.wav", SND_FILENAME | SND_ASYNC)


img0 = PhotoImage(file="decorsfin.png")            # charger la photo "decor6400x288.png"
decor=c1.create_image(0, 0, anchor=NW, image=img0)     # ajouter la photo du decor au canvas c1

icon=PhotoImage(file="logo.png")
fenetre.iconphoto(True,icon)

imgfinf1 = PhotoImage(file="transition2 (10).png")            # charger la photo "decor6400x288.png"
trans2=c1.create_image(963, 53, anchor=NW, image=imgfinf1)     # ajouter la photo du decor au canvas c1


photo11 = PhotoImage(file="vie4 (3).png")                      # recupere mario
vie4 = c1.create_image(-28,-60, anchor=NW, image=photo11)    # insertion mario
photo10 = PhotoImage(file="vie3 (3).png")                      # recupere mario
vie3 = c1.create_image(-28,-60, anchor=NW, image=photo10)    # insertion mario
photo9 = PhotoImage(file="vie2 (3).png")                      # recupere mario
vie2 = c1.create_image(-28,-60, anchor=NW, image=photo9)    # insertion mario
photo8 = PhotoImage(file="vie1 (3).png")                      # recupere mario
vie1 = c1.create_image(-28,-60, anchor=NW, image=photo8)    # insertion mario


score = 0                                          # donne une valeur a score

def compterScore():
     global score
     score+=250
     t1['text']="Score : "+str(score)


t1 = Label(fenetre, text = "Score = 0" )               # label pour afficher le message "Score = 0"
t1.pack(padx=0, pady=0, side=TOP)                      # definie affichage de t1

t6 = Label(fenetre, text = "Copyright © 2022 Hana company all rights reserved law n° 2006-961" )               # label pour afficher le message "Score = 0"
t6.pack(padx=0, pady=0, side=TOP)                      # definie affichage de t1



photofin1 = PhotoImage(file="fin1.png")
fin1=c1.create_image(14600,154, anchor=CENTER, image=photofin1)

photo = PhotoImage(file="j1.png")                      # recupere mario
mario1 = c1.create_image(100,258, anchor=SW, image=photo)    # insertion mario

photo2 = PhotoImage(file="j2.png")                      # recupere mario
mario2 = c1.create_image(100,258, anchor=SW, image=photo2)    # insertion mario




tryyy=0


def inverser():
    mariocours = c1.itemcget(mario1, "state")=="hidden" # connaitre l'état de la lampe
    global tryyy
    if tryyy>=10:
        c1.itemconfigure(mario1, state='hidden')
        c1.itemconfigure(mario2, state='hidden')

    elif mariocours :
           c1.itemconfigure(mario1, state='normal')       # montrer l'image i0 lampe allumée
           c1.itemconfigure(mario2, state='hidden')       # cacher l'image i1

    else :
           c1.itemconfigure(mario1, state='hidden')       # cacher l'image i0
           c1.itemconfigure(mario2, state='normal')       # montrer l'image i1 lampe éteinte
    fenetre.after( 200, inverser )


photocible = PhotoImage(file="piiece.png")              # recupere cible
cible1 = c1.create_image(9000,200, anchor=SW, image=photocible) # insertion cible
cible2 = c1.create_image(9050,200, anchor=SW, image=photocible)
cible3 = c1.create_image(9200,200, anchor=SW, image=photocible)
cible4 = c1.create_image(9300,200, anchor=SW, image=photocible)
cible5 = c1.create_image(9350,200, anchor=SW, image=photocible)
cible6 = c1.create_image(9400,200, anchor=SW, image=photocible)
cible7 = c1.create_image(9700,200, anchor=SW, image=photocible)
cible8 = c1.create_image(9755,200, anchor=SW, image=photocible)
cible9 = c1.create_image(9855,200, anchor=SW, image=photocible)
cible10 = c1.create_image(4200,200, anchor=SW, image=photocible)
cible11 = c1.create_image(4255,200, anchor=SW, image=photocible)
cible12 = c1.create_image(4355,200, anchor=SW, image=photocible)
cible13 = c1.create_image(4500,200, anchor=SW, image=photocible)
cible14 = c1.create_image(4755,200, anchor=SW, image=photocible)
cible15 = c1.create_image(4800,200, anchor=SW, image=photocible)
cible16 = c1.create_image(4900,200, anchor=SW, image=photocible)
cible17 = c1.create_image(5055,200, anchor=SW, image=photocible)

cible18 = c1.create_image(5600,200, anchor=SW, image=photocible)
cible19 = c1.create_image(5655,200, anchor=SW, image=photocible)
cible20 = c1.create_image(6800,200, anchor=SW, image=photocible)
cible21 = c1.create_image(6875,200, anchor=SW, image=photocible)
cible22 = c1.create_image(7000,200, anchor=SW, image=photocible)
cible23 = c1.create_image(7100,200, anchor=SW, image=photocible)
cible24 = c1.create_image(7155,200, anchor=SW, image=photocible)
cible25 = c1.create_image(7300,200, anchor=SW, image=photocible)
cible26 = c1.create_image(7400,200, anchor=SW, image=photocible)
cible27 = c1.create_image(7455,200, anchor=SW, image=photocible)
cible28 = c1.create_image(7600,200, anchor=SW, image=photocible)
cible29 = c1.create_image(7800,200, anchor=SW, image=photocible)
cible30 = c1.create_image(7855,200, anchor=SW, image=photocible)

cible31 = c1.create_image(10000,200, anchor=SW, image=photocible)
cible32 = c1.create_image(10055,200, anchor=SW, image=photocible)
cible33 = c1.create_image(10105,200, anchor=SW, image=photocible)
cible34 = c1.create_image(10200,200, anchor=SW, image=photocible)
cible35 = c1.create_image(10300,200, anchor=SW, image=photocible)
cible36 = c1.create_image(10355,200, anchor=SW, image=photocible)
cible37 = c1.create_image(10900,200, anchor=SW, image=photocible)
cible38 = c1.create_image(11100,200, anchor=SW, image=photocible)
cible39 = c1.create_image(11155,200, anchor=SW, image=photocible)
cible40 = c1.create_image(11300,200, anchor=SW, image=photocible)
cible41 = c1.create_image(11400,200, anchor=SW, image=photocible)
cible42 = c1.create_image(11455,200, anchor=SW, image=photocible)
cible43 = c1.create_image(11600,200, anchor=SW, image=photocible)


photocarapace = PhotoImage(file="mechant (2).png")
carapace=c1.create_image(1000, 260, anchor=SW, image=photocarapace)
carapace2=c1.create_image(5500, 260, anchor=SW, image=photocarapace)
carapace3=c1.create_image(6900, 260, anchor=SW, image=photocarapace)

carapace4=c1.create_image(8400, 260, anchor=SW, image=photocarapace)
carapace5=c1.create_image(9500, 260, anchor=SW, image=photocarapace)

carapace6=c1.create_image(10800, 260, anchor=SW, image=photocarapace)
carapace7=c1.create_image(12000, 260, anchor=SW, image=photocarapace)
carapace8=c1.create_image(14000, 260, anchor=SW, image=photocarapace)

carapace9=c1.create_image(16500, 260, anchor=SW, image=photocarapace)
carapace10=c1.create_image(15000, 260, anchor=SW, image=photocarapace)



photoepee = PhotoImage(file="epee (4).png")
epee=c1.create_image(12000, 275, anchor=SW, image=photoepee)


def Launcher():
    import NetryLauncher



def gererCollision(objet,cible):
    x = c1.coords(objet)[0]                           # extraire la position x de objet
    y = c1.coords(objet)[1]                           # extraire la position y de objet
    objetID=c1.find_closest(x, y)                     # scruter l'objet à la position x, y
    print( objetID, cible )
    if objetID[0] == cible:                          # si c'est l'objet cible
          PlaySound("coin.wav", SND_FILENAME | SND_ASYNC)
          c1.delete(cible)
          compterScore()


def Quitter():
    fenetre.destroy()


photocoeur = PhotoImage(file="coeurrr.png")              # recupere cible
coeur = c1.create_image(8200,175, anchor=CENTER, image=photocoeur) # insertion cible

photogame = PhotoImage(file="over.png")
over=c1.create_image(200,150, anchor=CENTER, image=photogame)
c1.itemconfigure(over, state='hidden')


photomm= PhotoImage(file="j1 (1).png")
mario3=c1.create_image(100, 258, anchor=SW, image=photomm)
c1.itemconfigure(mario3, state='hidden')
photompp = PhotoImage(file="j2 (1).png")
mario4=c1.create_image(100, 258, anchor=SW, image=photompp)
c1.itemconfigure(mario4, state='hidden')

photoboss = PhotoImage(file="bigboss1.png")
boss=c1.create_image(18000, 265, anchor=SW, image=photoboss)


fois=0
sword =0

inver=0


def tryy():
    c1.delete(mario1)
    c1.delete(mario2)
    c1.itemconfigure(mario1, state='normal')
    c1.itemconfigure(mario2, state='normal')


def inver2():
    mariocours1 = c1.itemcget(mario3, "state")=="hidden" # connaitre l'état de la lampe
    if mariocours1 :
        c1.itemconfigure(mario3, state='normal')       # montrer l'image i0 lampe allumée
        c1.itemconfigure(mario4, state='hidden')       # cacher l'image i1
    else :
        c1.itemconfigure(mario3, state='hidden')       # cacher l'image i0
        c1.itemconfigure(mario4, state='normal')       # montrer l'image i1 lampe éteinte
    fenetre.after( 200, inver2 )


def Epee (objet,cible):
    x = c1.coords(objet)[0]                           # extraire la position x de objet
    y = c1.coords(objet)[1]                           # extraire la position y de objet
    objetID=c1.find_closest(x, y)                     # scruter l'objet à la position x, y
    print( objetID, cible )
    global sword
    global inver
    global tryyy
    if objetID[0] == cible:
        tryyy+=10
        PlaySound("nouvelle-vie.wav", SND_FILENAME | SND_ASYNC)
        #tryy()
        c1.itemconfigure(epee, state='hidden')
        c1.itemconfigure(mario4, state='normal')
        inver2()




def Boss(objet,cible):
    x = c1.coords(objet)[0]                           # extraire la position x de objet
    y = c1.coords(objet)[1]                           # extraire la position y de objet
    objetID=c1.find_closest(x, y)                     # scruter l'objet à la position x, y
    print( objetID, cible )
    global sword
    global score
    if objetID[0] == cible:
        PlaySound("Bowser 001.wav", SND_FILENAME | SND_ASYNC)
        c1.itemconfigure(boss, state='hidden')
        score+=1000
        t1['text']="Score : "+str(score)


def Carapace2(objet,cible):

    x = c1.coords(objet)[0]                           # extraire la position x de objet
    y = c1.coords(objet)[1]                           # extraire la position y de objet
    objetID=c1.find_closest(x, y)                     # scruter l'objet à la position x, y
    print( objetID, cible )
    global score
    global fois


    if objetID[0] == cible and fois==0:
        PlaySound("aie.wav", SND_FILENAME | SND_ASYNC)                              # alors suppression bruyante
        c1.itemconfigure(mario2, state='hidden')
        c1.itemconfigure(mario1, state='hidden')
        c1.itemconfigure(vie1, state='hidden')
        score-=1000
        t1['text']="Score : "+str(score)
        fois+=10



    elif objetID[0] == cible and fois==10:
        PlaySound("aie.wav", SND_FILENAME | SND_ASYNC)                              # alors suppression bruyante
        c1.itemconfigure(mario2, state='hidden')
        c1.itemconfigure(mario1, state='hidden')
        c1.itemconfigure(vie2, state='hidden')

        score-=1000
        t1['text']="Score : "+str(score)
        fois+=10


    elif objetID[0] == cible and fois==20 :
        PlaySound("aie.wav", SND_FILENAME | SND_ASYNC)                              # alors suppression bruyante
        c1.itemconfigure(mario2, state='hidden')
        c1.itemconfigure(mario1, state='hidden')
        c1.itemconfigure(vie3, state='hidden')
        score-=1000
        t1['text']="Score : "+str(score)
        fenetre.after(1250, gameover)
        fenetre.after(7000, Quitter)




def gameover():
    c1.itemconfigure(over, state='normal')
    PlaySound("game-over.wav", SND_FILENAME | SND_ASYNC)                              # alors suppression bruyante







def CollisionCoeur(objet,cible):
    x = c1.coords(objet)[0]                           # extraire la position x de objet
    y = c1.coords(objet)[1]                           # extraire la position y de objet
    objetID=c1.find_closest(x, y)                     # scruter l'objet à la position x, y
    print( objetID, cible )
    global fois
    if objetID[0] == cible and fois==10:                          # si c'est l'objet cible
          PlaySound("nouvelle-vie.wav", SND_FILENAME | SND_ASYNC)
          c1.delete(cible)
          fois-=10
          c1.itemconfigure(vie1, state='normal')

    elif objetID[0] == cible and fois==20 :
        PlaySound("nouvelle-vie.wav", SND_FILENAME | SND_ASYNC)                              # alors suppression bruyante
        c1.delete(cible)
        fois-=10
        c1.itemconfigure(vie2, state='normal')




def Map ():
    import Netryend


photofin2 = PhotoImage(file="fin2.png")
fin2=c1.create_image(14600,154, anchor=CENTER, image=photofin2)

photochateau = PhotoImage(file="trone (1).png")
chateau=c1.create_image(15000,181, anchor=CENTER, image=photochateau)


def final():
    c1.itemconfigure(fin, state='normal')
    button3 = Button(  text = "Continue", font="Andalus",bd=2, width=7, command=lambda: [fenetre.destroy(), Map()])
    button3.pack(pady = 5)
    button3.place(x = 165, y = 265)

def Fin(objet,cible):
    x = c1.coords(objet)[0]                           # extraire la position x de objet
    y = c1.coords(objet)[1]                           # extraire la position y de objet
    objetID=c1.find_closest(x, y)                     # scruter l'objet à la position x, y
    print( objetID, cible )
    if objetID[0] == cible:                          # si c'est l'objet cible
          PlaySound("monde-termine.wav", SND_FILENAME | SND_ASYNC)
          fenetre.after(1000, final )






def Drapeau(objet,cible):
    x = c1.coords(objet)[0]                           # extraire la position x de objet
    y = c1.coords(objet)[1]                           # extraire la position y de objet
    objetID=c1.find_closest(x, y)                     # scruter l'objet à la position x, y
    print( objetID, cible )
    if objetID[0] == cible:                           # si c'est l'objet cible
          c1.itemconfigure(menu, state='hidden')
          c1.itemconfigure(vie4, state='normal')
          c1.itemconfigure(vie3, state='normal')
          c1.itemconfigure(vie2, state='normal')
          c1.itemconfigure(vie1, state='normal')



photofin = PhotoImage(file="Win2.png")
fin=c1.create_image(200,175, anchor=CENTER, image=photofin)
c1.itemconfigure(fin, state='hidden')


imgfinf = PhotoImage(file="transition1 (8).png")            # charger la photo "decor6400x288.png"
trans=c1.create_image(750, -383, anchor=NW, image=imgfinf)     # ajouter la photo du decor au canvas c1

def gererClavier(key):
     print( key.keysym )                   # affiche le code de la touche appuyée
     if key.keysym=="space" :              # si flèche droite appuyée
         c1.coords(mario1, 100, 200)       #     alors agrandir la fenêtre
         c1.coords(mario2, 100, 200)
         c1.coords(mario3, 100, 200)       #     alors agrandir la fenêtre
         c1.coords(mario4, 100, 200)


def gererClavier2(key):
     print( key.keysym )                   # affiche le code de la touche appuyée
     if key.keysym=="space" :              # si flèche droite appuyée
         c1.coords(mario1, 100, 258)       #     alors agrandir la fenêtre
         c1.coords(mario2, 100, 258)
         c1.coords(mario3, 100, 258)       #     alors agrandir la fenêtre
         c1.coords(mario4, 100, 258)



fenetre.bind("<KeyPress>", gererClavier)   # Exécuter gérerClavier si touche enfoncée
fenetre.bind("<KeyRelease>", gererClavier2)





inverser()
jouerPartie()                                          # Appeler le sous-programme jouerPartie
fenetre.mainloop()                                     # Affiche la fenêtre en boucle




