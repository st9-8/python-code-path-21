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


def demande_du_Joueur(mot=[]):
    print(mot)
    for lettre in range(len(mot)):
        essaie = 0
        reste = 6
        print(mot[lettre])
        choix_utilisateur = input("veuillez deviner votre lettre \n")
        occurence_de_la_lettre = 1
        if choix_utilisateur != mot[lettre]:
            while choix_utilisateur != mot[lettre] and essaie < 5:
                choix_utilisateur2 = choix_utilisateur
                choix_utilisateur = input("veuillez deviner la lettre \n")
                reste = --reste
                print("il vous reste:", reste, "essaie")
                essaie = ++ essaie
            else:
                if essaie == 6:
                    print("vous avez perdu")

                elif choix_utilisateur == choix_utilisateur2:
                    occurence_de_la_lettre = occurence_de_la_lettre + 1
                    print("vous avez deja mis cette lettre \n")
                    print("devinez encore \n")
                    if occurence_de_la_lettre > 1:
                        print(occurence_de_la_lettre)

                else:
                    pass

    print("vous avez gagner")


demande_du_Joueur(nouveau)
