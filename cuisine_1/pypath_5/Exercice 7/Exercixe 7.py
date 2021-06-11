import fontions_exercice7
import platform


def plateforme():
    print("bienvenue: ", platform.uname(),"\n system :", platform.system(), "\n")

def traitement(chaine):
    """ cette focntion nous permettra de traiter les informations entrées par l'utilisateur """
    
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â',' ']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a','']
    #chaine = chaine.lower()
    for i in range(len(accent)):
        chaine = str(chaine).lower().replace(accent[i], sans_accent[i])
    return chaine

# nos  menus

menu = {}
menu['1']="Moyenne"
menu['2']="Variance"
menu['3']="Ecart type"
menu['4']="Médiane"
menu['5']="Premier quartile"
menu['6']="troisième quartile"
menu['7']="Maximum"
menu['8']="Minimum"
menu['9']="Mode"
menu['10'] = "Coefficient de Pearson entre age et pression"
menu['11']="statistiques"
menu['12']="Sauvegarder tous"
menu['13']="Afficher tous"
menu['Q ou 0']="Quitter le programme"

def readFile(column):
    """ cette fonction lit un fichier et recupère les valuers de la colonne désirée\
    par l'utilisateur si elle existe """
    
    with open('data_exo_7.txt','r') as file:
        
        lines = file.readlines()
        #print(lines[0])
        
        desired_column_data = []
        index = -1
        for i in lines:
            #print(i)
            line = i.split()
            
            for k,item in enumerate(line):
                #print(k,item)
                if column == line[k] and index == -1:
                    index = k
                    #desired_column_data.append(column)
                elif k == index:
                    desired_column_data.append(line[k])
                    
    ## le resultat precedent est une liste de chaine de caractere, on convertit ces valeurs en entier pour pouvoir effectuer nos opération
    desired_column_data_int = []                
    for j in range(len(desired_column_data)):
            desired_column_data_int.append((int(desired_column_data[j])))                
    return desired_column_data_int




# On recupere l'entête de notre fichier puis on traite
    
with open('data_exo_7.txt','r') as file:
    lines = file.readline().rstrip()         # on lit la premier ligne en supprimant le séparateur de ligne
    line = lines.split('\t')                 # on supprime le séparateur de colonne on obtient une liste
    #print(line)
    header = []                             # notre entete
    for i in range(len(line)):
        header.append(traitement(line[i]))
        #print(header)
        

def readFileAll():
    ''' cette fonction récupère les valeurs de toutes les colonnes de notre fichier, on va l'utiliser pour notre sauvegarde '''
    liste = []
    for column in header:
        liste.append(readFile(column))
        
    return liste
  
plateforme()
column = 0
while column != "0":
    try:
        column = input("\n Entrez le nom de la colonne sur laquelle vous souhaitez travailler ou 0 si vous ne desirez rien: ")

                   
        if column in header:                 # verifie si la colonne entrée par lutilisateur existe dans le fichier
        
            column = traitement(column)      # on appel la fonction traitement() qui permet de mettre en minuscule et supprimer les accents

            column_int = readFile(column)    # on appel la fonction ReadFile() qui permet de recuperer les valeurs de la colonne entrée par l'utilisateur

    

            print("\n Quelle opération souhaitez vous effectuer?\n".center(50))
    
            while True:
            
                #options = sorted(menu.keys())
            
                for cle in menu.keys():
                    print (cle, menu[cle])         # on affiche le menu

                # en fonction du choix de l'utilisateur, on effectue une opération. fontions_exercice7 est notre module contenant les fonctions

                try:
                    selection=input(" \n votre choix svp: ".center(50))
                    
                    if selection =='1':
                        print ("\nLa moyenne de la colonne " ,column, " est: ", fontions_exercice7.moyenne(column_int))
                        
                    elif selection == '2': 
                        print ("\nLa variance de la colonne ", column, " est: ", fontions_exercice7.variance(column_int))
                        
                    elif selection == '3': 
                        print ("\nL'écart type de la colone ", column, " est: ", fontions_exercice7.ecart_type(column_int))
                        
                    elif selection == '4': 
                        print ("\nLa médiane de la colone ", column, " est: ", fontions_exercice7.mediane(column_int))
                        
                    elif selection == '5': 
                        print ("\nLe premier quartile de la colone ", column, " est: ", fontions_exercice7.premier_quartile(column_int))
                        
                    elif selection == '6': 
                        print ("\nLe troisieme quartile de la colone ", column, " est: ", fontions_exercice7.troisieme_quartile(column_int))
                        
                    elif selection == '7':
                        print (" \nLe maximum de ", column," est: ", fontions_exercice7.maximum(column_int))
                        
                    elif selection == '8':
                        print ("\nLe minimum de ", column," est: ", fontions_exercice7.minimum(column_int))
                        
                    elif selection == '9':
                        print ("\nLe mode de ", column, " est: ", fontions_exercice7.mode(column_int))
                        
                    elif selection == '10':  
                        liste_age = readFile('age')            # on recupere les elements de age
                        liste_pression = readFile('pression')  # on recupere les valeurs de pression
                        print ("\nLa corrélation entre age et pression est: ", fontions_exercice7.coefficient_pearson(liste_age,liste_pression))

                    elif selection == '11':
                        print("\nStatistiques de la colonne",column,"\n")
                        fontions_exercice7.statistique(column_int,column)

                    elif selection == '12':
                        liste = readFileAll()                            
                        fontions_exercice7.sauvegarder(liste,header)
                        print("\n données sauvegardées".center(100))

                    elif selection == '13':
                        print("\nvisualisation\n".center(100))
                        fontions_exercice7.afficher()

                    elif (selection == 'Q'or selection == '0') :
                        liste = readFileAll()
                        fontions_exercice7.sauvegarder(liste ,header)                   
                        print("vos resultats ont été enregistrer dans le fichier resultat.csv de votre repertoire courant, merci!!!")
                        break

                    else: 
                        print ("option inconnu selection l'une des option sus-citées!\n" )

                except KeyboardInterrupt:
                    print("\npour quitter le programme , appuyer sur  Q ou 0")

        elif column != '0':
            print("\ncette colonne n'existe pas")
            continue
        else:
            print("\nmerci pour votre attention")
            
    except KeyboardInterrupt:
        print("\npour quitter le programme , appuyer sur 0 ")
        

                        

                    
