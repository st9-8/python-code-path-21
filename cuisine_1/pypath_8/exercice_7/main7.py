#fonctions de l'exercice 7
from math import *
import getpass, platform, os
import pickle

def sys_deco(func):
    print("Bienvenue {}".format(getpass.getuser()))
    print("Statista tourne sous [{}]".format(platform.system()))
    return func

def clear():
    """Cette fonction efface la console"""

    if platform.system() == "Linux":
        os.system('clear')
    if platform.system() == "Windows":
        os.system('cls')

#@sys_deco
def moyenne(liste = []):
    "calcul la moyenne de la liste"
    moy = sum(liste)/len(liste)
    return moy

#@sys_deco
def mediane(liste = []):
    "calcul la mediane de la liste"
    n = len(liste)
    if n%2 == 0:
        med = liste[int(n/2)]
    else:
        med = (liste[int(n-1/2)] + liste[int(n+1/2)])/2
    return med

def maxi(liste = []):
    "calcul du max"
    return max(liste)

def mini(liste = []):
    "calcul du min"
    return min(liste)

def variance(liste = []):
    "calcul la variance la liste"
    l = [(float(x) - moyenne(liste))*(float(x) - moyenne(liste)) for x in liste]
    return sum(l)/len(liste)

def ecart_type(liste = []):
    "calcul l'ecart type"
    return sqrt(variance(liste))

def premier_quartile(liste = []):
    "calcul premier quartile"
    cpt = len(liste)/4
    if int(cpt) == True:
        p_quart = liste[cpt]
    else:
        p_quart = liste[int(cpt) + 1]
    return p_quart

def troisieme_quartile(liste = []):
    "calcul troisieme quartile"
    cpt = 3*len(liste)/4
    if int(cpt) == True:
        t_quart = liste[cpt]
    else:
        t_quart = liste[int(cpt) + 1]
    return t_quart

def mode(liste = []):
    "calcul du mode "
    try:
        s = set(x for x in liste) #on recupere chaque element de facon unique
        d = {x:0 for x in s} #un dictionnaire avec pour cles les element de s et leurs occurences qu'on initialise a 0

        for el in liste:
            d[el] = d[el] + 1

        l = [x for x in d.keys() if d[x]== max(d.values())]
    except TypeError:
        print("La liste a un probleme")

    return l

def effectif(liste = []):
    "calcul les effectifs"
    s = set(x for x in liste) #on recupere chaque element de facon unique
    d = {x:0 for x in s} #un dictionnaire avec pour cles les element de s et leurs occurences qu'on initialise a 0

    for el in liste:
        d[el] = d[el] + 1

    return d

def effectif_cumule(liste = []):
    "effectifs cumules"
    ef = effectif(liste) 

    #s = set(x for x in liste) #on recupere chaque element de facon unique
    #un dictionnaire avec pour cles les elements de s et leurs effectifs cumules qu'on initialise a 0

    cle = [x for x in ef.keys()]
    cle.sort()
    val = [x for x in ef.values()]
    
    ef_c=ef
  
    for i in range(1, len(cle)):
        ef_c[cle[i]] = sum(val[:i+1])
    
    return ef_c


def frequence(liste = []):
    "calcul frequence"
    ef = effectif(liste)
    
    cle = [x for x in ef.keys()]
    
    val = [x for x in ef.values()]
    v = sum(ef.values())

    fq = ef
    for i in range(0, len(cle)):
        fq[cle[i]] = fq[cle[i]]/v

    return fq

def frequence_cumule(liste = []):
    "frequence cumules"
    fq = frequence(liste) 

    #s = set(x for x in liste) #on recupere chaque element de facon unique
    #un dictionnaire avec pour cles les elements de s et leurs effectifs cumules qu'on initialise a 0

    cle = [x for x in fq.keys()]
    cle.sort()
    val = [x for x in fq.values()]
    
    fq_c = fq
  
    for i in range(1, len(cle)):
        fq_c[cle[i]] = sum(val[:i+1])
    
    return fq

def coef_p():
    "calcul du coefficient de P"
    pass

#@sys_deco
def init():
    "pour la lecture du fichier par colonne et par ligne"

    l = []

    with open("data_exo_7.txt",encoding="utf-8-sig") as file:
        lignes = file.readlines()
    
    for i in range (len(lignes)):
        
         l1 = lignes[i].split("\t")
         d = enumerate(l1)
         for e, t in d:
             f = {e: t for e in range(len(lignes)) if l1.index(t)==e}
             l.append(f)

    return l

def first_line():
    "Renvoie la premier d'un fichier"

    with open("data_exo_7.txt",encoding="utf-8-sig") as file:
        lignes = file.readlines()
    return lignes[0]


f = init()
index = -1
def retour_index(f, mot):
    "Retourne l'index du mot cle entrer par le user"
    for i in f:
        if mot in i.values():
            index = i.keys()
    return index

def dict_k_to_int(k):
    "Change la cle ou valeur d'un dict en int"
    for el in k:
        i = el
    return i

def trans_liste(liste=[]):
    "change les values de liste en int"
    new_liste = []
    for l in liste:
        new_liste.append(int(l))
    return new_liste

def init_list(mot,f):
    "Initialise une liste selon le mot cle entre"

    liste = []
    index = dict_k_to_int(retour_index(f,mot))

    for el in f:
        if index in el.keys():
            liste.append(dict_k_to_int(el.values()))
    liste.remove(mot)
    return liste           
    
def ecrire_fichier(name, med=0, moy=0, max=0, min=0, p_q=0 ,t_q=0 ,var=0, mode=[]):
    """ Fonction pour ecrire dans le nouveau fichier"""

    new = str(name) + " "+ str(med)+ " "+ str(moy) + " " + str(max) + " " + str(min) + " " + str(p_q)+ " " + str(t_q) + " " + str(var)+ " "+str(mode)+"\n"
    with open("data_res_7.txt",'a+') as file:
        file.write(new)

def lire_fichier():
    with open("data_res_7.txt",'r') as f:
        l = f.readlines()
        for e in l:
            print(e)


@sys_deco
def menu():
    """Cette fonction affiche le menu"""
    
    print( 
          """ \033[32;2;132;220;51;1;48;2m
                             MENU STATISTA
            1-  Calcul de la Moyenne
            2-  Calcul de la Mediane
            3-  Calcul du Max
            4-  Calcul du Min
            5-  Premier Quartile
            6-  Troisieme Quartile
            7-  Calcul du Mode
            8-  Ecart Type
            9-  Variance
            10- Sauvegarder tout
            11- Afficher tout
            12- Nouveau calcul
            13- Quitter
          \033[00m""")

@sys_deco
def quitter():
    exit( """ \033[36;2;132;220;51;1;48;2m
                Bye Bye !!! 
                MERCI DE VOTRE ATTENTION :-)
                \033[00m""")

#colonne moyenne mediane min max p_q t_q varaince mode











#f = frequence_cumule([1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4])
#print(f)

