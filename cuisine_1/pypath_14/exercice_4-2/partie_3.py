
import os
import sys
import random
import pickle
import platform
import datetime
def dessin_pendu(vie):

    """ cette fonction dessine le pendu
    """
    vie = int(vie)
    if(vie == 6):
        
        print("""\033[38m
                        ___________
                        |       |
                        |       
                        |           
                        |           
                        |           
                        |     
                        |
                    ---------
        \033[00m""")
        print("""\033[38m
                Encore 6 essais pour vous echappez !
          \033[00m""")
         
    elif(vie == 5):
        print("""\033[38m
                        ____________
                        |        |
                        |      (x_x)
                        |           
                        |           
                        |           
                        |          
                        |
                    ---------
        \033[00m""")
        print("""\033[38m
                Aie !! Vous avez encore 5 essais!
          \033[00m""") 
    elif(vie == 4):
        print("""\033[38m
                        ____________
                        |        |
                        |      (x_x)
                        |        |   
                        |        |   
                        |           
                        |          
                        |
                    ---------
        \033[00m""") 
        print("""\033[38m
                Plus que 4 essais ! Attention!
          \033[00m""")
    elif(vie == 3):
        print("""\033[38m
                        ____________
                        |        |
                        |      (x_x)
                        |        |   
                        |       /|   
                        |           
                        |          
                        |
                    ---------
        \033[00m""")
        print("""\033[38m
                reflechissez bien !
                Il vous reste 3 essais. 
          \033[00m""")
    elif(vie ==2 ):
        print("""\033[38m
                        ____________
                        |        |
                        |      (x_x)
                        |        |   
                        |       /|\  
                        |          
                        |         
                        |
                    ---------
        \033[00m""")
        print("""\033[38m
                2 essais,Concentrez-vous !
          \033[00m""")
    elif(vie==1):
        print("""\033[38m
                       ____________
                        |        |
                        |      (x_x)
                        |        |   
                        |       /|\  
                        |        | 
                        |      _/
                        |
                    ---------
        \033[00m""")
        print("""\033[38m
                Derniere chance !!!
          \033[00m""")
    elif(vie == 0):
        print("""\033[38m
                
                        ____________
                        |        |
                        |      (x_x)
                        |        |   
                        |       /|\  
                        |        | 
                        |      _/ \_
                    ---------
        \033[00m""")

        print("""
                \033[38m
                   PERDU !VOUS AVEZ ETE PENDU  !    
                \033[00m
            """)


    

def enregistre_top_score(nom,score):
    """ cette fonction est pour enregister les top score .il prend en parametre le nom et le score
    du joueur. ici notre nombre de top score c'est 5 ,si il est atteint et qu'un nouveau scrore et superieur a l'un des top scores,
    alors le plus petit des top  scores et retirer et on ajoutera le nouveau"""
    if os.path.exists("score.txt"):

        with open("score.txt", "rb")as f:
            scores = pickle.load(f)
        if len(scores) < 5:
            scores[nom] = score
            with open("score.txt", "wb")as f:
                pickle.dump(scores, f)
        else:
            liste = []
            for i in sorted(scores.items(), key=lambda x: x[1]):
                liste.append(i)
            if liste[0][1] < score:
                del scores[liste[0][0]]
                scores[nom] = score
                with open("score.txt", "wb")as f:
                    pickle.dump(scores, f)

    else:
        with open("score.txt","wb")as f:
            scores = dict()
            scores[nom] = score
            pickle.dump(scores, f)


            

def affiche_top_score():
    """cette fonction permet d'afficher les meilleurs du plus grand au plus petit
    """
    if os.path.exists("score.txt"):
	    with open("score.txt", "rb") as f:
	        scores = pickle.load(f)
	        pos = 0
	    print("---------- MEILLEURS SCORES ----------".center(50))
	    print("possition \t|   nom   date    heure |  \t\t\t\t -->| scores")
	    for cle,valeur in sorted(scores.items(), key=lambda x: x[1],reverse=True):#cette ligne( a partir de sorted) permet de trier un dictionnaire en fonction de la valeur de la clé
	    #si vous voulez trier en fonction de la clé faites key = lambda x:x[0]
		    pos += 1
		    print(pos,"\t\t|  ",cle,"   \t\t\t\t\t|",valeur,"points")
    else: 
        print("pas de score pour le moment")
       
	


def choisir_mot() : 
    """
        fonction permettant de choisir un mot au hasard dans notr dictionaire

    """
    try :

        liste_mots = [mot.strip() for mot in open("sowpods.txt", encoding="utf-8")]
        mot = random.choice(liste_mots).lower()
        return mot 
    except:
        print("Nous  avons pas pu ouvrir le fichier")
        print("1-verifier si le fichier est existant")
        print("2-si le fichier existe rassurer vous qu'il se trouve dans la meme dossier que ce code")



def play() :

    try :
        vie = 6
        score = 0
        mot =choisir_mot()
        mot_cacher = "_"*len(mot)
        lettre_pos = {}
        deja= set()

        for  i in tuple(enumerate(mot)) : 

            if i[1] in lettre_pos.keys() :
                lettre_pos[i[1]].append(i[0])
            else : 
                lettre_pos[i[1]]= [i[0]]
        
        while mot!= mot_cacher and vie >0 :
            dessin_pendu(vie)
            print("\n\n")
            print( " ".join(list(mot_cacher)))
            print("\n\n")
            lettre =  input("entrez une lettre :\n ->").lower()

            while not (lettre.isalpha()) : 

                print("mauvaise entrer")
                lettre =  input("entrez une lettre :\n ->").lower()
            
            if lettre in deja:
                print(" vous avez deja entrez cette lettre")

            else:
                deja.add(lettre)
                score += 50
                if lettre in lettre_pos.keys():
                    for j in lettre_pos[lettre]:
                        mot_cacher = list(mot_cacher)
                        mot_cacher[j] =lettre
                        mot_cacher= "".join(mot_cacher)

                else :
                    vie -=1
                    if score != 0 :
                        score +=50
                    print("Incorrect")
            if mot == mot_cacher:
                print(" \033[32m Bravo !! vous avez evité la pendaison .\n Enfin Pour cette fois !!!\033[00m")
                print("le mot etait :",mot,"".center(50))
                nom = input("Entrer votre nom ->")
                date = str(datetime.datetime.now())
                print(nom,"votre srores est de :", score)
                enregistre_top_score(nom+"  "+date,score)

            if vie == 0:
               
                print("le mot etait :", mot)
                dessin_pendu(vie)
                input("Appuyer sur entrez pour continuer")
                affiche_top_score()

                
    except : 
        print("une erreur est  survenue")

def clean() :
    """
        cette fonction permet nettoyer l'ecran
    """
    if(platform.system() == "Linux"):
        os.system('clear')
    elif(platform.system() == "Windows"):
        os.system('cls')

def menu():
    """
    cette fonction dessine le menu 
    permet de lancer une nouvelle partie
    afficher un les top  scores
    et quitter le jeux 

    """
    print("PENDU".center(50))
    print("################################################################")
    print("#                  Bienvenue dans PENDU!!!!!!                  #")
    print("################################################################")
    print("#                          REGLES!!!!!!                        #")
    print("# Les règles sont simples.Vous diposez de 6 vies pour trouver  #")
    print("# un mot qui masqué.A chaque essai, il faut entrer une lettre  #")
    print("# que vous estimez appartenir au mot. Si vous echouez à la fin #")
    print("# de vos 6 vies, vous êtes PENDU! Sinon,vous avez gagnez.Alors #")
    print("#                          BONNE CHANCE!                       #")
    print("################################################################")
    print("MENU".center(50))
    
    print("   1-Nouvelle Partie")
    print("   2-Meilleurs scores") 
    print("   3-Quitter")
    choix_valeur ={
        "1":play,
        "2":affiche_top_score,
        "3":sys.exit
    }
    choix=""
    while choix not in  choix_valeur.keys():
        choix= input (" faites votre choix \n ->")
    if choix=="3":
        print("BYE ET MERCI")
        choix_valeur[choix]()
    else:
        choix_valeur[choix]()
        input("Appuyer sur une touche.....")
        clean()
        menu()

menu()



