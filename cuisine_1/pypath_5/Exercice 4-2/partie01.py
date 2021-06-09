import random
def choix():
    '''cette fonction nous permet de choisir un mot au hazard dans une liste\
     de mot contenu dans un fichier'''

    try:
        with open("sowpods.txt","r") as file:
        
            lines = file.readlines()    # on lit toutes les lignes du fichier
        
            lines = [line.rstrip() for line in lines]  # on supprimme le séparateur de ligne avec rstip     
             
            choix =  random.choice(lines)    # on effectue un choix aléatoire
            #print(choix)
            
    except IOError:
        print("!!!!!!! fichier introuvable ")

    return(choix)                        # puis on retourne le choix 
