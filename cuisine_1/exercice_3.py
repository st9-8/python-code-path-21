import random


# Design.
print("\n ------------------------ Exercice 3 --------------------------- \n \n ")
print("----------------- !! PIERRE - PAPIER - CISEEAU !! ----------------------- \n\n")


# Fonction permettant de choisir un mot aleatoire dans la liste des trois mots.
def choix_aleatoire():
	liste_des_mots = ["Pierre" , "Feuille" , "Ciseau"]
	# je recuperes toutes les lignes du fichier, je choisis une de ces lignes aleatoirement et je l'affiche.
	return random.choice(liste_des_mots)

def score(entier):
	score_du_joueur = 0
	choix_du_systeme = choix_aleatoire()
	if entier == 1 :
		if choix_du_systeme == "Feuille":
			score_du_joueur = 1
	elif entier == 2 :
		if choix_du_systeme == "Pierre":
			score_du_joueur = 1
	elif entier == 3 : 
		if choix_du_systeme == "Ciseau":
			score_du_joueur = 1
	return score_du_joueur

# Menu principal
# J'initialise choice à 1 pour pouvoir etrer dans la boucle au moins une fois.
choice = "1"
score_j = 0
# Boucle permettant de jouer autant de fois.
while(choice == "1"):
	print(" Choisissez un mot parmi les 03 suivants et tentez de gagner...")
	print("    1. Ciseau. ")
	print("    2. Feuille. ")
	print("    3. Pierre. ")
	print("\n Entrez votre choix : ")
	choix_du_joueur = input("  >> ")
	while(choix_du_joueur != '1' and choix_du_joueur != '2' and choix_du_joueur != '3'):
		print(" \n Choisissez soit le 1, le 2 ou le 3. ")
		choix_du_joueur = input("  >> ")
	choix_du_joueur = int(choix_du_joueur)		
	score_j = score(choix_du_joueur) + score_j
	print(". . . .  .. .. ..  ... ... .... ................ fin du tour.")
	print("\n Voulez-vous rejouer ?? \n")
	print("    1. Oui. ")
	print("    2. Non. ")
	choice = input(" \n   >> ")
if score_j > 1:
	print(" Votre score est de {} points \n".format(score_j))
else : 
	print(" Votre score est de {} point \n".format(score_j))

print("  ---------------- FIN DU PROGRAMME !! ---------------------")

 # Fin du programme.