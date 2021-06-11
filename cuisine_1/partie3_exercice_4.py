import random


# Design.
print("\n ------------------------ Exercice 4 --------------------------- ")
print(" ------------------------  Partie 3 ---------------------------- \n\n")
print("----------------------- !! JEU DU PENDU !! ------------------------- \n\n")


# Fonction permettant de choisir un mot aleatoire dans la liste du dictionnaire SOWPODS.
def choix_aleatoire():
    # J'ouvre le fichier
	with open("sowpods.txt","r") as f:
		# je recuperes toutes les lignes du fichier, je choisis une de ces lignes aleatoirement et je l'affiche.
		return random.choice(f.readlines())

#Fonction permettant de deviner le mot_choisi
booleen = True
def deviner_le_mot():
	trouver = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]
	# Je stocke le mot choisI dans la chaine mot_choisi.
	mot_choisi = choix_aleatoire() 
	# Compteur permettant de parcourir mot_choisi.
	i = 1
	# J'initialise la chaine qui va me permettre de compter le nombre d'espaces du mot choisi.
	mot_non_deviné = ""
	# Parcours me permettat de connaitre la taille du mot choisi.
	while(i<len(mot_choisi)):
		mot_non_deviné = mot_non_deviné + "-"
		i = i+1
	# Ici le joueur commence à jouer. J'initialise mot_Deja_deviné à mot_non_deviné car le joueur n'a pa sencre trouvé une lettre juste:	
	mot_deja_deviné = mot_non_deviné
	print(" \n Mot masqué : {}".format(mot_deja_deviné))
	# Je declare les listes que je vais utiliser dans cette fonction
	# Liste contenant les lettres que le joueur va entrer mais qui ne font pas parti du mot choisi
	liste_des_lettres_incorrectes = []
	# Liste contenant les lettres qui appartiennent au mot à choisir  mais que le joueur a deja entré
	liste_des_lettres_autres_fois_correctes = []
	# Liste des lettres minuscules de l'alphabet.
	lettres_minuscules = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	# Boucle dans la quelle le joueur va chercher à trouver le mot.
	global booleen
	global verficateur1
	while(("-" in mot_deja_deviné) and (booleen)):
		#Je recupere la lettre entree par le joueur et je fais les tests
		lettre_choisie_par_le_joueur = input("\n Devinez une lettre : ")
		# je previens le joueur que les lettres sont majuscules.
		while(lettre_choisie_par_le_joueur in lettres_minuscules):
			print(" Toutes les lettres du mot sont en majuscules.")
			#Je recupere encore la lettre entree par le joueur et je fais les tests
			lettre_choisie_par_le_joueur = input("\n Entrez une lettre majuscule : ")
		# Test me permettant d'afficher un message different à l'utilisateur
		if(lettre_choisie_par_le_joueur in liste_des_lettres_incorrectes):
			if(lettre_choisie_par_le_joueur in liste_des_lettres_autres_fois_correctes):
				verficateur1 = verficateur1 + 1
				if(verficateur1 == 6):
					booleen = False
				print(" Vous avez deja entré cette lettre. \n Il n'existe plus d'occurence de cette lettre.")
				continue
			else:
				verficateur1 = verficateur1 + 1
				if(verficateur1 == 6):
					booleen = False
				print(" Cette lettre ne fait pas partie du mot. \n Evitez d'entrer cette lettre pour maximiser vos chances.")
				continue
		# Si la lettre n'appartient pas au mot choisi.
		if(lettre_choisie_par_le_joueur not in mot_choisi):
			# je recommence à compter les echecs du joueur
			verficateur1 = verficateur1 + 1
			print(" Incorrect ! ")
			# je stocke les valeurs entrees par le joueur pour gerer les redondances.
			liste_des_lettres_incorrectes.append(lettre_choisie_par_le_joueur)
		# Si la lettre appartient je la localise dans le mot.
		else:
			# je reset la variable
			verficateur1 = 0
			# je stocke les valeurs entrees par le joueur pour gerer les redondances.
			liste_des_lettres_autres_fois_correctes.append(lettre_choisie_par_le_joueur)
			# je recupere l'indice de la lettre entree par le joueur.
			les_indexs = trouver(mot_choisi,lettre_choisie_par_le_joueur)
			# je convertis la chaine en liste pour pouvoir la modifier.
			mot_choisi = list(mot_choisi)
			# je modifie la liste c'est a dire je remplace toutes les occurences de la lettre entree par un caractere different de tout le reste.
			for i in les_indexs:
				mot_choisi[i] = '*'
			# ensuite, je mets la lettre entree par le joueur dans sa bonne position dans la chaine mot_deja_deviné en utilisant une liste car je ne peux pas directement modifier la chaine de caractere.
			# Je convertis d'abord la chaine mot_deja_deviné en liste pour pouvoir la modifier
			mot_deja_deviné = list(mot_deja_deviné)
			# je modifie la liste c'est a dire je remplace le tiret par la lettre trouvee par le joueur dans toutes les occurences de la lettre.
			for i in les_indexs:
				mot_deja_deviné[i] = lettre_choisie_par_le_joueur
			# j'initialise la chaine dans la quelle je vais copier toute la liste apres
			chaine_tempo = ""
			# je parcours la liste pour pouvoir la copier dans une chaine.
			for j in mot_deja_deviné: 
				chaine_tempo = chaine_tempo + j
			# je recopie maintenant les valeurs de la liste dans la  chaine. et la j'obtiens la chaine que j'avais au depart mais modifiee.
			mot_deja_deviné = chaine_tempo
			# J'affiche le mot deja deviné au joueur au fur et à mesure.
			print(" ",mot_deja_deviné)
		# Test me permettant d'arreter la boucle (si le joueur a deja 6 echecs successifs.)
		if(verficateur1 == 6):
			booleen = False
		if verficateur1 == 3:
			print(" Soyez plus concentrés pour trouver les bonnes lettres. \n  03 echecs succesifs ca fait pas serieux. ")
	# Je teste si le joueur a gagné ou pas
	if(verficateur1 == 6):
		print(" \n -------------- Suite à vos nombreux échecs succesiifs, \n        Vous avez perdu la partie :( ")	
		print(" \n Voulez-vous vanger ou quitter le jeu  ??")
		print("\n  1. Vous venger. \n  2. Quitter le jeu.")
	else:
		# Je felicite le joueur.
		print("\n ---------------------- Bravo !! Vous avez trouvé le mot. :)  ")
		print("\n Voulez-vous lancer une nouvelle partie ou quitter le jeu ??")
		print("\n  1. Lancer une nouvelle partie. \n  2. Quitter le jeu.")

# Menu principal
print(" Bienvenue dans le JEU PENDU. \n Il est question pour vous de deviner un mot en devinant progressivement ses lettres.")
print(" Les mots sont tous en majuscules. \n Soyez meticuleux pour gagner la partie. \n Vous avez peu de chances.")    
print(" !! Bonne chance !! \n ")
# J'initialise choice à "1" pour pouvoir etrer dans la boucle au moins une fois.
choice = "1"
# Boucle permettant de jouer autant de fois.
while(choice == "1"):
	# Je reinitialise mes variables qui me permettent de compter le nombre d'essais du joueur.
	verficateur1 = 0
	booleen = True
	print("\n     PARTIE LANCEE...... \n")
	deviner_le_mot()
	choice = input(" \n   >> ")
print("  ---------------- FIN DU PROGRAMME !! ---------------------")

 # Fin du programme.