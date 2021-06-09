# -*-coding:Utf-8 -*
from random import choice

def generer_mot():
    file = open('/home/yvan/Bureau/seed/cuisines/sowpods.txt', "r")
    # La variable "liste_mots" est une liste contenant toutes les lignes du fichier
    liste_mots = file.readlines()
    file.close()
    choix = choice(liste_mots)
    choix = list(choix)
    choix.remove('\n')
    return "".join(choix)

def play():
    mot_cache = ""
    essai = 6
    lettres_trouvees = ""
    mot = generer_mot()
    print(mot)
    for lettre in mot:
        mot_cache = mot_cache + "_ "
    
    print("\t*** BIENVENU DANS LE JEU DU PENDU ***")
    
    while essai > 0:
        print("\n\t>>> Nombre d'essai possibles: "+str(essai))
        print("\n\t>>> Mot à deviner : "+ mot_cache)
        lettre_devine = input("\t>>> Devinez une lettre : ")[0:1].upper()

        if lettre_devine in mot:
            if lettre_devine not in lettres_trouvees:
                lettres_trouvees = lettres_trouvees + lettre_devine
                print("\t-> Bien vu!")
            else:
                print("\t-> Attention!!! Lettre deja trouve!")
        else:
            essai = essai - 1
            print("\n\t-> Incorret\t -1 essai")
            if essai <= 6:
                print("\t ==========Y= ")
            if essai <= 5:
                print("\t ||/       |  ")
            if essai <= 4:
                print("\t ||        0  ")
            if essai <= 3:
                print("\t ||       /|\ ")
            if essai <= 2:
                print("\t ||       / \  ")
            if essai <= 1:                    
                print("\t/||           ")
            if essai <= 0:
                print("\t==============\n")
                print("\t>>> #-#Vous avez perdu#-# <<<")


        mot_cache = ""
        for x in mot:
            if x in lettres_trouvees:
                mot_cache += x + " "
            else:
                mot_cache += "_ "

        if "_" not in mot_cache:
            print("\t>>> *.* *.* *.* *.* *.* *.*")
            print("\t>>> *.* *.* *.* *.* *.* *.*")
            print("\t>>> *$*Mot trouvé: "+mot_cache+" *$* <<<")
            print("\t>>> *$*Vous avez Gagné!*$* <<<")
            print("\t>>> *.* *.* *.* *.* *.* *.*")
            print("\t>>> *.* *.* *.* *.* *.* *.*")

            break
     
    print("\n\t    *** Fin de la partie ***    ")

play()