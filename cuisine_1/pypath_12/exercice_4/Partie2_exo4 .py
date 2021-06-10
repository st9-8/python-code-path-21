def motmasqué(motchoisi) :            
    rep = ""                         
    lettres = []               

   if rep.upper()!=motchoisi.upper():
        rep = "" 
        L=input('------> Devinez votre lettre (en minuscule): ') #l'utilisateur doit entrer une lettre a tester
        lettres.append(L)                       #on ajoute cette lettre aux autres lettres deja testé
        print('\n Vous avez entré: '+L)              #on affiche la lettre 
            
        while len(L)!=1:                        #on verifie que l'utilisateur a vraiment entrer une lettre
            L=input('SVP Entrer une SEULE lettre: ')#on affiche un message d'erreur  
            lettres.append(L)
            for L in motchoisi:
                if L in lettres :                   #on verifie si la lettre entré est deja dans laliste deja presente
                    rep = rep + L.upper()  
                elif L=='-':                        #on verifie si la lettre entré est dans le mot masqué 
                    rep=rep + L.upper()           #on ajoute à la réponse affiché la lettre correcte 
                else :                              
                    rep = rep + "_ "           #sinon on laisse la lettre masqué 
            print("Les lettres déja proposées sont:",lettres)
            
    elif rep.upper()==motchoisi.upper():
            print("Vous avez deviné le mot","\'",motchoisi.upper(),"\'","!") #on dit a l'utilisateur qu'il a deviné le mot
    
