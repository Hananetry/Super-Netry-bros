########################################################################
# JeffProd Simple Python Chess Program
########################################################################
# AUTHOR	: Jean-Francois GAZET
# GUI           : Didier MULLER
# WEB 		: http://www.jeffprod.com
# TWITTER	: @JeffProd
# MAIL		: jeffgazet@gmail.com
# LICENCE	: GNU GENERAL PUBLIC LICENSE Version 2, June 1991
########################################################################


from tkinter import *
from piece import *
from board import *
from engine import *
from time import sleep
from random import randint, choice

class Image:

    def __init__(self,nom='VIDE',couleur='',coord_x=0,coord_y=0,nom_image=''):

        self.nom = nom
        self.couleur = couleur
        self.x=coord_x
        self.y=coord_y
        self.nom_image = nom_image

#---------------------------------------------------------------------


def coord_case_clic(x_pos,y_pos):
    # renvoie les coordonnÃ©es d'une case en fonction des coordonnÃ©es du clic
    coord_x = (x_pos-c-5)//c
    coord_y = (y_pos-c+5)//c
    return coord_x, coord_y

def coord_case_no(no):
    # renvoie les coordonnÃ©es d'une case en fonction du numÃ©ro de la case (0 Ã  63)
    coord_x = no%8
    coord_y = no//8
    return coord_x, coord_y

def nom_case(x_pos,y_pos):
    # renvoie le nom d'une case (de a1 Ã  h8) en fonction des coordonnÃ©es de la case
    return chr(97+x_pos)+str(8-y_pos)

def no_case(nom):
    # inverse de nom_case
    colonne = ord(nom[0])-97
    ligne = int(nom[1])
    return 8*(8-ligne) + colonne

def coord_image(x_pos,y_pos):
    # renvoie les coordonnÃ©es du centre d'une case en fonction des coordonnÃ©es de la case
    x = c*x_pos+110
    y = c*y_pos+100
    return x,y

def afficher_echiquier(b):
    # cree les listes de pieces et les affiche
    for i in range(64):
        if b.cases[i].image != '':
            x,y = coord_case_no(i)
            x,y = coord_image(x,y)
            f_piece.append(PhotoImage(file=b.cases[i].image))
            pieces.append(Image(b.cases[i].nom, b.cases[i].couleur, x, y, canevas.create_image(x,y,image=f_piece[-1])))

def dessus(evt) :
    global dc
    forme = "arrow"
    for i in range(len(pieces)) :
        if pieces[i].x-dc < evt.x < pieces[i].x+dc and pieces[i].y-dc < evt.y < pieces[i].y+dc and b.side2move==pieces[i].couleur:
            forme = "fleur"
    canevas.config(cursor = forme)

def glisser(evt):
    global x, y, num, coup
    x3, y3 = coord_case_clic(x, y)
    coup = nom_case(x3,y3)
    if num == -1 :
        for i in range(len(pieces)) :
            if pieces[i].x-dc < evt.x < pieces[i].x+dc and pieces[i].y-dc < evt.y < pieces[i].y+dc and b.side2move==pieces[i].couleur:
                canevas.tag_raise(pieces[i].nom_image)
                x, y, num = evt.x, evt.y, i
    else :
        delta_x, delta_y = evt.x - x, evt.y - y
        canevas.coords(pieces[num].nom_image, pieces[num].x + delta_x, pieces[num].y + delta_y)

def coup_valide(dep,arr,promote):
    # vÃ©rifie si le coup est valide avant de poser la piÃ¨ce
    mList=b.gen_moves_list()
    pos1 = b.coord.index(dep)
    pos2 = b.coord.index(arr)
    if(((pos1,pos2,promote) not in mList) or (b.domove(pos1,pos2,promote)==False)):
        return False
    return True

def enlever_piece(x,y,num):
    # enleve une piece de l'echiquier
    for i in range(len(pieces)) :
        if pieces[i].x==x and pieces[i].y==y and i!=num:
            return i
    # prise en passant
    if pieces[num].nom=="PION" and pieces[num].couleur=="blanc":
        for i in range(len(pieces)) :
            if pieces[i].x==x and pieces[i].y==y+c:
                return i
    if pieces[num].nom=="PION" and pieces[num].couleur=="noir":
        for i in range(len(pieces)) :
            if pieces[i].x==x and pieces[i].y==y-c:
                return i
    return -1

def bouger_piece(num,x1,y1,x2,y2):
    nbr_pas = 20
    dx = (x2-x1)/nbr_pas
    dy = (y2-y1)/nbr_pas
    canevas.tag_raise(pieces[num].nom_image)
    for i in range(nbr_pas):
        pieces[num].x += dx
        pieces[num].y += dy
        canevas.coords(pieces[num].nom_image, pieces[num].x, pieces[num].y)
        sleep(1/nbr_pas)  # dÃ©lai (en secondes)
        canevas.update()
    pieces[num].x = x2
    pieces[num].y = y2
    canevas.coords(pieces[num].nom_image, pieces[num].x, pieces[num].y)

def roques(depart,arrivee):
    x1, y1 = coord_case_no(depart)
    x2, y2 = coord_case_no(arrivee)
    x1, y1 = coord_image(x1, y1)
    x2, y2 = coord_image(x2, y2)
    num=0
    while not (pieces[num].x == x1 and pieces[num].y == y1):    # trouve la tour Ã  dÃ©placer
        num += 1
    bouger_piece(num,x1,y1,x2,y2)

def deposer(evt):
    global num, coup, demi_coup, debut_patie
    promotion=""
    no_a_virer = -1
    ok = False
    if num != -1 :
        x2 = pieces[num].x + evt.x - x
        y2 = pieces[num].y + evt.y - y
        # centrer les pieces sur la case
        x3, y3 = coord_case_clic(x2, y2)
        x1, y1 = coord_image(x3,y3)
        arr = nom_case(x3,y3)
        if x3<8 and x3>=0 and y3<8 and y3>=0 :            # evite que les pieces soient posÃ©es n'importe oÃ¹
            if pieces[num].nom=="PION" and pieces[num].couleur=="blanc" and y3==0:
                promotion ="q"
            if pieces[num].nom=="PION" and pieces[num].couleur=="noir" and y3==7:
                promotion ="q"
            if coup_valide(coup, arr, promotion):
                # roque?
                if pieces[num].nom=="ROI" and pieces[num].couleur=="blanc":
                    if pieces[num].x-x1 == -2*c:
                        roques(63,61)
                    elif pieces[num].x-x1 == 2*c:
                        roques(56,59)
                elif pieces[num].nom=="ROI" and pieces[num].couleur=="noir":
                    if pieces[num].x-x1 == -2*c:
                        roques(7,5)
                    elif pieces[num].x-x1 == 2*c:
                        roques(0,3)

                if promotion != "":
                    coul = pieces[num].couleur
                    del(pieces[num])
                    del(f_piece[num])
                    if coul=="blanc":   # on peut faire autre chose qu'une dame...
                        f_piece.append(PhotoImage(file="Db.png"))
                    else:
                        f_piece.append(PhotoImage(file="Dn.png"))
                    pieces.append(Image("DAME", coul, x1, y1, canevas.create_image(x1,y1,image=f_piece[-1])))
                    num = len(pieces)-1
                else:
                    pieces[num].x = x1
                    pieces[num].y = y1
                coup += arr
                debut_partie.append(coup)
                no_a_virer =enlever_piece(x1,y1,num)  # piÃ¨ce adverse Ã  enlever en cas de prise
                demi_coup += 1
                ok = True
        canevas.coords(pieces[num].nom_image, pieces[num].x, pieces[num].y)
        if no_a_virer != -1:
            del(pieces[no_a_virer])
            del(f_piece[no_a_virer])
        canevas.update()
    if ok:
        ordi_joue(b)
    num = -1

def animation_piece(depart, arrivee):
    no_a_virer = -1
    x1, y1 = coord_case_no(depart)
    x2, y2 = coord_case_no(arrivee)
    x1, y1 = coord_image(x1, y1)
    x2, y2 = coord_image(x2, y2)
    num=0
    while not (pieces[num].x == x1 and pieces[num].y == y1):    # trouve la piÃ¨ce dÃ©placÃ©e
        num += 1
    bouger_piece(num,x1,y1,x2,y2)
    no_a_virer =enlever_piece(x2,y2,num)  # piÃ¨ce adverse Ã  enlever en cas de prise
    if no_a_virer != -1:
        del(pieces[no_a_virer])
        del(f_piece[no_a_virer])
    #roques
    if pieces[num].nom=="ROI" and pieces[num].couleur=="blanc":
        if x1-x2 == -2*c:
            roques(63,61)
        elif x1-x2 == 2*c:
            roques(56,59)
    elif pieces[num].nom=="ROI" and pieces[num].couleur=="noir":
        if x1-x2 == -2*c:
            roques(7,5)
        elif x1-x2 == 2*c:
            roques(0,3)

def trouver_ouv(debut_liste):
    # retourne la liste des ouvertures correspondant aux premiers coups
    global ouvertures
    fin = len(ouvertures)
    long_debut = len(debut_liste)
    j=0
    ouv = []
    while j<fin:
        if debut_liste==ouvertures[j][0:long_debut]:
            ouv.append(j)
        j += 1
    return ouv

def ordi_joue(b):
    global demi_coup, ouvertures, mode_ouverture, debut_partie
    canevas.config(cursor = "watch")
    if mode_ouverture :
        if demi_coup == 0:  # choisit une ouverture au hasard
            j = randint(0,len(ouvertures))
            dep = ouvertures[j][0][0:2]
            arr = ouvertures[j][0][2:4]
            coup = [no_case(dep),no_case(arr),'']
            str_coup = dep+arr
            debut_partie.append(str_coup)
        else:
            ouv=trouver_ouv(debut_partie)
            if len(ouv)>0:
                j = choice(ouv)
                print(ouvertures[j])
                if len(ouvertures[j])>len(debut_partie):
                    dep = ouvertures[j][demi_coup][0:2]
                    arr = ouvertures[j][demi_coup][2:4]
                    coup = [no_case(dep),no_case(arr),'']
                    str_coup = dep+arr
                    debut_partie.append(str_coup)
                else:
                    mode_ouverture = False
                    coup = e.search(b)
            else:
                mode_ouverture = False
                coup = e.search(b)
    else:
        coup = e.search(b)
    e.print_result(b)
    demi_coup += 1
    if not e.endgame:
        b.domove(coup[0],coup[1],coup[2])
        animation_piece(coup[0],coup[1])
        canevas.config(cursor = "arrow")
        b.render()


# ----- crÃ©ation des menus et sous-menus ------------------------------------------

def bye():
    l = randint(1,10)
    if l==5 :
        import Netrybye




def creer_menus(fen):
    top = Menu(fen)
    fen.config(menu=top)

    jeu = Menu(top, tearoff=False)
    top.add_cascade(label='Game', menu=jeu)
    jeu.add_command(label='New Game', command=reinit)
    jeu.add_command(label='Save the game', command=sauver_partie)
    jeu.add_command(label='Take back the game', command=recuperer_partie)
    jeu.add_command(label='Exit', command=lambda: [fen.destroy(), bye()])

    ia = Menu(top, tearoff=False)
    submenu=Menu(ia, tearoff=False)
    top.add_cascade(label='AI', menu=ia)
    ia.add_cascade(label='Play !', command=go)
    ia.add_cascade(label='Depth', menu=submenu)
    submenu.add_command(label='3', command=prof3)
    submenu.add_command(label="4", command=prof4)
    submenu.add_command(label='5', command=prof5)

def reinit():
    global f_piece, pieces, x, y, num, b, debut_partie, demi_coup, mode_ouverture
    f_piece = [] # fichier image de la piece
    pieces = [] # liste des pieces sur le plateau
    x, y, num = -1, -1, -1
    b.setboard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - - 1")  # position initiale en FEN
    afficher_echiquier(b)
    demi_coup = 0  # compte les coups jouÃ©s
    debut_partie = []
    e.init()
    mode_ouverture = True

def recuperer_partie():
    # recupÃ¨re une position au format FEN dans le fichier position.txt
    global f_piece, pieces, x, y, num, b
    f_piece = [] # fichier image de la piece
    pieces = [] # liste des pieces sur le plateau
    x, y, num = -1, -1, -1
    try:
        fichier = open("position.txt", "r")
        position = fichier.read()
        print(position)
        b.setboard(position)
        fichier.close()
        afficher_echiquier(b)
        e.init()
        mode_ouverture = False
    except FileNotFoundError:
        print("ficher introuvable")

def sauver_partie():
    # enregistre une position au format FEN dans le fichier position.txt
    fichier = open("position.txt", "w")
    fichier.write(b.getboard())
    fichier.write("\n")
    fichier.close()

def prof3():
    e.setDepth(3)

def prof4():
    e.setDepth(4)

def prof5():
    e.setDepth(5)

def go():
    ordi_joue(b)


# opening book

def ouvrir_livre():
    try:
        fichier = open("book.txt", "r")
        ouvertures_texte = fichier.readlines()
        fichier.close()
        for ligne in ouvertures_texte:
            ouvertures.append(ligne.split())
        fichier.close()
    except FileNotFoundError:
        print("opening book introuvable")

# ---------------------------------------------------------------------------------

c = 70         # cÃ´tÃ© d'un carrÃ©
dc = c//2
fenetre = Tk()
creer_menus(fenetre)
fenetre.title("Netry Chess Game - © 2022 Hana")
canevas = Canvas(fenetre, bg='white', height=700, width=700)
canevas.pack(side=TOP)
photo=PhotoImage(file="echiquier2.png")
canevas.create_image(320, 380, image=photo)
canevas.pack()

icon=PhotoImage(file="logo.png")
fenetre.iconphoto(True,icon)


mode_ouverture = True
demi_coup = 0  # compte les coups jouÃ©s
ouvertures = []
debut_partie = []
ouvrir_livre()

# utiles pour le deplacement avec la souris
f_piece = [] # fichier image de la piece
pieces = [] # liste des pieces sur le plateau

x, y, num = -1, -1, -1
b = Board()  # Ã©chiquier
#b.setboard("3qk3/8/8/8/8/8/8/4K3 w KQkq - - 0")  # position initiale en FEN
b.setboard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - - 1")  # position initiale en FEN
couleur_joueur="blanc"
afficher_echiquier(b)
coup =""  # coup jouÃ©
e=Engine()  # "cerveau" de l'ordinateur


canevas.bind('<B1-Motion>',glisser)
canevas.bind('<ButtonRelease-1>',deposer)
canevas.bind('<Motion>',dessus)
fenetre.mainloop()