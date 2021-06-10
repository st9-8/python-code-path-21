from random import choice
 
 
COUP = ("Pierre", "Feuille", "Ciseaux")
 
score = 0            #variable pour compter le score
nbre_coup = 0        # nombre de fois joué
score_egal = 0       # nombre d'égalité

# demande à l'utilisateur s'il veut jouer: y pour yes et n pour no

while  (input("désirez vous Jouer? (cliquez sur une touche pour oui ou sur 'n' pour non): ").lower()) != "n":       # tant qu'il sa reponse est oui
    
    print("\n"+"-"*50)
    print("Bienvenue au jeu du: Pierre - Feuille - Ciseaux")
    print("-"*50 +"\n")
    try:
        
        a = int(input("Choisissez un chiffre:\n 0: Pierre\n 1: Feuille\n 2: Ciseaux\n votre choix:  "))     #choix de l'utilisateur
        b = choice(range(3))                                                                            # choix de la machine
        if a in [0,1,2]:
            
            nbre_coup += 1                                          # on incremente le nombre de tour joué

            print("\n {} VS {}".format(COUP[a], COUP[b]))               # message: choix de l'utilisateur contre choix de la machine                                

            if a == b:
                print("ÉGALITÉ\n")                                      # si les deux font le meme choix il y'a egalité egalité
                score_egal += 1

            elif (a>b and b+1==a) or (a<b and a+b==2):            # sinon si l'utilisateur choit par exemple 0:Pierre et la machine choisit 2: ciseaux, 0 < 2 et 0+2 = 2 
                print("VOUS GAGNEZ\n")                            # alors il gagne car la pierre bat le ciseau
                score += 1                                        # on augmente 1 au score à chaque fois qu'il gagne

            else:                                                  # par contre s'il choisit 0:pierre et la machine choisit 1:feuille, 0<1 mais 0+1 != 2
                print("VOUS PERDEZ\n")                              # alors il perd car la feuille bat la pierre
        else:
            print("choix invalide")                        # si le choix un mauvais numero on ne le penalise pas
    except ValueError:
        print("choix invalide")
else:
    print("\n vous avez gagné  ", score," coups sur ",nbre_coup,"avec ",score_egal,"match null \n merci pour la partie")         # quand il decide de ne plus jouer on lui affiche son resultat
