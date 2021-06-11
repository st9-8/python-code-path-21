#contient les fonctions principales

def jouer(ordi_choix="", user_choix=""):

    user_choix = user_choix.lower()
    
    valider = False
    if user_choix == 'pierre' and ordi_choix == 'ciseau':
        valider = True
        print("Gagner!!!")

    elif user_choix == 'feuille' and ordi_choix == 'pierre':
        valider = True
        print("Gagner!!!")

    elif user_choix == 'ciseau' and ordi_choix == 'feuille':
        valider = True
        print("Gagner!!!")

    else:
        valider = False
        print("Perdu!!!")

    return valider

def autrePartie():
    reponse = input("Nouvelle partie ? (O/N):")
    
    while(reponse.isalpha() is False):
        print("Entrée invalide.")
        reponse = input("Jouer une autre partie ? (O/N): ")
    
    return reponse.upper()

def menu():

    """Cette fonction affiche le menu"""
    
    print( 
          """ \033[36;2;132;220;51;1;48;2m
                             *MENU: Pierre, Feuille, Ciseau*
        
        Nouvelle partie? O/N
            
          \033[00m""")
