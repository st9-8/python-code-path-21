import random       #on importe le module random
l = ["pierre", "feuille", "ciseau"]      #la liste des mots du jeu
print(l)
i = 0       #score de la partie
p = "y"     #condition d'arrêt
while p == "y":
    j = random.choice(l)        #choix du mot du sytème
    x = input("veillez entrer votre choix ")        #le joueur entre son mot
    if x == "pierre" and j == "pierre" or x == "feuille" and j == "feuille" or x == "ciseau" and j == "ciseau":
        print("mot identique, match nul", x, "contre", j)       
        k=0
    elif x == "pierre" and j == "ciseau":
        print("votre choix est gagnant ", x, "contre", j)
        k=1
    elif x == "feuille" and j == "pierre":
       print("votre choix est gagnant ", x, "contre", j)
       k=1
    elif x == "ciseau" and j == "feuille":
        print("votre choix est gagnant ", x, "contre", j)
        k=1
    else:
        print("vous avez perdu la partie ", x, "contre", j)
        k=0
    i = i+k
    
    p=input("appuyer sur Y pour continuer ou sur tout autre touche pour quitter la partie ")
print("votre score durant la partie est ", i)
