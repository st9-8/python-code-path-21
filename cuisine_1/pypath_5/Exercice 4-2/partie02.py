
def deviner_mot():
    """ dans cette section, on demande à l'utilisateur  de deviner les lettres\
    d'un mot """
    

     
    mot = "bonjour"          # notre mot à déviner
    
        
    print("\n Bienvenu au jeu du pendu")

    affichage = [ "_ " for caracter in mot]    #  initialiament on ajoute autant de  (_) qu'il y a de caractère dans le mot
    

    lettres_incorrectes = []  # trace des lettres dévinées incorrectes

    longueur = len(mot)
    
    while longueur > 0:                                   # tant que le mot n'est pas vide, vu qu'on s'arrete quand on a tout déviné correctement
        print( "mot à déviner: "," ".join(affichage))
        
        proposition = input("dévinez votre lettre: ")                                # demande à l'utilisateur d'entrer sa proposition de lettre
        
        if proposition in mot:                                        # si sa propositon est correcte
            
            index = [index  for index in range(len(mot)) if mot[index] == proposition]          #on recupere le ou les index du caractere dans le mot
            #print(index)
            for i in index:                      # pour chaque position

                affichage[i ] = proposition      # on met le caractere à la bonne position

                print(" ".join(affichage))       # puis on affiche le caractere déviné et les caractères restant

                mot = mot.replace(proposition,'$')     # ensuite on supprime les caracteres dévinés correctement
                #print(mot)
                
                longueur -= 1                    #  ensuite on décremente la longueur de notre mot
                
        else:
            if proposition in lettres_incorrectes:  # sinon on verifie si la propositon a deja été faite
                print( " cette lettre a déjà été déviné et classé incorrecte essayez un autre")
                
            else:          # sinon
                lettres_incorrectes.append(proposition)     # on ajoute la lettre à la trace des lettres incorretes 
                print("lettre incorrecte!!!!")

        

    
