def traitement(chaine):
    
    """ pour traiter la chaine  à encoder ou à décoder car notre aplphabet\
    est en majuscule et sans accent"""
    
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â',' ']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a',' ']
    for i in range(len(accent)):
        chaine = str(chaine).lower().replace(accent[i], sans_accent[i])
    return chaine


def encodage_cesar(phrase, d):
    
    """ fonction d'encodage, on fait un décalage vers la droite avec un pas d"""
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    resultat = ''
    phrase = traitement(phrase).upper()          # suppression des accent et mise en majuscule
    #print(phrase)
    for lettre in phrase:
        if lettre == ' ':                        # pour distinguer les mots apres cryptage
            resultat += lettre
        else:
            ordre = ord(lettre)- 65             # obtenir le caractère ASCII de la lettre et le ramener à l'echelle [0,25]
            indice = (ordre + d ) % 26    # obtenir l'indice de la lettre après décalage
            resultat += alphabet[indice]
            
    return resultat
                                
                                
print(encodage_cesar("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD", 3))    #test




def decodage_cesar(phrase, d ):

    """ idem que la focntion d'encodage à un detail près. ici on effectue plutot un décalage vers la gauche"""
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    resultat = ''
    phrase = traitement(phrase).upper()
    #print(phrase)
    for lettre in phrase:
        if lettre == ' ':
            resultat += lettre
        else:
            ordre = ord(lettre) - 65 
            indice = (ordre - d )%26
            resultat += alphabet[indice]
    return resultat
    
print(decodage_cesar("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",3))
            
