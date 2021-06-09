encoding = 'utf-8'
import pandas as pd
import colorama
import csv
import os.path



def plateforme():
    print('system:',platform.system)
    
def moy(liste):
    try:
        moyen = sum(liste)/len(liste)
        
    except ZeroDivisionError:
        print("la liste est vide")
    else:
        return (moyen)

def median(liste):
    try:
        a = len(liste)
        l= liste.sort()
        if a%2 == 0:
            med = ((liste[(a//2)+1] + liste[a//2])/2)
        else:
            med = liste[(a+1)//2]
    except IndexError:
        print("impossible de trouver la médiane")
    else:
        return (med)

def Premier_quartile(liste):
    try:
        a = len(liste)
        l= liste.sort()
        if a%4 == 0:
            Q1 = ((liste[(a//4)+1] + liste[a//4])/2)
        else:
            Q1 = liste[(a+1)//4]
    except IndexError:
        print("impossible de trouver le premier quartile")
    else:
        return (Q1)

def troisieme_quartile(liste):
    try:
        a = len(liste)
        l= liste.sort()
        if a%4 == 0:
            Q3 = ((liste[(a//4)+1] + liste[a//4])/2)
        else:
            Q3 = liste[(a+1)//4]
    except IndexError:
        print("impossible de trouver lE troisime quartile")
    else:
        return (Q3)
    
def mode(liste):
    dic = {}
    for i in liste:
        dic[i] = liste.count(i)
    for k, val in dic.items():
         if val == max(dic.values()):
             return (k)
        
    #return(str(key_list))

def ecart_type(liste):
    try:
        y=math.sqrt(variance(liste))
    else:
        return (y)

def variance(liste):
    try:
        dev=[(x-moyen(liste))**2
        variance = sum(deviation)/len(liste)       
    except ZeroDivisionError:
        print("la liste est vide")
    else:
        return (variance)

def coefficient_pearson(liste):
    pass

def effectifs(liste):
    pass

def frequences(liste):
    freq=0
    for x in liste:
        S+=x
        freq=[]
    for x in liste:
        L.append(x/freq)
    return (freq)

def effectifs_cumules(liste):
       L=[]
       somme_partielle=0
       for x inn liste_effectifs:
           somme_partielle+=x
           L.append(somme_partielle)
        return (L)

def frequences_cumules(liste):

    return (freq_c)

def tableauFE(liste):
    try:
    else:
        return (tableau)


def sauvegarder():
    f = open("resultat.txt",'w', encoding = 'utf-8')
    #for i in {"Moyenne","Médiane","Maximum","Minimum","Mode"}:
    
    f.write("Moyenne\t\tMédiane\t\tMaximum\t\tMinimum\t\tMode\n")
    
    moye = str(moy(liste))
    med = str(median(liste))
    maxi = str(max(liste))
    mini = str(min(liste))
    mod = str(mode(liste))
    
    f.write(moye + "\t\t" + med + "\t\t" + maxi + "\t\t" +mini + "\t\t" + mod)
    
       
   
def afficher():
    try:
        f  = open("resultat.txt","r", encoding = "utf_8")
        print (f.read())
        f.close
    except IOError:
        print("!!!!!! vous n'avez effectuer aucune opération")
    

# menus

menu1 = {}
menu1['1']="Age" 
menu1['2']="Pression"
menu1['3']="Cholester"
menu1['4']="Taux_Max"
menu1['5']="quitter"

menu['1']="Moyenne" 
menu['2']="Médiane"
menu['3']="premier quartile"
menu['4']="troisieme quartile"
menu['5']="Maximum"
menu['6']="Minimum"
menu['7']="Mode"
menu['8']="ecart-type"
menu['9']="Variance"
menu['10']="coefficient de pearson"
menu['11']="tableau des effectifs et des frequences cumulé(e)s"
menu['12']="Sauvegarder tous"
menu['13']="Afficher tous"
menu['14']="Quitter le programme"

 #--------lecture du fichier data_exo_7.txt
try:
    f = open("G:\essai\data_exo_7.txt","r", encoding = "utf_8")
    print (f.read())
    f.close

# --------le corps du programme
    user=os.getlogin()
    print(user)
    plateforme()
    
    print("\n-----------------> veuillez choisir une des colonnes ci-dessous!!!!")
    while True:
        options = sorted(menu1.keys())
        for entry in options:
            print (entry, menu1[entry])

        with open("G:\essai\data_ex0_7.txt","r", encoding = "utf_8") as infile, open("data_exo_7.csv",'w') as outfile:
            for line in infile:
                outfile.write(line.replace('|',';'))
        reader = pd.read_csv('data_exo_7.csv',  sep=';', encoding ="ISO-8859-1")
        columns = reader.columns

        #print(len(reader))
        #print(reader[columns[0]][4])
        try:
            choix = input("\n sur quelle parametre du premier menu souhaitez-vous travailler?:\n")
            liste = []
            if choix == "1":
                for i in range(len(reader)):
                    liste.append(reader[columns[0]][i])
                    plateforme()
        
            elif choix == "2":
                 for i in range(len(reader)):
                     liste.append(reader[columns[1]][i])
            elif choix == "3":
                 for i in range(len(reader)):
                    liste.append(reader[columns[2]][i])
            elif choix == "4":
                for i in range(len(reader)):
                    liste.append(reader[columns[3]][i])
            elif choix == '5':
                exit()
            else:
                print("\n--------------->Entrer invalide choissez une bonne option svp\n")
                continue
        
            print("\n_*_*_*_*Les element de la colonne que vous avez choisi sont  *_*_*_*:\n ",liste)

            print("\n Quelle opération souhaitez  vous effectuer  ?????????")
            while True:
                options = sorted(menu.keys())
                for entry in options:
                    print (entry, menu[entry])

                try:
                    selection=input("\n choisissez svp !!!!!!: \n ")
    
                    if selection =='1':
                        print ("\nLa moyenne du parametre " ,menu1[choix], " est: ", moy(liste))
                    elif selection =='2':
                        print ("\nLa mediane du parametre  " ,menu1[choix], " est: ", median(liste))
                    elif selection =='3':
                        print ("\nLe premier quartile du parametre  " ,menu1[choix], " est: ", premier_quartile(liste))
                    elif selection =='4':
                        print ("\nLa troisieme quartile du parametre  " ,menu1[choix], " est: ", troisieme_quartile(liste))
                    elif selection == '5':
                        print ("\nLe maximum ", menu1[choix]," est: ", max(liste))
                    elif selection == '6':
                        print ("\nLe minimum ", menu1[choix]," est: ", min(liste))
                    elif selection =='7':
                        print ("\nLe mode ", menu1[choix], " est: ", mode(liste))
                    elif selection =='8':
                        print ("\nL'ecart-type du parametre  " ,menu1[choix], " est: ", ecart_type())
                    elif selection =='9':
                        print ("\nLa variance du parametre  " ,menu1[choix], " est: ", variance()) 
                    elif selection == '10': 
                        print ("\nLe coefficient de Pearson de la colone ", menu1[choix], " est: ", coefficient_pearson())
                    elif selection == '11':
                        print ("\nLe tableau des effectifs et des frequences cumulé ")
                        tableauFE()
                    elif selection == '12':
                        sauvegarder()
                        print ("\nDonnées sauvegardées de la colonne ", menu1[choix], "!!!!!")
                    elif selection == '13':
                        print ("\nVisualisation des caractéristique de: \n", menu1[choix])     
                        afficher()
                        break   
                    elif selection == '14':
                        sauvegarder()
                        print("vos resultats ont été enregistrer dans le fichier resultat.txt de votre repertoire courant, merci!!!")
                        break
                    else: 
                        print ("option inconnu selection l'une des option sus-citées!\n" )
                   

                except KeyboardInterrupt:
                    print("pour arretez vos opération , appuyer  exit")
    
        
        except KeyboardInterrupt:
            print("pour quitter le programme, appuyer  exit")
except IOError:
    print("!!!!!!! fichier introuvable ")
#os.system("pause")

