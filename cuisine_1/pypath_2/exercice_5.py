import random

tableau = []
with open("sowpods.txt", "r") as f:
    lines = f.readlines()
    for l in lines[1:]:
        tableau.append(l.split()[-1])
        nouveau = random.choice(tableau)


def choix_de_mot():
    tableau = []
    with open("sowpods.txt", "r") as f:
        lines = f.readlines()
        for l in lines[1:]:
            tableau.append(l.split()[-1])
            nouveau = random.choice(tableau)
        print(nouveau)


def demande_du_Joueur(liste=[]):
    print(liste)
    for mot in range(len(liste)):
        print(liste[mot])
        choix_utilisateur = input("veuillez deviner votre lettre \n")
        while choix_utilisateur != liste[mot]:
            choix_utilisateur = input("veuillez deviner la lettre \n")
            choix_utilisateur2 = choix_utilisateur
            if choix_utilisateur == choix_utilisateur2:
                print("vous avez deja mis cette lettre \n")
            else:
                pass
        else:
            ++mot
    print("vous avez gagner")


demande_du_Joueur(nouveau)