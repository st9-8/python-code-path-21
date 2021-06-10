import csv

""" ce module contient les fonctions que nous allons utilisé dans notre programme """

def moyenne(liste):
    
    """ce bloc calcule la moyenne d'une liste qui est la somme de ses élément\
    divisé par sa longuer, ca prend en compte le fait qu'on ne peut diviser un nombre par 0"""

    try:
        moyen = sum(liste)/len(liste)
        return round(moyen,2)                  # round(x,n) permet de retreindre le nombre de chiffre pares la virgule. dans notre cas, on affiche 2
    except ZeroDivisionError:
        print("la liste est vide")
        

def variance (liste):
    
    """ la variance d'une liste c'est la moyenne des carrés mois le carré de la moyenne"""
    try:
        m=moyenne(liste)
        var=0
        
        for k in range(len(liste)):
        
            var += (liste[k]-m)**2
            variance = var/len(liste)
        return round(variance,2)

    except ZeroDivisionError:
        print("la liste est vide")
        

def ecart_type(liste):
    
    """ calcul de l'ecart tytype d'une liste qui est la racine carré de la variance """
    try:
        v = variance(liste)
        ecart = v ** (0.5)
        return round(ecart,2)
    except ZeroDivisionError:
        print("la liste est vide")

        
def coefficient_pearson(liste1,liste2):
    '''Le coefficient r de Bravais-Pearson entre deux listes  se calcule en appliquant la formule suivante:
    covariance(liste1,liste2)/ecart_type(liste1)*ecart_type(liste)2 '''
    try:
        '''calcul de la covariance'''
        # on calcul la moyenne et l'ecart type des deux listes
        moy1 = moyenne(liste1)
        moy2 = moyenne(liste2)
        ecart1 = ecart_type(liste1)
        ecart2 = ecart_type(liste2)
    
        somme = 0
        for i in range(len(liste1)):
            somme += (liste1[i]-moy1)*(liste2[i]-moy2)  #chaque element de la premier liste moins la moyenne multiplié par chaque element de la seconde liste moins la moyenne
            covariance = somme / len(liste1)         # la variance c'est la somme précédente divisée par la taille de la liste
    
        ''' corrélation'''
        correlation = covariance /(ecart1*ecart2)
        return round(correlation,3)
    
    except ZeroDivisionError:
        print("la liste est vide")

        
def mediane(liste):
    
    """ cette fonction calcule la médiane d'une colonne qui est l'élement au juste\
    milieu de la liste triée """

    try:
        a = len(liste)
        liste.sort()                                # on trie la liste
        if a%2 == 0:                                # test si la longeur est pair
            med = (liste[(a-1)//2] + liste[a//2])/2 # la mediane sera la moyenne des élément qui sépare au mieu la colonne
        else:                                       # sinon
            med = liste[(a-1)//2]                   # la médiane sera l'élément au milieu
        return med
    except IndexError:
        print("impossible de trouver la médiane")
    
        
    
def premier_quartile(liste):
    
    """ cette fonction calcule le premier quartile d'une colonne qui est l'élement\
    separant les 25% de la liste triée """

    try:
        a = len(liste)
        liste.sort()                                # on trie la liste
        if a%4 == 0:                                # on verifie si a est un diviseur de 4
            quartile1 = liste[(a//4)-1]             # le 1er quartile sera l'element à la position a/4 et son indice est a/4 - 1
        else:                                       #sinon
            quartile1 = liste[(a//4)]               # on prend l'élément à la positon a/4 + 1 d'indice a/4
        return quartile1
    except IndexError:
        print("impossible de trouver la médiane")


def troisieme_quartile(liste):
    
    """ cette fonction calcule le troisieme quartile d'une colonne qui est l'élement\
    separant les 75% de la liste triée """

    try:
        a = len(liste)
        
        liste.sort()                                 # on trie la liste
        if (3*a)%4 == 0:                                 # on verifie si 3a est un diviseur de 4
            quartile3 =  liste[(3*a)//4 - 1]             # le 3 quartile sera l'element à la position 3a/4 et son indice est 3a/4 - 1
        else:                                        #sinon
            quartile3 = liste[(3*a)//4]               # on prend l'élément à la positon 3a/4 + 1 d'indice 3a/4
        return quartile3
    except IndexError:
        print("impossible de trouver la médiane")
        


def maximum(liste):
    
    """ calcul du minimum des valeurs d’une liste """
    try:
        maxi = liste[0]
        for i in range(len(liste)):
            if liste[i] > maxi:
                maxi = liste[i]
        return maxi
    except IndexError:
        print("liste vide")

        
def minimum(liste):
    
    """ calcul du minimum des valeurs d’une liste """
    try:
        mini = liste[0]
        for i in range(len(liste)):
            if liste[i] < mini:
                mini = liste[i]
        return mini
    except IndexError:
        print("liste vide")



def mode(liste):
    
    """ calcul du mode qui est la ou les valeur(s) la (les) presente(s) dans la liste"""
    dic = {}
    for i in liste:
        dic[i] = liste.count(i)                                  #on compte le nombre d'occurence de chaque valeur
    return [k for k, v in dic.items() if v == max(dic.values())]  # et on affiche le ou les maximum


def effectif(liste):
    
    """ il s'agit de compter le nombre d'occurence de chaque valeur """
    liste.sort()
    dic = {}
    for i in liste:
        dic[i] = liste.count(i)
    return [valeur for cle, valeur in dic.items()]
    
def effectif_cumuler(liste):
    
    """ on cumule les effectif c'est a dire qu'on calcule l'effectif d'une valeur en tenant compte de resultat precedant"""
    liste = effectif(liste)        # on calcul d'abord les effectifs
    liste_cumul = []               # liste des effectif cumulés initialement vide
    j = 0                          # variable qui contiendra a chaque fois le resultat précedent
    for i in range(len(liste)):
        liste_cumul.append(liste[i]+j)
        j += liste[i]
    return liste_cumul


def frequence(liste):
    
    """ ce bloc calcul les frequences des element d'une liste """
    
    liste = effectif(liste)                 # on calcul d'abord les effectifs
    #print(sum(liste))
    ma_liste = []                           # la liste qui contiendra les frequence
    for i in range(len(liste)):
        freq = (liste[i]/sum(liste))*100    # calcul de la frequence
        ma_liste.append(round(freq,2))
    return ma_liste


def frequence_cumuler(liste):
    
    """ on calcul les frequences cumules """
    
    liste = frequence(liste)                    # on calcul d'abord les frequences
    freq_cumul = []                             # liste qui contiendra les frequences a la sortie
    j = 0                                       # variable qui contiendra le resultat de l'iteration precedente
    for i in range(len(liste)):
        freq_cumul.append(round(liste[i]+j,2))           # cumul des frequences et ajout a la liste
        j += liste[i]

    return freq_cumul


       
def statistique (liste,colonne):

    """ cette fonction permet d'ecrire dans un fichier les observations statistiques d'une colonne\
    (effectifs, effectifs cumules, frequences, frequences cumules)"""
    
    eff = effectif(liste)                    # calcul des effectifs
    
    eff_cumul = effectif_cumuler(liste)       # calcul des effectifs cumulés

    freq = frequence(liste)                   # calcul des frequences
    
    freq_cumul = frequence_cumuler(liste)     # calcul des frequences cumulés

    liste.sort()
    liste = list(set(liste))                  # supprimer les doublons dans la liste avant l'affichage car les effectifs on deja été calculés

    
    # on cree notre tableau qui est une liste de liste contenant tous les element calculés plus haut
    result = []
    result.append([(elt) for elt in liste])    
    result.append([(elt) for elt in eff])
    result.append([(elt) for elt in eff_cumul])
    result.append([(elt) for elt in freq])
    result.append([(elt) for elt in freq_cumul])
    #print(result)
    
    # on ajoute les noms en premiere position de chaque ligne dans notre tableau precedent
    a = dict()
    a[0] = "liste            "
    a[1] = "effectifs        "
    a[2] = "effectifs cumulés"
    a[3] = "frequences       "
    a[4] = "frequence cumulés"
    #print(a)
    for k,v in a.items():
        result[k].insert(0,a[k])          
        
    # on affiche le tableau crée précédemment
            
    for i in range(len(result)) : 
        for j in range(len(result[i])): 
            print(result[i][j], end="\t")
        print() 
    
    #with open ("data_caracteristique.txt", "w") as file:
        
     #   file.write(colonne.ljust(20) +str(liste)+ "\n")                  # premiere ligne de notre fichier qui contient le nom de la liste de depart et ses valeurs
        
      #  file.write("effectifs".ljust(20) +str(eff)+ "\n")                 # insertion des effectifs. la fonction ljust() permet de faire le decalage entre deux valeur de la ligne
        
      #  file.write("effectifs cumulés".ljust(20)+str(eff_cumul)+ "\n")              # insertion de des effectifs cumulés
        
      #  file.write("frequences".ljust(20) +str( freq) + "\n")                 # ecriture des frequences
        
       # file.write("frequences cumulés".ljust(20)+str(freq_cumul)+"\n")                  # ecriture de frquences cumulés

        
        

    #with open ("data_caracteristique.txt", "r") as filein:
     #   pass
        #print(filein.read())
    #filein.close()

 
   
def sauvegarder(liste,column):
    """ce bloc permet de sauvegarder dans une fichier toutes les caracteristiques descriptives telles\
     que la moyenne etc... de toutes colonne"""

    """ elle prend deux  parametres; la 1ere est une liste de liste c'est a dire une liste contenant \
     la liste de toutes nos colonnes, et la se seconde une liste contenant le nom des colonnes """

    with open("resultat.csv",'w') as file:
        writer = csv.writer(file, delimiter = ';', quotechar = '|')
        #print(column)
        column.insert(0,"caracteristique")      # entete de notre fichier
        #print(column)
        writer.writerow(column)         

         # on calcule pour chaque colonne ses caracteristiques que l'on met dans une liste avec un nom spécifique tel que la moyenne
         
        moye = ["moyenne"]
        med = ["mediane"]
        var = ["variance"]
        ecart = ["ecart type"]
        premier = ["premier quartile"]
        troisieme = ["troisieme quartile"]
        maxi = ["maximum"]
        mini =["minimum"]
        mod = ["mode"]
        
        for i in range(len(liste)):
            moye.append((moyenne(liste[i])))
            med.append((mediane(liste[i])))
            var.append((variance(liste[i])))
            ecart.append((ecart_type(liste[i])))
            premier.append((premier_quartile(liste[i])))
            troisieme.append((troisieme_quartile(liste[i])))
            maxi.append((maximum(liste[i])))
            mini.append((minimum(liste[i])))
            mod.append((mode(liste[i])))
            
        #print(moye)
        #for i in range(len(liste)):
        row = [moye,med,var,ecart,premier,troisieme,maxi,mini,mod]    
        writer.writerows(row)                                         # ecrire une liste sur une ligne



def afficher():
    """ ici, on lit le contenu de notre fichier et l'affiche à l'ecran """
    
    try:
        with open("resultat.csv",'r') as infile, open("resultat.txt",'w') as outfile:
            for line in infile:
                outfile.write((line.replace(';',' '.ljust(20))))
                
        with open("resultat.txt",'r') as outfile:
            print(outfile.read())
            #reader = csv.reader(file, delimiter = ';', quotechar = '|')
            #for line in reader:
             #   print (line)
        
    except IOError:
        print("!!!!!! vous n'avez effectuer aucune opération")


   
       
