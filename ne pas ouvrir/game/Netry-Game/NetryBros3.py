# Créé par Hana, le 19/03/2022 en Python 3.7
# Créé par Hana, le 19/02/2022 en Python 3.7
''' programme jeu mario avec cibles et carapace, décors en mouvement avec nuages,
insertion de colision pour les cibles et carapace et mouvement des cibles,
score personalisé qui augmente a chaque cibles'''



from tkinter import *
from winsound import *

def jouerPartie():

    c1.move(decor, -10, 0)                             # déplacer le décor à la position x
    c1.move(carapace, -29, 0 )
    c1.move(carapace2, -29, 0 )
    c1.move(carapace3, -29, 0 )
    c1.move(carapace4, -29, 0 )
    c1.move(carapace5, -29, 0 )

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


img0 = PhotoImage(file="decors3.png")            # charger la photo "decor6400x288.png"
decor=c1.create_image(0, 0, anchor=NW, image=img0)     # ajouter la photo du decor au canvas c1


icon=PhotoImage(file="logo.png")
fenetre.iconphoto(True,icon)


photo11 = PhotoImage(file="vie4 (2).png")                      # recupere mario
vie4 = c1.create_image(-28,-60, anchor=NW, image=photo11)    # insertion mario
photo10 = PhotoImage(file="vie3 (2).png")                      # recupere mario
vie3 = c1.create_image(-28,-60, anchor=NW, image=photo10)    # insertion mario
photo9 = PhotoImage(file="vie2 (2).png")                      # recupere mario
vie2 = c1.create_image(-28,-60, anchor=NW, image=photo9)    # insertion mario
photo8 = PhotoImage(file="vie1 (2).png")                      # recupere mario
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



photofin1 = PhotoImage(file="fin5.png")
fin1=c1.create_image(8200,154, anchor=CENTER, image=photofin1)

photo = PhotoImage(file="j1.png")                      # recupere mario
mario1 = c1.create_image(100,258, anchor=SW, image=photo)    # insertion mario

photo2 = PhotoImage(file="j2.png")                      # recupere mario
mario2 = c1.create_image(100,258, anchor=SW, image=photo2)    # insertion mario







def inverser():
    mariocours = c1.itemcget(mario1, "state")=="hidden" # connaitre l'état de la lampe
    if mariocours :
           c1.itemconfigure(mario1, state='normal')       # montrer l'image i0 lampe allumée
           c1.itemconfigure(mario2, state='hidden')       # cacher l'image i1
    else :
           c1.itemconfigure(mario1, state='hidden')       # cacher l'image i0
           c1.itemconfigure(mario2, state='normal')       # montrer l'image i1 lampe éteinte
    fenetre.after( 200, inverser )



photocible = PhotoImage(file="piiece.png")              # recupere cible
cible1 = c1.create_image(1455,200, anchor=SW, image=photocible) # insertion cible
cible2 = c1.create_image(1000,200, anchor=SW, image=photocible)
cible3 = c1.create_image(1100,200, anchor=SW, image=photocible)
cible4 = c1.create_image(1155,200, anchor=SW, image=photocible)
cible5 = c1.create_image(1200,200, anchor=SW, image=photocible)
cible6 = c1.create_image(1355,200, anchor=SW, image=photocible)
cible7 = c1.create_image(1550,200, anchor=SW, image=photocible)
cible8 = c1.create_image(1600,200, anchor=SW, image=photocible)
cible9 = c1.create_image(1755,200, anchor=SW, image=photocible)
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




photocarapace = PhotoImage(file="mechant2 (3).png")
carapace=c1.create_image(4200, 261, anchor=SW, image=photocarapace)
carapace2=c1.create_image(5500, 261, anchor=SW, image=photocarapace)
carapace3=c1.create_image(6900, 261, anchor=SW, image=photocarapace)

carapace4=c1.create_image(8400, 261, anchor=SW, image=photocarapace)
carapace5=c1.create_image(9500, 261, anchor=SW, image=photocarapace)


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
coeur = c1.create_image(5500,175, anchor=CENTER, image=photocoeur) # insertion cible

photogame = PhotoImage(file="over.png")
over=c1.create_image(200,150, anchor=CENTER, image=photogame)
c1.itemconfigure(over, state='hidden')


fois=0

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







photofin2 = PhotoImage(file="fin6.png")
fin2=c1.create_image(8200,154, anchor=CENTER, image=photofin2)

photochateau = PhotoImage(file="chateau3 (1).png")
chateau=c1.create_image(8600,210, anchor=CENTER, image=photochateau)


def Map ():
    import Map3


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





photofin = PhotoImage(file="Win.png")
fin=c1.create_image(200,175, anchor=CENTER, image=photofin)
c1.itemconfigure(fin, state='hidden')


def gererClavier(key):
     print( key.keysym )                   # affiche le code de la touche appuyée
     if key.keysym=="space" :              # si flèche droite appuyée
         c1.coords(mario1, 100, 200)       #     alors agrandir la fenêtre
         c1.coords(mario2, 100, 200)


def gererClavier2(key):
     print( key.keysym )                   # affiche le code de la touche appuyée
     if key.keysym=="space" :              # si flèche droite appuyée
         c1.coords(mario1, 100, 258)       #     alors agrandir la fenêtre
         c1.coords(mario2, 100, 258)



fenetre.bind("<KeyPress>", gererClavier)   # Exécuter gérerClavier si touche enfoncée
fenetre.bind("<KeyRelease>", gererClavier2)





inverser()
jouerPartie()                                          # Appeler le sous-programme jouerPartie
fenetre.mainloop()                                     # Affiche la fenêtre en boucle


