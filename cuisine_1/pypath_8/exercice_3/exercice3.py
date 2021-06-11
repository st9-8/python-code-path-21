#main exercice 3

import main3, random
import f_usuelles

ordi_choix = random.choice(["pierre", "feuille", "ciseau"])


main3.menu()

choix = main3.autrePartie()


score = 0

while choix not in ['O', 'N']:
    print( 
          """ \033[31;2;132;220;51;1;48;2m
          Choix non valide
            
          \033[00m \n""")
    choix = main3.autrePartie()
    
while choix  == 'O':
    print( 
          """ \033[36;2;132;220;51;1;48;2m
            Pierre, Feuille ou Ciseau ? :-)
            
          \033[00m""")
    user_choix = input(" ")

    if user_choix not in ["pierre", "feuille", "ciseau"]:
        print("Mot non reconnu!!! ")
        choix = main3.autrePartie()
    else:
        res = main3.jouer(ordi_choix, user_choix)
        if res == True:
            score = score + 1  

if choix == 'N':
   
    f_usuelles.clear()
    print( 
        """ \033[35;2;132;220;51;1;48;2m
        Bye!
        Votre score est {}
            
        \033[00m""".format(score))

    



