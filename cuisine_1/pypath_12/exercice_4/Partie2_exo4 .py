def motmasqué(motchoisi) : #fonction    pour le mot masqué et le nombre de vies
    reponse = ""      #variable de type str vide
    lettres = []      #variable de type list vide

    while reponse!=str(motchoisi) :
        reponse = "" #la variable est vide 
        L=input('devinez votre lettre (en minuscule): ') #l'utilisateur doit entrer une lettre a tester
        lettres.append(L)                       #on ajoute cette lettre aux autres lettres deja testé
        print('Lettre entrée: '+L)              #on affiche la lettre 
        while len(L)!=1:                        #on verifie que l'utilisateur a vraiment entrer une lettre
            L=input('Entrer une SEULE lettre a tester: ')#on affiche un message d'erreur  
            lettres.append(L)                            
        for L in motchoisi:                                
            if L in lettres :                   #on verifie si la lettre entré est deja dans laliste deja presente
                reponse = reponse + L  
            elif L=='-':                        #on verifie si la lettre entré est dans le mot masqué 
                reponse=reponse + L            #on ajoute à la réponse affiché la lettre correcte 
            else :                              
                reponse = reponse + "_ "           #sinon on laisse le lettre masqué 
        print("Les lettres déja proposées sont:",lettres)        
        print(reponse)                          #on affiche le mot
        
    if reponse==str(motchoisi) : #si le mot est correct et que le nombre d'erreur n'est pas 0 
        print("Vous avez deviné le mot","\'",motchoisi,"\'","!") #on dit a l'utilisateur qu'il a deviné le mot
        print('\n')
        
    if reponse!=str(motchoisi):                #si le mot n'est pas correct et que le nombre d'erreur est 0 
        print("Perdu le mot à trouver était","\'", motchoisi,"\'") #on affiche le bon mot et on dit a l'utilisateur qu'il n'a pas deviné le mot
