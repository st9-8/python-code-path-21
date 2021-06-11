import math
import pandas
import os.path
import colorama
import platform


      
def afficher():



#-------------------menus

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


# --------le corps du programme

user=os.getlogin()           #affiche le nom de l'utilisateur dans le systeme qui execute le programme
print("\n L'administrateur de ce PC est: ",user)
print("\n Vous travaillez sur un systeme: ",platform.system())              #affiche le systeme sur lequel on focntionne
print('\n')
print('BIENVENUE DANS VOTRE ANALYSEUR DE DONNEES')
print('*****************************************')
print('\n')

print('****** LES PARAMETRES: ',menu1)
print('\n')
choix = input("\n Sur quel parametre du premier menu souhaitez-vous travailler?: \n")
        
#-------------------ouverture du fichier
df=pandas.read_table('data_exo_7.txt',sep='\t',header=0)

#-------------traitement sur les parametres et le fichier a traiter
if choix=='1':
    print('vous travaillez sur la colonne des ages')
    X=list(df['age'])
elif choix=='2':
    print('vous travaillez sur la colonne des pressions')
    X=list(df['pression'])
elif choix=='3':
    print('vous travaillez sur la colonne des ages')
    X=list(df['cholester'])
elif choix=='4':
    print('vous travaillez sur la colonne des ages')
    X=list(df['taux_max'])
else:
    print('faites un choix valide')


#-----------------les calculs
    for i in X:
            A=len(X)
            B=sum(X)
#-----------------calcul de la moyenne
            moy=A/B
            C=(B**2)/A
            
#---------------------calcul de la variance
            variance=C-(moy**2)
            
#-----------------------calcul de l'ecart type
            EcartT=math.sqrt(variance)
            covariance=A*B-moy
            
#----------------calcul du coefficient de pearson
            ceifficient_person=covariance/EcartT

#-----------------calcul de la mediane
            if A%2 == 0:
                med = (X[(A-1)//2] + X[A//2])/2
            else:
                med = X[(A-1)//2]


#--------------------determination du maximum et minimum de la liste
            mini = X[0]
            for i in range(len(X)):
                if X[i] < mini:
                    mini = X[i]

            maxi = X[0]
            for i in range(len(X)):
                if X[i] > maxi:
                    maxi = X[i]

            
#----------------------------calcul du premier et du troisieme quartile        
            if A%4 == 0:
                Q1 = ((X[(A//4)+1] + X[A//4])/2)
            else:
                Q1 = X[(A+1)//4]

            if A%4 == 0:
                Q3 = ((X[(3*A//4)+1] + X[3*A//4])/2)
            else:
                Q3 = X[(3*A+1)//4]

#---------------------determination des effectifs


#--------------------calcul des frequences
            freq=0
            for i in X:
                S+=i
                freq=[]
            for i in X:
                L.append(x/freq)

#-------------------------calcul des effectifs cumulés
                L=[]
                somme_partielle=0
                for x in liste_effectifs:
                    somme_partielle+=x
                    L.append(somme_partielle)

#--------------------calcul des frequences cumulées

#-------------------calcul du mode



#-----------execution des differentes operations 
print('******* MENU:',menu2)
selection=input("\n ------------> Quelle opération souhaitez  vous effectuer  ?????????")
print('\n')
if selection =='1':
       print ("\nLa moyenne du parametre " ,menu1[choix], " est: ", moy)
elif selection =='2':
       print ("\nLa mediane du parametre  " ,menu1[choix], " est: ", med)
elif selection =='3':
       print ("\nLe premier quartile du parametre  " ,menu1[choix], " est: ", Q1)
elif selection =='4':
       print ("\nLa troisieme quartile du parametre  " ,menu1[choix], " est: ", q3)
elif selection == '5':
       print ("\nLe maximum ", menu1[choix]," est: ", maxi)
elif selection == '6':
       print ("\nLe minimum ", menu1[choix]," est: ", mini)
elif selection =='7':
       print ("\nLe mode ", menu1[choix], " est: ", mode)
elif selection =='8':
       print ("\nL'ecart-type du parametre  " ,menu1[choix], " est: ", ecart_type)
elif selection =='9':
       print ("\nLa variance du parametre  " ,menu1[choix], " est: ", variance) 
elif selection == '10': 
       print ("\nLe coefficient de Pearson de la colone ", menu1[choix], " est: ",coefficient_pearson)
elif selection == '11':
       print ("\n-------->Le tableau des effectifs et des frequences cumulé ")
       print('\n',effectif)
       print('\n',eff_cum)
       print('\n',frequence)
       print('\n',freq_cum)
       
elif selection == '12':
       file=open('resultat.txt','a')
       file.write(
       file.close()
       print ("\nDonnées sauvegardées de la colonne ", menu1[choix], "!!!!!")
       exit()
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
