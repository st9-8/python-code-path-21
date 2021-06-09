#Partie 1

from random import choice

def mot(): # choix aleatoire dans la liste
    with open("SOWPODS.txt", 'r') as file:
            lignes=file.readlines()
            mot=choice(lignes).strip('\n')
    return mot

#partie 2
def affichage(word): #pour ecrire espace
    f=" ".join(word) #transformer liste en string

    return f

def getPosition(terme,lettre): #renvoie les occurences de la lettre dans le mot
    liste=[pos for pos,c in enumerate(terme) if lettre==c]   
    return liste

def replace(terme,liste,nouvelle_lettre): # remplace la lettre dans le mot aux positions fournies dans la liste
    for i in range(len(terme)):
        if i in liste:
            terme[i]=nouvelle_lettre
    return "".join(terme)

def deco(funct):  # decorateur
    print("Bienvenue au ",funct.__name__)
    return funct

@deco    
def Pendu():
    lettre_devines=set() # l'ensemble des lettres trouvees
    terme=mot()
    mot_devine=['_' for car in terme]
    mot_devine="".join(mot_devine)
    while(mot_devine!=terme):
        print(affichage(mot_devine))
        lettre=input("Choisissez votre lettre\n")
        lettre_devines.add(lettre) #stocker la lettre
        if lettre in terme:
            liste=getPosition(terme,lettre)
            mot_devine=replace(list(mot_devine),liste,lettre)
        else:
            print("Incorrect")
    print(affichage(mot_devine))   
            

    
Pendu()
