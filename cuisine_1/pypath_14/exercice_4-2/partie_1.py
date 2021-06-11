"""
ce fichier contient la fonction qui permet de choisir un mot au hasard
dans une liste de mots du dictionnaire SOWPODS.
"""

import random

def choisir_mot() : 
    """
        fonction permettant de choisir un mot au hasard dans notr dictionaire

    """
    try :

        liste_mots = [mot.strip() for mot in open("sowpods.txt", encoding="utf-8")]
        mot = random.choice(liste_mots).lower()
        return mot 
    except:
        print("Nous  avons pas pu ouvrir le fichier")
        print("1-verifier si le fichier est existant")
        print("2-si le fichier existe rassurer vous qu'il se trouve dans la meme dossier que ce code")

#print(choisir_mot())