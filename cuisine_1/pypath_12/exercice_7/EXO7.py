encoding = 'utf-8'
import csv
import os.path
import colorama
import platform
import pandas as pd
    
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
        y=math.sqrt(variance(liste))
        return (y)

def variance(liste):
    try:
        dev=[(x-moyen(liste))**2]
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
    for x in liste_effectifs:
        somme_partielle+=x
        L.append(somme_partielle)
    return (L)

def frequences_cumules(liste):
    pass

def tableauFE(liste):
    pass


def sauvegarder():
    f = open("resultat.txt",'w', encoding = 'utf-8')
    #for i in {"Moyenne","Médiane","Maximum","Minimum","Mode",'variance','ecart_type','tableau des effectifs et frequences cumulés'}:
    
    f.write("Moyenne\t\tMédiane\t\tMaximum\t\tMinimum\t\tMode\t\tVariance\t\tEcart_type\t\tTableau des effectifs et frequences cumulés")
    
    moye = str(moy(liste))
    med = str(median(liste))
    maxi = str(max(liste))
    mini = str(min(liste))
    mod = str(mode(liste))
    var=str(variance(liste))
    ecartT=str(ecart_type(liste))
    tab=tableauFE(liste)
    
    f.write(moye + "\t\t" + med + "\t\t" + maxi + "\t\t" +mini + "\t\t" + mod+ "\t\t" + var + "\t\t" + ecartT + "\t\t" +tab )

      
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

menu={}
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
    f = open("data_exo_7.txt","r", encoding = "utf_8")
    print (f.read())
    f.close

# --------le corps du programme
    user=os.getlogin()           #affiche le nom de l'utilisateur dans le systeme qui execute le programme
    print("\n L'administrateur de ce PC est: ",user)
    print("\n Vous travaillez sur un systeme: ",platform.system())              #affiche le systeme sur lequel on focntionne
    print('\n')
    print('BIENVENUE DANS VOTRE ANALYSEUR DE DONNEES')
    print('*****************************************')
    print('\n')
    
    while True:
        options = sorted(menu1.keys())
        for entry in options:
            print (entry, menu1[entry])

        try:
            choix = input("\n sur quelle parametre du premier menu souhaitez-vous travailler?: ")
            liste = []
            sortie=pandas.read_csv('data_exo_7.csv',usecols=[(choix)])
            print(sortie)
            if choix == "1":
                for i in range(len(reader)):
                    liste.append(reader[columns[0]][i])
        
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
                print("\n--------------->Entrer invalide choissez une bonne option svp: ")
                continue
        
            print("\n_*_*_*_*Les element de la colonne que vous avez choisi sont  *_*_*_*:\n ",liste)
            
            print("\n ------------> Quelle opération souhaitez  vous effectuer  ?????????")
            while True:
                options = sorted(menu.keys())
                for entry in options:
                    print (entry, menu[entry])

                try:
                    selection=input("\n choisissez svp !!!!!!: ")
    
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

