#------------------------------ Module built-in ---------------------------------
from random import choice
#--------------------------------------------------------------------------------
#------------------------------ Fonctions ---------------------------------------
def controleurChoixJoueur(choix):
    if choix == "Pierre":
        tmp = 1
    elif choix == "Feuille":
        tmp = 2
    elif choix == 'Ciseau':
        tmp = 3
    else:
        tmp = 4
    return tmp

def controleurJeu(choix):
    if choix == "oui":
        tmp = 1
    elif choix == "non":
        tmp = 2  
    else:
        tmp = 3
    return tmp 
#----------------------------------------------------------------------------------
#------------------------------ Programme principal -------------------------------
#---------------------- Variables -------------------------
listeChoix = ["Pierre","Feuille","Ciseau"] 
score,tmp,partie = 0,0,0
choixJoueur,choixSysteme = "None",'None'
continuer = "oui"
#-----------------------------------------------------------
while continuer != 'non': #Boucle controlant si le joueur continue la partie ou pas
    choixJoueur = input("Entrez votre choix (Pierre,Feuille ou Ciseau): ")
    tmp = controleurChoixJoueur(choixJoueur)
    while tmp == 4: #Boucle controlant que le joueur entre la bonne valeur
        print("Votre choix doit etre soit 'Pierre', 'Feuille' ou 'Ciseau'")
        choixJoueur = input("Entrez votre choix (Pierre,Feuille ou Ciseau): ")
        tmp = controleurChoixJoueur(choixJoueur)

    choixSysteme = choice(listeChoix)
    partie += 1 #Compteur de parties
    print(f" Partie {partie} ".center(50,"="))
    print(f"Systeme: {choixSysteme}")
    print(f"Joueur: {choixJoueur}")
    if choixJoueur=="Pierre" and choixSysteme == "Ciseau":
        score += 1    
    elif choixJoueur=="Feuille" and choixSysteme == "Pierre":
        score += 1
    elif choixJoueur=="Ciseau" and choixSysteme == "Feuille":
        score += 1
    else:
        pass #Dans tout autre cas le joueur ne gagne pas de point

    tmp = 0
    continuer = input("Voulez vous continuer? (oui/non): ")
    tmp = controleurJeu(continuer)
    while tmp == 3: #Boucle controlant que le joueur entre la bonne valeur a propos continuer la partie ou pas
        print("Votre choix doit etre 'oui' ou 'non'!")
        continuer = input("Voulez vous continuer? (oui/non): ")
        tmp = controleurJeu(continuer)

print(" Score ".center(50,"="))
print(f"Score: {score}")
