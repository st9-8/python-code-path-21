#------------------------------ Module built-in ---------------------------------
from random import choice
#--------------------------------------------------------------------------------
#----------------------------------------- Fonctions ---------------------------------------------------#
def Jouer(motTrouve,motMistere):
    cpt = 6
    print("Jeu du pendu".center(70,"-"))
    print(f"Vous avez {cpt} tentatives")
    while motTrouve != motMistere and cpt > 0:
        i = 0
        motMistere = list(motMistere)
        motTrouve = list(motTrouve)
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
        if lettre in trace: 
            print(trace)
            pass
        else: 
            cpt = cpt - 1
        trace.append(lettre)
        print(f"plus que {cpt}!")

    if motTrouve == motMistere:   
        print(f"bravo!! Le mot a trouver etait {motMistere}")
    else:  
        print(f"dommage:( Le mot a trouver etait {motMistere}")
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
trace = [] # Liste qui garde les entrees du joueur


Jouer(motTrouve, motMistere)

#choix = input("Jouer a nouveau?(oui/non):  ")
# -------------------------- Menu facultatif --------------------------- # 
"""while choix != "non": 
    while choix != "oui":  
        print("Votre choix doit etre soit 'oui' ou 'non': ")
        choix = input("Jouer a nouveau?(oui/non):  ")
    Jouer(motTrouve, motMistere)
"""# ----------------------------------------------------------- # 

