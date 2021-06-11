import random



#PARTI 1: random choice dans un fichier

def random_read_file(file):
    with open(file, 'r') as f:
        line = f.readlines()
        mot = random.choice(line)
    return mot.strip("\n")

#PARTI 2: le jeu

#fonctions utiles
def str_to_liste(l = ""):
    "permet de transformer une chaine de caractere en une liste"
    liste = []
    for el in l:
        liste.append(el)
    return liste


def list_to_str(liste = []):
    "permet de transformer une liste en une chaine de caractere"
    mot = ""
    for el in liste:
        mot = mot + el
    return mot

def remplacer(liste1 = [], liste2 = []):
    "remplace tous les elements de la liste1 qui ne sont pas dans liste2 par '_'"
    
    for el in liste1:
        if el not in liste2:
            i = liste1.index(el)
            liste1[i] = "_"

def jouer():
    "fonction jouer"
    mot = random_read_file("file.txt")
    mot.split("\n")
    mot = mot.lower()

    trouver = False
    let = []#contient les lettres entrees par le joueur

    new_mot = str_to_liste(mot)

    while trouver == False:
        devine = str_to_liste(mot)
        lettre = input("Devinez la lettre: ")

        if lettre not in new_mot:
            print("Incorrect!!!\n")

        let.append(lettre)

        remplacer(devine,let)
        print(list_to_str(devine))

        if list_to_str(devine) == mot:
            trouver = True
            print("Correcte!!!")
