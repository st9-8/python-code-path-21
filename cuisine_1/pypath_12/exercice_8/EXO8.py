import numpy
import string
import random
import colorama

#.........definir la fonction d'encodage tenant compte de la table ASCII
def encodage():
    message=''
    for i in range(len(texte)):
        A=texte[i]
        if A!=' ':
            message+=chr((ord(A)+int(clé)-96)%26+96)
        else:
            message+=' ' 
    return print(message)

#.........definir la fonction de décodage tenant compte de la table ASCII                
def decodage():
    message=''
    for i in range(len(texte)):   
            A=texte[i]
            if A!=' ':
                message+=chr((ord(A)+int(clé)-96)%26+96)
            else:
                message+=' ' 
    return print(message)


#.........programme principal

print("\n BIENVENUE DANS L'ALGORITHME DU CHIFFREMENT DE CESAR")
print('-------------------------------------------------------')
      #...........afficher un menu
print("""
****** MENU ******

1. ENCODAGE
2. DECODAGE
""")

while True:
      #...........aprés le choix,l'utilisateur entre son texte
   choix=input('\n Voulez vous encoder ou decoder votre texte? Faites un choix: ')
   texte=input('\n Veuillez saisir votre texte -----> : ')
   print('\n votre texte est bien : ',texte)
   
   if choix=='1':
        print(choix,' -------> ENCODAGE')
        print('\n La clé represente le nombre de décalage que vous voulez effectuer')
        print('\n Votre clé peut varier de 1 a 26')
        clé=input('\n Entrer une valeur: ')
        if int(clé)<26:
            print('.............................')
            encodage()
        else:
            print('\n Entrez une valeur inferieure a 26')
            
   elif choix=='2':
        print(choix,' -------> DECODAGE')
        print('\n La clé represente le nombre de décalage que vous voulez effectuer')
        clé=input('\n Entrer une valeur: ')
        if int(clé)<26:
            print('.............................')
            decodage()
        else:
            print('\n Entrez une valeur inferieure a 26')
   else:
        print('\n Entrer une valeur correcte')

