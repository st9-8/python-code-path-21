#----------------------------------------- Fonctions ---------------------------------------------------#
def encodage(texte,nombreDecalage):
    taille = len(texte)
    i = 0
    while i < taille:
        if texte[i] == " ": 
            texte[i] = " "
        else: 
            texte[i] = alphabet[alphabet.index(texte[i].lower()) - nombreDecalage]
        i = i + 1
    return texte

def decodage(texte,nombreDecalage):
    alphabet.reverse()
    taille = len(texte)
    i = 0
    while i < taille:
        if texte[i] == " ": 
            texte[i] = " "
        else: 
            texte[i] = alphabet[alphabet.index(texte[i].lower()) - nombreDecalage]
        i = i + 1
    alphabet.reverse()
    return texte
#--------------------------------------------------------------------------------------------------------#
#------>>>>>>>>>  alphabet <<<<<<<<<-----#
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#-------------------------------------------------------------------------------------------------------------------
choix = 0
while choix != 3: #Boucle controlant le menu
    print("1. Encoder (decalage a gauche)")
    print("2. Decoder (decalage a droite)")
    print("3. Quitter")
    choix = int(input("Entrez votre choix: "))
    while choix < 1 or choix >3: #Boucle controlant le choix de l'utilisateur
        print("Votre choix doit etre compris entre 1 et 3")
        choix = int(input("Entrez votre choix: "))

    if choix == 1: 
        nombreDecalage = int(input("Entrez le decalage: "))
        texte = input("Entrer un texte: ")
        texte = list(texte)
        print("+--+-------------------------------------------------+--+")
        print("Encodage: ",''.join(encodage(texte,nombreDecalage)))
        print("+--+-------------------------------------------------+--+")

    elif choix == 2:
        nombreDecalage = int(input("Entrez le decalage: "))
        texte = input("Entrer un texte: ")
        texte = list(texte)
        print("+--+-------------------------------------------------+--+")
        print("Decodage: ",''.join(decodage(texte,nombreDecalage)))
        print("+--+-------------------------------------------------+--+")

    else: 
        pass
#-------------------------------------------------------------------------------------------------------------------   



