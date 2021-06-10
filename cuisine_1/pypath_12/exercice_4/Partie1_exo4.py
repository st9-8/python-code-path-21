
def choixmot() :                       #fonction chargée de choisir un mot aléatoirement
    f=open('sowpods.txt','r')               #on ouvre le dictionnaire pour le lire       
    line= random.randrange(0,336531)     #le dico est composée de lignes qui corresponde chacun à un mot donc line est la ligne du mot choisie aléatoirement   
    for n in range (0,line):             #pour n de 0 jusqu'à la ligne du mot
        motchoisi=f.readline().replace('\n','') #lire le mot choisi     
    f.close()                            # on ferme le dico
    return motchoisi                           #on retourne le mot choisi



                         
