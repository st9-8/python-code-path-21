import random

def ch_aleatoire(list):###fonction qui choisit aleatoirement un element dans une liste
    return random.choice(list)
ans = ["pierre","feuille","ciseau"]
def Menu():
    print("1-pierre\n"
          "2-feuille\n"
          "3-ciseau\n")
    choix = input("faites votre choix")
    try:##gestion des erreurs: si choix n'est pas un chiffre du menu
        choix = int(choix)
        if choix not in range(1,4):
            print("ERREUR , la valeur n'est pas dans l'intervalle 1 a 3")
        else:
          return choix
    except:
        print("la vie ce n'est pas le piege")
        print("veillez entrer un chiffre compris entre 1 et 3")
point = [0,0]###liste des points position 0 point du joueur ,position 1 point de l'ordi

def quit(b,n):##fonction quitter
    if b == True:
       if point[0] > point[1]:
           print("\nvous avez gagne en {} coups".format(n))
       elif point[0] < point[1]:
            print("\nj'ai gagne en {} coups".format(n))
       else:
           print("egalite en {} coups".format(n))
    if b == False:
        pass
############main############

print("Jeu: Pierre-Feuille-Ciseau\n")
num_essai = 0
quitter = False

while quitter == False:
        num_essai += 1 #nombre d'essai

        ch = Menu()
        os = ch_aleatoire(ans)
        if (ch == 1 and os == "ciseau") or ( ch == 2 and os == "pierre") or (ch == 3 and os == "feuille"):
            point[0] += 1
            print("Mon choix etait", os)
        elif (os == "pierre" and ch == 3) or (os == "feuille" and ch == 1) or (os == "ciseau" and ch == 2):
            point[1] += 1
            print("Mon choix etait", os)
        elif (os == "pierre" and ch == 1) or (os == "feuille" and ch == 2)or (os == "ciseau" and ch == 3):
            print("Mon choix etait", os)
            print("egaux , refaisons un essai")
        else:
            pass
        print("joueur1 a {} points et l'ordi {} points".format(point[0], point[1]))

        b=input("voulez-vous quitter\n,1-oui \t 2-non")
        while b != "1" and  b != "2":#test si la personne entre bien 1 ou 2
            b=input ("Entrer 1 ou 2")
        b=int(b)
        if b == 1:
            quitter = True
        quit(quitter,num_essai)