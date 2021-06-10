""" 
ce code  est  pour le jeu pierre -feuille ciseau
regle  : 
la feuille bat la pierre
la pierre bat le ciseau
le ciseau  bat la feuille

il  y'as posssibilité de jouer plusieur fois 
et affficher le score des parties jouer 

"""
import random


def lancer_partie():
    """
        cette  fonction  permet de lancer le jeu et de compter les parties jouer 
    """

    nombre_partie = 0 #  contient le  nombre de partie jouer 
    partie_gagner = 0 #  contient le nombre de partie gagner 
    partie_perdue = 0#  contient le  nombre de partie perdu 
    partie_nulle = 0 # contient le nombre de partie nulle
    #rejouer =''
    partie  = "oui" # permet de controler si l'utilisateur veux jouer ou non . on peut jouer au debut

    choix = {
        1 : "pierre" ,
        2 : "feuille",
        3 : "ciseau"
    }#  ce dictionnaire contient les valeurs possible

    print("\t\t\t\t Bievenue au jeux Pierre-feuille-ciseau\n\n".lower())
    print("\t\t\t\t\t voici les régles".upper())
    print("\t\t\t\t\t -la feuille bat la pierre \n\t\t\t\t\t -la pierre bat le ciseau \n\t\t\t\t\t -le ciseau  bat la feuille")
    



    while partie == "oui" : 
        partie =""

        nombre_partie += 1
        print("\t\t\t\tFaites votre choix ")
        print("\t\t\t\t\t1- pierre \n\t\t\t\t\t2-feuille  \n\t\t\t\t\t3-ciseau")
        user_choice = 0

        while int(user_choice) not in choix.keys() :
            # on se rassurer qu'il entre quelque parmi les choix possible

            user_choice =int(input("\t\t\t\t\tvotre choix \n ->".strip()) )

        cpu_choice = random.randint(1,3) # choix aleatoire de l'ordinateur 

        print("\n\t\t\t\t\tvous avez choisi: '{}' ".format(choix[user_choice]))
        print("\t\t\t\t\tLe choix de l'ordinateur :'{}' ".format(choix[cpu_choice]))

        if user_choice == cpu_choice+1  or user_choice == cpu_choice-2: 
            """
                le dictionnaire est  fait de telle sorte que les clés soient des entiers
                et  ranger dans un pseudo ordre (1 <2 ,2<3  mais 3<1)
            """
            partie_gagner +=1
            print("\n\t\t\t\t\tFelicitations ! vous avez gagner \n")
        elif user_choice == cpu_choice :
            partie_nulle +=1
            print("\n\t\t\t\t\tPartie nulle !!! \n")
        else: 
            """
                ici on gere les autre cas possible 
            """
            partie_perdue +=1
            print("\n\t\t\t\t\tDommage vous avez perdu !!!\n")

        while partie not in ["oui","non"] : 

            partie =  input("\n\t\t\t\t\tvoulez vous rejouer oui/non \n ->".lower().strip())

        if  partie == "non" :
            #partie = False
            print("\n\t\t\t\t\tMerci d'avoir jouer ")
            print("\t\t\t\t\tStatistique")
            print("\t\t\t\t\tNombre de partie  joué :{} \n\t\t\t\t\tNombre de partie gagnée :{} \n\t\t\t\t\tNombre de partie perdue :{}\n\t\t\t\t\tNombre de partie nulle:{}".format(nombre_partie,partie_gagner,partie_perdue,partie_nulle))

        """else :
            partie = True
        """



lancer_partie()


            


       
       




    


        


   

