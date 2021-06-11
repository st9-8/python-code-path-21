import random


# Design.
print("\n ------------------------ Exercice 4 --------------------------- ")
print(" ------------------------  Partie 2 ---------------------------- \n\n")
print("----------------------- !! JEU DU PENDU !! ------------------------- \n\n")




# Partie 1 : choisir un mot aleatoire dans la liste du dictionnaire SOWPODS.
def choix_aleatoire():
    # J'ouvre le fichier
	with open("sowpods.txt","r") as f:
		# je recuperes toutes les lignes du fichier, je choisis une de ces lignes aleatoirement et je l'affiche.
		return random.choice(f.readlines())

# Partie 2 : le joueur doit deviner le mot.
def deviner_le_mot():
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
	print("Mot masqué : {}".format(mot_deja_deviné))
	# Liste des lettres minuscules de l'alphabet.
	lettres_minuscules = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	liste_des_lettres_incorrectes = []
	liste_des_lettres_autres_fois_correctes = []
	# Boucle dans la quelle le joueur va chercher à trouver le mot.
	while("-" in mot_deja_deviné):
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
				print(" Vous avez deja entré cette lettre. \n Il n'existe plus d'occurence.")
				continue
			else:
				print(" Cette lettre ne fait pas partie du mot. \n Evitez d'entrer cette lettre pour maximiser vos chances.")
				continue
		# Si la lettre n'appartient pas au mot choisi.
		if(lettre_choisie_par_le_joueur not in mot_choisi):
			print(" Incorrect ! ")
			# je stocke les valeurs entrees par le joueur pour gerer les redondances.
			liste_des_lettres_incorrectes.append(lettre_choisie_par_le_joueur)
		# Si la lettre appartient je la localise dans le mot.
		else:
			# je stocke les valeurs entrees par le joueur pour gerer les redondances.
			liste_des_lettres_autres_fois_correctes.append(lettre_choisie_par_le_joueur)
			# Je convertis la chaine contenant le mot choisi en liste pour pouvoir facilement manipuler
			mot_choisi = list(mot_choisi)
			# je recupere l'indice de la lettre entree par le joueur.
			index_de_la_lettre_entree = mot_choisi.index(lettre_choisie_par_le_joueur)
			# Je remplace la lettre deja trouvee par un caractere autre que celui qu'on peut trouver dans ces mots pour pouvoir gerer la redondance certaines lettres.
			mot_choisi[index_de_la_lettre_entree] = '*'
			# je met la lettre entree par le joueur dans sa bonne position dans la chaine mot_deja_deviné en utilisant une liste car je ne peux pas directement modifier la chaine de caractere.
			# Je convertis d'abord la chaine mot_deja_deviné en liste pour pouvoir la modifier
			mot_deja_deviné = list(mot_deja_deviné)
			# je modifie la liste c'est a dire ke remplace le tiret par la lettre trouvee par le joueur.
			mot_deja_deviné[index_de_la_lettre_entree] = lettre_choisie_par_le_joueur
			# j'initialise la chaine dans la quelle je vais copier toute la liste apres
			chaine_tempo = ""
			# je parcours la liste pour pouvoir la copier dans une chaine.
			for i in mot_deja_deviné: 
				chaine_tempo = chaine_tempo + i
			# je reconvertis la liste en chaine
			mot_deja_deviné = str(mot_deja_deviné)
			# je recopie maintenant les valeurs de la liste dans la  chaine. et la j'obtiens la chaine que j'avais au depart mais modifiee.
			mot_deja_deviné = chaine_tempo
			# J'affiche le mot deja deviné au joueur au fur et à mesure.
			print(" ",mot_deja_deviné)
	# Je felicite le joueur.
	print(" Bravo !! Vous avez trouvé le mot.")

deviner_le_mot()
