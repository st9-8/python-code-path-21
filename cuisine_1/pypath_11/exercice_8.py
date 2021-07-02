# Design.
print("\n ------------------------ Exercice 8 --------------------------- \n\n")
print("---------------- !! CHIFFREMENT DE CESAR !! ------------------- \n\n")

# fonction d'encodage qui prend le texte à encoder en paramètre.
def encodage(chaine):
	# dictionaire contenant les codes de toutes les lettres majuscules et minuscules.
	dictionaire_encodage = {"A":"X","B":"Y","C":"Z","D":"A","E":"B","F":"C","G":"D","H":"E","I":"F","J":"G","K":"H","L":"I","M":"J","N":"K","O":"L","P":"M","Q":"N","R":"O","S":"P","T":"Q","U":"R","V":"S","W":"T","X":"U","Y":"V","Z":"W","a":"x","b":"y","c":"z","d":"a","e":"b","f":"c","g":"d","h":"e","i":"f","j":"g","k":"h","l":"i","m":"j","n":"k","o":"l","p":"m","q":"n","r":"o","s":"p","t":"q","u":"r","v":"s","w":"t","x":"u","y":"v","z":"w"}
	# compteur me permettant de parcourir la chaine.
	i = 0 
	#parcours de la chaine.
	while(i!=len(chaine)):
		#Comme l'espace n'a pas d'encodage different, si je tombe sur ca je ne le remplace pas.
		if chaine[i] == " ":
			print(" ", end="")
		else:
		#affichage de l'encodage de chacune des lettres de la chaine.
			print(dictionaire_encodage[chaine[i]], end="") 
		i = i+1

# fonction de decodage qui prend le texte à decoder en paramètre.
def decodage(chaine):
	# dictionaire contenant les codes de toutes les lettres majuscules et minuscules.
	dictionaire_de_decodage = {"X":"A","Y":"B","Z":"C","A":"D","B":"E","C":"F","D":"G","E":"H","F":"I","G":"J","H":"K","I":"L","J":"M","K":"N","L":"O","M":"P","N":"Q","O":"R","P":"S","Q":"T","R":"U","S":"V","T":"W","U":"X","V":"Y","W":"Z","x":"a","y":"b","z":"c","a":"d","b":"e","c":"f","d":"g","e":"h","f":"i","g":"j","h":"k","i":"l","j":"m","k":"n","l":"o","m":"p","n":"q","o":"r","p":"s","q":"t","r":"u","s":"v","t":"w","u":"x","v":"y","w":"z"}
	# compteur me permettant de parcourir la chaine.
	i = 0 
	#parcours de la chaine.
	while(i!=len(chaine)):
		#Comme l'espace n'a pas de decodage different, si je tombe sur ca je ne le remplace pas.
		if chaine[i] == " ":
			print(" ", end="")
		else:
		#affichage de l'encodage de chacune des lettres de la chaine.
			print(dictionaire_de_decodage[chaine[i]], end="") 
		i = i+1


#Menu principal.
# Boucles permettant de realiser plusieurs fois les operations.
# J'initialise choix_2 à "1" pour entrer dans la boucle.
choix_2 = '1' 
while(choix_2 == '1'): 
	# je recupere le choix de l'utilisateur.
	choix = input(" 1. Encoder une phrase. \n 2. Décoder une phrase. \n \n Que voulez-vous faire ?? \n   >> ")
	# test de l'entree de l'utilisateur
	if(choix == '1'):
		chaine = input("Entrez la phrase à encoder. \n   >> ")
		print("L'encodage de {} est : ".format(chaine), end = "")
		# Appel de la fonction correspondante (encodage)
		encodage(chaine)
		# je recupere le choix de l'utilisateur.
		choix_2 = input("\n \n Voulez-vous effectuer une autre operation ?? \n 1. Oui \n 2. Non \n  >> ")
	# test de l'entree de l'utilisateur	
	elif(choix == '2'):
		chaine = input("Entrez la phrase à décoder. \n   >> ")
		print("Le Décodage de {} est : ".format(chaine), end = "")
		# Appel de la fonction correspondante (decodage)
		decodage(chaine)
		# je recupere le choix de l'utilisateur.
		choix_2 = input("\n \n Voulez-vous effectuer une autre operation ?? \n \n 1. Oui \n 2. Non \n  >> ")
	else:
		# je modifie la valeur de choix_2 pour ne plus entrer dans la boucle car le choix est deja indisponble.
		choix_2 = '4'

# test pour savoir si l'utilissateur est sorti du programme par erreur ou non.
if choix_2 == '2':
	print("------------------------------- Fin du programme. ----------------------------")
else:
	print("Choix indisponible !!")

# Fin du programme 
