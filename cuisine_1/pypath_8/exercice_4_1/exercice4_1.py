from parti_3 import *

#MENU
print("""
*MENU PENDU*
\n
Devinez les lettres d'un mot
\n
1- Nouvelle partie
2- Quitter
""")

choix = input("Entrez votre choix: ")
choix = int(choix)
while choix not in [1,2]:
    input("entrer un choix valide ")

if choix == 1:
    jouer()

    print("""
*MENU PENDU*
\n
Devinez les lettres d'un mot
\n
1- Nouvelle partie
2- Quitter
""")

choix = input("Entrez votre choix: ")
choix = int(choix)

if choix == 2:
    print("BYE!!!")
    