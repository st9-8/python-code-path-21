import numpy
import random


#-----------------fonction qui definit le choix du mot dans un dictionnaire
def choixmot() :                       
    f=open('sowpods.txt','r')                   
    line= random.randrange(0,267000)      
    for n in range (0,line):             
        motchoisi=f.readline().replace('\n','')   
    f.close()                            
    return motchoisi                           

#---------------------fonction pour le mot masqué et le nombre de vies
def motmasqué(motchoisi) :            
    rep = ""                         
    lettres = []               #une variable liste
    essais = 6                #on defini ici le nombre d'essais

    while rep.upper()!=motchoisi.upper():
        if essais!=0 :
            rep = "" 
            L=input('------> Devinez votre lettre (en minuscule): ') #l'utilisateur doit entrer une lettre a tester
            lettres.append(L)                       #on ajoute cette lettre aux autres lettres deja testé
            print('\n Vous avez entré: '+L)              #on affiche la lettre 
            essais=nombre_vies(motchoisi,L,essais )                 
            X=str(essais)                             #on converti le nombre d'essais en str
            while len(L)!=1:                        #on verifie que le joueur n'a pas entré plusieurs lettres
                L=input('SVP Entrer une SEULE lettre: ')  #sinon affiche un message d'erreur  
                lettres.append(L)                            
            for L in motchoisi:                                
                if L in lettres :                   #on verifie si la lettre entré est deja dans la liste deja presente
                    rep = rep + L.upper()  
                elif L=='-':                        #on verifie si la lettre entré est dans le mot masqué 
                    rep=rep + L.upper()           #on ajoute à la réponse affiché la lettre correcte 
                else :                              
                    rep = rep + "_ "           #sinon on laisse la lettre masqué 
            print("Les lettres déja proposées sont:",lettres)        
            print(rep)                          #on affiche le mot 
            print('Il vous reste '+X+' essais\n') #on affiche le nombre d'essais qui reste

        elif essais==0:                #si le mot n'est pas correct et que le nombre d'erreur est 0
            print("Perdu le mot à trouver était","\'", motchoisi.upper(),"\'") #on affiche le bon mot et on dit a l'utilisateur qu'il n'a pas deviné le mot
            pendu_final = r"""
        --------------
            |        |
            |        |
            |       / \
            |       \_/
            |      __|__
            |        |
            |        |
            |       / \
           /|\     /   \
          / | \
         /  |  \
         ~~~~~~~~~~~~~~~~~~~~~
         ~~~~~~~~~~~~~~~~~~~~~
         ~~~~~~~~~~~~~~~~~~~~~
                         """

            print(pendu_final)
            revenir()
    if rep.upper()==motchoisi.upper():
        if essais!=0 : #si le mot est correct et que le nombre d'erreur n'est pas 0
            print("Vous avez deviné le mot","\'",motchoisi.upper(),"\'","!") #on dit a l'utilisateur qu'il a deviné le mot
            print(' _  _    .  _ . _ _  _  _ _ .  _      ') 
            print('|_ |_ |  | |  |  |  |_|  |  | | | |\ |')
            print('|  |_ |_ | |_ |  |  | |  |  | |_| | \|')
            print('\n')
            revenir()
        
       
#-----------------------------fonction pour definir le nombre d'essais
def nombre_vies(motchoisi,L,essais) :                  
    if L in motchoisi :        #si la lettre proposé est dans le mot demandé alors le nombre d'essais reste le meme 
        essais=essais                        #le nombre de vies ne change pas 
    elif len(L)!=1:                      #si plusieurs lettres sont entréespar le joueur
        essais=essais                                     
    else :
        essais=essais-1                       #si l'utilisateur entre une lettre incorrecte le nombre d'essais diminue de 1
    return essais                          #on retourne le nombre d'essais 

#--------------------fonction pour recommencer un nouveau tour
def revenir():
    menu2= r"""
    1 = CONTINUER 
    2 = QUITTER
              """

    print('SUITE: \n',menu2)
    recommencer=input("\n ---------> Entrer une lettre pour recommencer: ") #on propose de rejouer
    if recommencer ==str(1):                              
        motchoisi=choixmot()                        #on appelle les fonctions du jeu
        motmasqué(motchoisi)
    elif recommencer ==str(2):
        exit()
    else:
        print('\n Choix invalide')
        exit()

    
#-------------------------------programme principal
        
print('******BIENVENUE DANS LE JEU DU PENDU******')
print('--------------------------------------------')
print('\n')
nom = input("--------> Veuillez entrer le nom de joueur: ")        #le joueur entre son nom
print ("Salut, " + nom, "!!!!!!!!!!!!!!!!")  
print ("\n")
print ('\n ++ Des mots sont tirés au sort parmi une base de donnée.')      #on enumere les principes du jeu
print ('\n ++ les lettres sont remplacées par des tirets.')
print("\n ++ Le but du jeu est d'essayer de retrouver le mot.")
print("\n ++ Vous devez saisir vos réponses lettres par lettre ou avec l'intégralité du mot.")
print("\n ++ Les majuscules et les caractères spéciaux (accents,...) sont volontairement omis pour plus de facilité.\n")

#-----------------------le menu pour debuter le jeu
menu1 = r"""
1 = JOUER 
2 = QUITTER
         """

print('MENU: \n',menu1)
choix=input('\n--------------> Entrer votre choix: ')
if choix==str(1):
    motchoisi=choixmot()                        #on appelle les fonctions du jeu
    motmasqué(motchoisi)
elif choix==str(2):
    exit()
else:
    print('\n Faites un choix valide')
