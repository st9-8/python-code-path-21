#------------------------------ Module built-in ---------------------------------
from random import choice
#--------------------------------------------------------------------------------
#----------------------------------------- Fonctions ---------------------------------------------------#
def Jouer(motTrouve, motMistere):  
    while motTrouve != motMistere:
        i = 0
        motMistere = list(motMistere)
        motTrouve = list(motTrouve)
        print("Jeu du pendu".center(70,"-"))
        lettre = input("Entrez une lettre du mot a deviner: ")
        while i < taille: 
            if motMistere[i] == lettre:
                motTrouve[i] = lettre
            else:  
                pass
            i = i + 1
        motTrouve = ''.join(motTrouve)
        motMistere = ''.join(motMistere)
        print(motTrouve)
        print("=".center(70,"-"))
        
    print(f"bravo!! Le mot a trouver etait {motMistere}")
#--------------------------------------------------------------------------------------------------------#
# -------------------------- Lecture du dictionnaire --------------------------- # 
with open("sowpods.txt",'r') as fichier: 
    dictionnaire = fichier.readlines()
    dictionnaireTemporaire = []
    for element in dictionnaire:
        dictionnaireTemporaire.append(element.strip("\n"))
    dictionnaire = dictionnaireTemporaire
# ------------------------------------------------------------------------------- #
motMistere = choice(dictionnaire) #Generation aleatoire d'un mot
motTrouve = []
for element in motMistere:
    motTrouve.append("_")
motTrouve = ''.join(motTrouve)
taille = len(motMistere)

Jouer(motTrouve, motMistere)