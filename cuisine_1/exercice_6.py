# Design.
print("\n ------------------------ Exercice 6 --------------------------- \n\n")
print("---------------- !! TRAITEMENT DES NUMEROS !! ------------------- \n\n")

# Fonction qui permet de traiter un numero (le mettre sous la forme de 8 chiffres) pour faciliter le tri 
def traitement(chaine):
	numero_traité = []
	chaine_traitee = ""
	# je convertis d'abord le numero en liste
	chaine = list(chaine)
	# Je l'inverse pour stocker uniquement les  08 derniers chiffres
	liste_inverse = list(reversed(chaine))
	# Je stocke les 08 derniers chiffres dans une liste que je vais inverseer pour avoir le numero en lui meme.
	for i in range(1,9):
		numero_traité.append(liste_inverse[i])
	# Je remets les elements de la liste dans une chaine pour retourner une chaine.
	for j in list(reversed(numero_traité)):
		chaine_traitee = chaine_traitee + j
	# Je retourne la chaine qui est le numero traité.
	return chaine_traitee

	
# Je cree mon decorateur qui prend en parameter la fonction trier()
def mon_decorateur(fonction):
	# je cree donc la fonction qui est celle qui sera decoree.
	def fonction_decoree():
		# J'initialise mes variables. cette liste contiendra tous les numeros standardisés.
		liste_de_numeros_standardisés = []
		# Variable qui va contenir un numero deja standardisé. c'est lui que je copie à chaque fois pour mettre dans le fichier liste_de_numeros_standardisés
		numero_standardisé = ""
		# J'appelle la fonction pour la decore. 
		liste_de_numeros = fonction()
		# Je parcours cette liste de numeros pour standardiser tous les numeros.
		for num in liste_de_numeros:
			numero_standardisé = "+237 6" + num
			liste_de_numeros_standardisés.append(numero_standardisé)
		for numero_correct in liste_de_numeros_standardisés:
			print("  ",numero_correct)
	return fonction_decoree

# J'appelle mon decorateur
@mon_decorateur
# Fonction trier qui prend la liste des numeros en paramètre et trie la liste.
def trier():
	# Liste qui contiendra à la fin la lsite triee dans l'ordre croissant de tous les numeros du fichier.
	liste_de_numeros_traités = []
	# J'ouvre le fichier en lecture pour recuper les numeros.
	with open("data_exo_6.txt","r") as fic:
		# Je lis d'abord la premiere ligne du fichier car elle ne comporte pas un numero
		fic.readline()
		# Ensuite je stocke le reste des lignes (les numeros) dans le fichier liste_de_numeros
		liste_de_numeros = fic.readlines()
		# Ce parcours me permet de traiter tous les numeros c'est à dire les mettres sous la fome de 8 chiffes pour pouvoir les trier et avoir le rsultat escompté
		for numero in liste_de_numeros:
			liste_de_numeros_traités.append(traitement(numero))
	#  Cette liste contient donc la liste des numeros, tous sous le format de 08 chiffres.
	liste_de_numeros_traités = sorted(liste_de_numeros_traités)
	# je retourne la liste des numeros tries.
	return liste_de_numeros_traités

#appel de la fonction.
trier()