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
    trouve = False
    lettres_trouvees = ""
    mot = generer_mot()
    print(mot)
    for lettre in mot:
        mot_cache = mot_cache + "_ "
    
    print("\t*** BIENVENU DANS LE JEU DU PENDU ***")
    
    while trouve is False:
        print("\n\t>>> Mot à deviner : "+ mot_cache)
        lettre_devine = input("\t>>> Devinez une lettre : ")[0:1].upper()

        if lettre_devine in mot:
            if lettre_devine not in lettres_trouvees:
                lettres_trouvees = lettres_trouvees + lettre_devine
                print("\t-> Bien vu!")
            else:
                print("\t-> Attention!!! Lettre deja trouve!")
        else:
            trouve = False
            print("\t-> Incorret")
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
            trouve = True
     
    print("\n\t    *** Fin de la partie ***    ")

play()