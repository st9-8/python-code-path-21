from ast import Str
import random
nom = input("veuillew saisir votre nom\n")
user_victoires = 0
pc_victoires = 0
nuls = 0
kai = 0
while True:
    coupJoueur = input('entrez votre coup : (p)ierre , (f)euille , (c)iseaux ou (q)uitter:')
    if coupJoueur == "q":
        print("vous avez quitté le jeu")
        print(nom," : " , user_victoires , " nuls : " , nuls , " Pc : " , pc_victoires)
        break
    if coupJoueur != "p" and coupJoueur != "f" and coupJoueur != "c":
        continue
    if coupJoueur == "p":
        kai = 1
        print("Pierre contre ...." , end = " ")
    elif coupJoueur == "f":
        kai = 2
        print("Feuille contre ...." , end = " ")
    else:
        kai = 3
        print("Ciseaux contre ... " , end = " ")
    coupPC = random.randint(1,3)
    if coupPC == 1:
        print("PIERRE")
    elif coupPC == 2:
        print("Feuille")
    else:
        coupPC == 3
        print("Ciseaux")

    if kai == coupPC:
        print("Match nul")
        nuls += 1
    elif kai == 1 and coupPC == 3:
        print("Vous remportez la partie")
        user_victoires +=1
    elif kai == 2 and coupPC == 1:
        print("Vous remportez la partie")
        user_victoires +=1
    elif kai == 3 and coupPC == 2:
        print("Vous remportez la partie")
        user_victoires +=1
    elif kai == 1 and coupPC == 2:
        print("Vous perdez la partie")
        pc_victoires +=1
    elif kai == 2 and coupPC == 3:
        print("Vous perdez la partie")
        pc_victoires +=1
    elif coupJoueur == "c" and coupPC == "p":
        print("Vous perdez la partie")
        pc_victoires +=1
