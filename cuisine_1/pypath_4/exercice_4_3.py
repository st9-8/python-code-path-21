import random   #on utilise random pour le choix aléatoire
print("\n\n  ----------------------- \n Bienvenue au jeu du Pendu")
words = [word.strip() for word in open("sowpods.txt", encoding="utf-8")] #on recupère les mots dans une liste en enlevant les espaces autour de ceux-ci avec Strip()
mot_secret = random.choice(words)   #choix au hasard d'un mot
score = ""
recherche = ""
essaie = 6       #Nombre de tentative autorisé pour le joueur
while essaie > 0:      #nombre de tentatives
    print("\n ****** Mot à deviner: ", score, "******")
    proposition = input("\n proposez une lettre en minuscule : ")     #le joeur entre une lettre
    proposition = proposition.upper()
    if proposition in mot_secret:
        if proposition in recherche :     #on vérifie si la lettre est déjà trouvé
            print("\n Tu as déjà trouver cette lettre, essaies encore")
        else :
            recherche = recherche + proposition  #la lettre est dans le mot secret
            print("\n -> Bravo ! Tu y es presque")
            essaie -= 0
    else :
        print("\n -> C'est pas la bonne, essaies encore")
        essaie -= 1
        print(" -> Il te reste ", essaie, "tentative(s)")
    score = ""
    for x in mot_secret:     #on affiche les lettres déjà trouvées et ceux qui manquent par un "_"
           if x in recherche:
               score += x + " " 
           else:
               score += "_ "
    if "_" not in score:      #on vérifie si on a trouvé le bon mot
      print("\n\n Waouh, tu as Gagné!")
      break
    if essaie == 0 :
        print("\n \n Tus perdu la partie ")
print("\n\n Fin de la partie, le mot est ", mot_secret, "\n Merci d'avoir joué")
