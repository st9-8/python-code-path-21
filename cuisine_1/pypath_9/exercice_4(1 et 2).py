#Partie 1

from random import choice

def mot(): # choix aleatoire dans la liste
    with open("SOWPODS.txt", 'r') as file:
            lignes=file.readlines()
            mot=choice(lignes).strip('\n')
    return mot
