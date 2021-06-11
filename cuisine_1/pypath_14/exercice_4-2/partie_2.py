import partie_1

def play() :
    """
        cette fonction permet  de lancer le jeu
        masquer le mots
        afficher les lettres correct
    """

    try :

        mot = partie_1.choisir_mot()
        mot_cacher = "_"*len(mot)
        lettre_pos = {}
        deja= set()

        for  i in tuple(enumerate(mot)) : 

            if i[1] in lettre_pos.keys() :
                lettre_pos[i[1]].append(i[0])
            else : 
                lettre_pos[i[1]]= [i[0]]
        
        while mot != mot_cacher :
            print( " ".join(list(mot_cacher)))
            lettre =  input("entrez une lettre :\n ->").lower()

            while not (lettre.isalpha()) : 

                print("mauvaise entrer")
                lettre =  input("entrez une lettre :\n ->").lower()
            
            if lettre in deja:
                print(" vous avez deja entrez cette lettre")

            else:
                deja.add(lettre)
                if lettre in lettre_pos.keys():
                    for j in lettre_pos[lettre]:
                        mot_cacher = list(mot_cacher)
                        mot_cacher[j] =lettre
                        mot_cacher= "".join(mot_cacher)

                else :
                    print("Incorrect")
            if mot == mot_cacher:
                print(mot)
                print(" Bravo !! vous avez evité la pendaison .\n Enfin Pour cette fois !!!")
        
    except : 
        print("une erreur est  survenue")

    
play()
            
            

        


    
