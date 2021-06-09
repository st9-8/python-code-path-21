import numpy
import random
import csv

def choixmot() :                       #fonction pour choisir un mot aléatoirement
    with open("sowpods.txt")as f:            #on ouvre le dictionnaire pour le lire
        lines=csv.reader(f,delimiter=',')
        liste=list(lines)
        hasard = random.randint(0,len(liste)-1)
        motchoisi = liste[hasard]   
        print ("\n Un mot a été choisi parmi la base de donnée\n")
    return motchoisi                       #on retourne le mot


def motmasqué(motchoisi) : #fonction    pour le mot masqué et le nombre de vies
    reponse = ""      #variable de type str vide
    lettres = []      #variable de type list vide
    essais = 6          #nombre d'essais

    while reponse.upper()!=str(motchoisi) and essais!=0 :
        reponse = "" #la variable est vide 
        L=input('devinez votre lettre (en minuscule): ') #l'utilisateur doit entrer une lettre a tester
        lettres.append(L)                       #on ajoute cette lettre aux autres lettres deja testé
        print('Lettre entrée: '+L)              #on affiche la lettre 
        essais=nombre_vies(motchoisi,L,essais )                 
        X=str(essais)                         #on transforme le nombre d'essais en str
        while len(L)!=1:                        #on verifie que l'utilisateur a vraiment entrer une lettre
            L=input('Entrer une SEULE lettre a tester: ')#on affiche un message d'erreur  
            lettres.append(L)                            
        for L in motchoisi:                                
            if L in lettres :                   #on verifie si la lettre entré est deja dans laliste deja presente
                reponse = reponse + L.upper()  
            elif L=='-':                        #on verifie si la lettre entré est dans le mot masqué 
                reponse=reponse + L            #on ajoute à la réponse affiché la lettre correcte 
            else :                              
                reponse = reponse + "_ "           #sinon on laisse le lettre masqué 
        print("Les lettres déja proposées sont:",lettres)        
        print(reponse)                          #on affiche le mot 
        print('Il vous reste '+X+' essais\n') #on affiche le nombre d'essais qui reste
    if reponse==str(motchoisi) and essais!=0 : #si le mot est correct et que le nombre d'erreur n'est pas 0 
        print("Vous avez deviné le mot","\'",motchoisi,"\'","!") #on dit a l'utilisateur qu'il a deviné le mot
        print('\n')
        revenir()
        
    if reponse!=str(motchoisi) and essais==0:                #si le mot n'est pas correct et que le nombre d'erreur est 0 
        print("Perdu le mot à trouver était","\'", motchoisi,"\'") #on affiche le bon mot et on dit a l'utilisateur qu'il n'a pas deviné le mot
        revenir()
       

def nombre_vies(motchoisi,L,essais) :                 #fonction pour definir le nombre d'essais 
    if L in motchoisi :        #si la lettre proposé est dans le mot demandé alors le nombre d'essais reste le meme 
        essais=essais                        #le nombre de vies ne change pas 
    elif len(L)!=1:                      #si le joueur entre plusieurs lettres
        essais=essais                         #le nombre de vies ne change pas              
    else :
        essais=essais-1                       #si l'utilisateur entre une lettre incorrecte le nombre d'essais diminue de 1
    return essais                          #on retourne le nombre d'essais 

def revenir():
    menu2 = {}
    menu2['1']="CONTINUER" 
    menu2['2']="QUITTER"

    print('SUITE: ',menu2)
    recommencer=input("\n ---------> Entrer une lettre pour recommencer:") #on propose de rejouer
    if type(recommencer)==str(1):                              
        motchoisi=choixmot()                        #on appelle les fonctions du jeu
        motmasqué(motchoisi)
    elif type(recommencer)==str(2):
        exit()
    else:
        print('\n Choix invalide')
        exit()

    
#programme principal
        
print('******BIENVENUE DANS LE JEU DU PENDU******')
print('--------------------------------------------')
print('\n')
nom = input("--------> Veuillez entrer le nom de joueur:")        #le joueur entre son nom
print ("Salut, " + nom, "!!!!!!!!!!!!!!!!")  
print ("\n")
print ('\n ++ Des mots sont tirés au sort parmi une base de donnée.')      #on enumere les principes du jeu
print ('\n ++ les lettres sont remplacées par des tirets.')
print("\n ++ Le but du jeu est d'essayer de retrouver le mot.")
print("\n ++ Vous devez saisir vos réponses lettres par lettre ou avec l'intégralité du mot.")
print("\n ++ Les majuscules et les caractères spéciaux (accents,...) sont volontairement omis pour plus de facilité.\n")

#le menu pour debuter le jeu
menu1 = {}
menu1['1']="JOUER" 
menu1['2']="QUITTER"

print('MENU: ',menu1)
choix=input('\n--------------> Entrer votre choix: ')
if choix==str(1):
    motchoisi=choixmot()                        #on appelle les fonctions du jeu
    motmasqué(motchoisi)
elif choix==str(2):
    exit()
else:
    print('\n Faites un choix valide')
