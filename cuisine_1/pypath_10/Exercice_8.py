# -*-coding:Utf-8 -*

A_clair = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
A_cypher = ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']

def encodage():
    texte_co = []
    texte = (input("Votre phrase à encoder : ")).upper()
    print("Texte en clair: "+texte)

    texte = texte.split()
    for k, mot in enumerate(texte):
        liste_mot = []
        for i, lettre in enumerate(mot):
            for j, elt in enumerate(A_clair):
                if lettre == elt:
                    liste_mot.append(A_clair[j-3])
        texte_co.append("".join(liste_mot))
    texte_co = " ".join(texte_co)

    print("Texte chiffré: "+texte_co)

def decodage():
    texte = []
    texte_co = (input("Votre phrase à décoder : ")).upper()
    print("Texte chiffré: "+texte_co)

    texte_co = texte_co.split()
    for k, mot in enumerate(texte_co):
        liste_mot = []
        for i, lettre in enumerate(mot):
            for j, elt in enumerate(A_cypher):
                if lettre == elt:
                    liste_mot.append(A_cypher[j-23])
        texte.append("".join(liste_mot))
    texte = " ".join(texte)

    print("Texte en clair: "+texte)

print("\t***CHIFFREMENT DE CÉSAR***\n\n\t1. Encoder une expression\n\t2. Decoder une expression\n\t0. Quitter")
choix = -1
while choix <= -1 or choix > 2:
    try:
        choix = int(input("\n\t>>> Que voulez-vous faire(1/2): "))
    except:
        conso = -1
        print("Vous n'avez pas saisi une consommation correct")
    if choix == 1:
        encodage()
    if choix == 2:
        decodage()