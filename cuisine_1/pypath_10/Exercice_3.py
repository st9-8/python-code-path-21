# -*-coding:Utf-8 -*
from random import choice

liste = ['pierre', 'feuille', 'ciseau'] #Liste des choix possible
print("\t\tEXERCICE 3\n")
c = 'oui'
score = 0
nb_tours = 0
choix = str()
while c.lower() == 'oui':
    print("\t--> Pierre\n\t--> Feuille\n\t--> Ciseau\n\n\t***Bon choix: +1\n\t***Mauvaix choix: +0") #zone de choix pour le joueur
    
    while (choix != 'pierre' and choix != 'feuille' and choix != 'ciseau'): #Condition permettant de sécuriser la saisie du joueur
        choix = input("\t>>> Faites votre choix: ")
        choix = choix.lower()

    rd = choice(liste)

    if choix == rd:
        print("\n\t*$*Vous avez gagné !*$*")
        score += 1
    else:
        print("Oups! vous avez perdu")
    
    nb_tours += 1
    print("\n\t>>> Voulez-vous jouer un tours de plus ?\n\t(oui \ non)")
    c = input("\t>>> ")
    try:
        c = c.lower()
        assert c == 'oui' or c == 'non'
    except AssertionError:
        print("\t>>> Erreur de saisie")

print("\n\t%PARTIE TERMINÉ%\n\t--> Score: "+str(score)+"\n\t--> Nombre de tour(s): "+str(nb_tours)+"\n\n\t>>> A Bientôt!")