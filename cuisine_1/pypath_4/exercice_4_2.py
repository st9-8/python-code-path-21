mot_secret = "python"    #on initialise le mot secret
score = ""
lettres_trouvees = ""
print("\n\n  ----------------------- \n Bienvenue au jeu du Pendu")
while True:      #une boucle infini pour que l'utilisateur joue tant qu'il n'a pas trouver le mot
    print("\n ****** Mot à deviner: ", score, "******")
    proposition = input("\n proposez une lettre : ")     #le joeur entre une lettre
    if proposition in mot_secret:
        lettres_trouvees = lettres_trouvees + proposition  #la lettre est dans le mot secret
        print("\n -> Bravo ! Tu y es presque")
    else :
        print("\n -> C'est pas la bonne, essaies encore")
    score = ""
    for x in mot_secret:     #on affiche les lettres déjà trouvées et ceux qui manquent par un "_"
           if x in lettres_trouvees:
               score += x + " " 
           else:
               score += "_ "
    if "_" not in score:    #condition de sortie de la boucle infinie
      break
print("\n\n Waouh, tu as Gagné! ")
print("\n\n Fin de la partie, le mot est ", score, "\n Merci d'avoir joué")
