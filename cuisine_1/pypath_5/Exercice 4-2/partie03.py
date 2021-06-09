import random
def choix():
    '''cette fonction nous permet de choisir un mot au hazard dans une liste\
     de mot contenu dans un fichier'''

    with open("sowpods.txt","r") as file:
        
        lines = file.readlines()    # on lit toutes les lignes du fichier
        
        lines = [line.rstrip() for line in lines]  #on supprimme le séparateur de ligne avec rstip     
             
        choix =  random.choice(lines)    #on effectue un choix aléatoire
        #print(choix)

    return(choix)                        # puis on retourne le choix 



#import os

#def deviner_mot():
while input("\nvoulez vous jouer? (y/n): ") != "n":
    
    """ dans cette section, on demande à l'utilisateur  d'essayer de deviner\
    tant qu'il veut encore jouer """
    
    #os.system('cls')        # on efface l'ecran
     
    mot = choix()          # notre mot à déviner
    mot1 = mot
        
    print("\n Bienvenu au jeu du pendu")

    affichage = [ "_" for caracter in mot]    #  initialiament on ajoute autant de  (_) qu'il y a de caractère dans le mot
    

    lettres_incorrectes = []             # trace des lettres dévinées incorrectes

    longueur = len(mot)
    tentatives = 6
    
    while (longueur  > 0 and tentatives > 0):                                   # tant que le mot n'est pas vide et le nombre  maximum de tentative n'est pas atteint

        print( "\n mot à déviner: "," ".join(affichage))
        
        proposition = input("\n dévinez votre lettre: ")                      # demande à l'utilisateur d'entrer sa proposition de lettre
        proposition = proposition.upper()                                   # on converti en majuscule
        
        if proposition in mot:                                                # si sa propositon est correcte
            
            index = [index  for index in range(len(mot)) if mot[index] == proposition]          #on recupere le ou les index du caractere dans le mot
            #print(index)
            for i in index:                            # pour chaque position

                affichage[i ] = proposition            # on met le caractere à la bonne position

                print(" ".join(affichage))             # puis on affiche le caractere déviné et les caractères restant

                mot = mot.replace(proposition,'$')     # on enleve la lettre bien devinée du mot
                longueur -= 1                          # la longueur diminue
                #print(mot)
                
                
                
        else:
            if proposition in lettres_incorrectes:          # sinon on verifie si la propositon a deja été faite

                print( " \n cette lettre a déjà été déviné et classé incorrecte essayez un autre\n")
                
            else:               # sinon

                lettres_incorrectes.append(proposition)     # on ajoute la lettre à la trace des lettres incorretes

                tentatives -= 1                             #  ensuite on décremente la longueur de notre mot

                # dessin pour nombre de tentatives restantes
                
                print("\n lettre incorrecte!!!!!\n")
                if tentatives==0:
                    print("  ==========|= ")
                if tentatives<=1:
                    print("  ||/       O  ")
                if tentatives<=2:
                    print("  ||        |  ")
                if tentatives<=3:
                    print("  ||       /|\ ")
                if tentatives<=4:
                    print("  ||       /|  ")
                if tentatives<=5:                    
                    print(" /||           ")
                if tentatives<=6:
                    print("==============\n")
                    
    # message de gain ou pert à la fin d'une partie
    
    if '_'  in affichage:
        print("vous avez perdu!!!!\n le mot à deviné etait: ", mot1)
    else:
        print("Bravo!!!! vous avez gagné\n")

    

    
