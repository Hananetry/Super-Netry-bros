# Créé par Hana, le 05/03/2022 en Python 3.7
# Memory pour 2 joueurs humains

from tkinter import *
from random import randint, shuffle

# ----- variables globales ---------------------------------------------------
images = []         # contient les liens aux fichiers images
cartes = []         # contient le lien vers l'image des différentes cartes
cartes_jouees = []  # contient les cartes jouées
nb_lignes, nb_colonnes = 5, 4
joueur_actuel = 0
score = [0,0]
fini6 = False
peut_jouer = True


# ----- Images ----------------------------------------------------------------
def charger_images():
    del images[:]   # vide la liste
    nb_images = 21  # l'image no 0 est le dos des cartes
    choixCartes = []
    choixCartes.append(0)
    i=0
    while i < nb_images-1:           # tirage au sort des cartes à utiliser
        x = randint(1, nb_images-1)
        if x not in choixCartes:
            choixCartes.append(x)
            i += 1
    for i in range(nb_images):           # importation des images
        nom = 'carte-' + str(choixCartes[i]) + '.png'
        image = PhotoImage(file = nom)
        images.append(image)


# ----- Melange des cartes -----------------------------------------------------
def melanger_cartes():
    global nb_colonnes, nb_lignes, cartes
    nb_cartes = nb_colonnes * nb_lignes
    cartes=list(range(1,nb_cartes//2+1))*2
    shuffle(cartes)


# ----- Retourne les deux cartes à la fin de la sélection ----------------------
def gerer_tirage():
    global nb_colonnes, nb_lignes, cartes_jouees
    global joueur_actuel, fini6, peut_jouer
    if cartes[cartes_jouees[0]-1] == cartes[cartes_jouees[1]-1]:
        # enlève les cartes identiques. Le joueur actuel reste le même
        canvas.delete(cartes_jouees[0])
        canvas.delete(cartes_jouees[1])
        score[joueur_actuel] += 1
    else:
        # retourne les cartes différentes. Le joueur actuel change
        canvas.itemconfig(cartes_jouees[0], image = images[0])
        canvas.itemconfig(cartes_jouees[1], image = images[0])
        joueur_actuel = (joueur_actuel+1)%2     # la main passe à l'autre joueur
    cartes_jouees = []
    text1 = 'Player 1 : ' + str(score[0]*2)
    text2 = 'Player 2 : ' + str(score[1]*2)
    points_joueur1.config(text = text1)
    points_joueur2.config(text = text2)
    peut_jouer = True           # réactive l'effet du clic de la souris
    if joueur_actuel == 0:      # celui qui joue est en orange
        points_joueur1.config(bg = 'gray')
        points_joueur2.config(bg = 'white')
    else:
        points_joueur2.config(bg = 'gray')
        points_joueur1.config(bg = 'white')
    if score[0] + score[1] == (nb_colonnes*nb_lignes)//2:
        fini6=True               # afficher le résultat de la partie
        if score[0] > score[1]:
            texte = "Player 1 won !"
        elif score[0] < score[1]:
            texte = "Player 2 won !"
        else:
            texte = "Egalité !"
        canvas.create_rectangle(0,0,(110*nb_colonnes)+20,(110*nb_lignes)+20,
                                fill='white')
        canvas.create_text((55*nb_colonnes)+10,(55*nb_lignes)+10,
                           text=texte,font='Calibri 24',fill='black')

# ----- Retourne la carte sélectionnée -----------------------------------------
def cliquer_carte(event):
    global fini6, plateau, cartes_jouees, peut_jouer
    if len(cartes_jouees) < 2:
        carteSel = canvas.find_closest(event.x, event.y)
        carteID = carteSel[0]
        if fini6:
            fini6 = False
            reinit()
        else:
            canvas.itemconfig(carteID, image = images[cartes[carteID-1]]) # montre la carte
            if len(cartes_jouees) == 0:
                cartes_jouees.append(carteID)    # enregistre la carte jouée
            elif carteID != cartes_jouees[0]:    # ne pas cliquer 2x sur la même carte !
                cartes_jouees.append(carteID)
    if peut_jouer and len(cartes_jouees) == 2:
        peut_jouer = False                  # désactive l'effet du clic de la souris
        plateau.after(1500,gerer_tirage)    # patiente 1,5 secondes avant de continuer


# -----  Change la taille du plateau de jeu  -------------------------------------
def jeu5x4():
    global nb_colonnes
    nb_colonnes = 4
    reinit()

def jeu5x6():
    global nb_colonnes
    nb_colonnes = 6
    reinit()

def jeu5x8():
    global nb_colonnes
    nb_colonnes = 8
    reinit()



def Launcher():
    import NetryLauncher


def bye():
    l = randint(1,10)
    if l==2 :
        import Netrybye

# ----- création des menus et sous-menus ------------------------------------------
def creer_menus(fen):
    top = Menu(fen)
    fen.config(menu=top)

    jeu = Menu(top, tearoff=False)
    top.add_cascade(label='Game', menu=jeu)
    jeu.add_command(label='New game', command=reinit)

    submenu=Menu(jeu, tearoff=False)
    jeu.add_cascade(label='Size', menu=submenu)
    submenu.add_command(label='5 x 4', command=jeu5x4)
    submenu.add_command(label='5 x 6', command=jeu5x6)
    submenu.add_command(label='5 x 8', command=jeu5x8)

    jeu.add_command(label='Exit', command=lambda: [fen.destroy(),bye()])


# ----- Création du canvas --------------------------------------------------------
def creer_canevas(fen, col, lig):
    return Canvas(fen, width=(110*col)+10, height=(110*lig)+10, bg='white')


# ----- Modifier le canvas --------------------------------------------------------
# Redémarre une partie et change éventuellement la difficulté
def reinit():
    global canvas, joueur_actuel, score, nb_lignes, nb_colonnes
    joueur_actuel = 0
    score =[0,0]
    del cartes[:]
    del cartes_jouees[:]
    canvas.destroy()
    canvas = creer_canevas(plateau, nb_colonnes, nb_lignes)
    canvas.pack(side = TOP, padx = 5, pady = 5)
    canvas.bind("<Button-1>", cliquer_carte)    # permet le clic sur les cartes
    melanger_cartes()
    for i in range(nb_colonnes):                # dessin des cartes retournées
        for j in range(nb_lignes):
            canvas.create_image((110*i)+60, (110*j)+60, image=images[0])
    text1 = 'Player 1 : ' + str(score[0]*2)
    text2 = 'Player 2 : ' + str(score[1]*2)
    points_joueur1.config(text = text1, bg = 'gray')
    points_joueur2.config(text = text2, bg = 'white')


# ----- Programme principal ----------------------------------------------------
fenetre2 = Tk()
fenetre2.title("Netry Memory")
creer_menus(fenetre2)


icon=PhotoImage(file="logo.png")
fenetre2.iconphoto(True,icon)
# création du canvas dont la taille dépend du nombre de cartes
plateau = Frame(fenetre2)
plateau.pack()
canvas=creer_canevas(plateau, nb_colonnes, nb_lignes)
canvas.pack(side = TOP, padx = 2, pady = 2)
points_joueur1 = Label(fenetre2, text = "Player 1 : 0",
                       bg="gray", font="Helvetica 16")
points_joueur1.pack(pady = 2, side = LEFT)
points_joueur2 = Label(fenetre2, text = "Player 2 : 0", font="Helvetica 16")
points_joueur2.pack(pady = 2, side = RIGHT)
charger_images()
melanger_cartes()
for i in range(nb_colonnes):                # dessin des cartes retournées
    for j in range(nb_lignes):
        canvas.create_image((110*i)+60, (110*j)+60, image = images[0])
canvas.bind("<Button-1>", cliquer_carte)    # permet le clic sur les cartes
fenetre2.mainloop()


