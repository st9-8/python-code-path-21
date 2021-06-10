from collections import Counter
from math import *
import time
#separer les donnees du fichier, chaque ligne devient une liste
c=[]
fichier = open("data_exo_7.txt", "r")
c.append(fichier.readline().split("\t"))
for i in fichier:
   c.append(fichier.readline().split("\t"))

fichier.close()

""""
#liste de liste(comme les elements du fichier, donc en colonne)
d=[]
for i in range(0,len(c[0])):
    p = []
    for j in range(1,len(c)):
        p.append(c[j][i])
    d.append(p)
print(d)
"""
def recherche_entete():
    print("Les entetes des colonnes sont",c[0])
    p=-1
    while p == -1:
        word = input("veillez entrer un  nom")
        for i in range(0,len(c[0])):
          if word == c[0][i]:
            print("Colonne trouvee")
            p = i#position de l'entete de la colonne dans la premiere liste du tableau
        if p == -1:
            print("colonne  inexistance")
    return p
def liste_init(p):
    liste=[]
    for i in range(1,len(c)):
        liste.append(int(c[i][p]))
    return liste



def Menu():
    time.sleep(5)
    possible = str(list(range(1,15)))
    print("1-Moyenne d'une colonne\n"
          "2-Medianne d'une colonne\n"
          "3-Maximum d'une colonne\n"
          "4-Minimum d'une colonne\n"
          "5-Mode d'une colonne\n"
          "6-Premier quartile d'une colonne\n"
          "7- Troisieme quartile d'une colonne\n"
          "8-Variance d'une colonne\n"
          "9-Ecart-type d'une colonne\n"
          "10-Coefficient de Pearson\n"
          "11-Tableau effectifs et frequences\n"
          "12-Sauvegarder tout\n"
          "13-Afficher tout\n "
          "14-Quitter\n")
    choix=input("entrer votre choix")
    if choix in possible:
        choix=int(choix)
        return choix
    else:
        while choix not in possible:
           choix=input("veillez entrer une valeur comprise entre 1 et 14")
        choix=input(choix)
        return choix




def mode(liste):
    counter = Counter(liste)
    max_count = max(counter.values())
    modo = [k for k, v in counter.items() if v == max_count]
    return modo


def moyenne(liste):
    return (1/len(liste))* sum(liste)

def mediane(liste):
    return sum(liste)/2

def maximum(liste):
    return max(liste)

def minimun(liste):
    return min(liste)

def variance(liste):
    moyen=moyenne(liste)
    var=0
    for i in range(0,len(liste)):
        var += (liste[i]-moyen)**2
    return var * (1/len(liste))

def ecart_type(liste):
    var=variance(liste)
    return sqrt(var)

def effectif(liste):
    liste=sorted(liste)
    effect=Counter(liste)
    return effect

def effectif_cumule(liste):
    eff=effectif(liste)
    last=0
    a = set(liste)
    a = list(a)

    b=[]
    for i in a:
        b.append({i: eff[i] + last})
        last = eff[i] + last
    return b
def frequence(liste):
    eff = effectif(liste)
    k= eff.keys()
    val=[]
    for i in k:
        val.append(eff[i])
    b = sum(val)
    freq=[]
    for x in eff.keys():
        y=eff[x]/b
        freq.append({x:y})
    return freq
def frequence_cumule(liste):
    g=effectif_cumule(liste)
    k=effectif(liste)
    keyss = k.keys()#liste des cles des effectifs
    k = list(k.items()) # liste de dictionnaire cle valeur des effectifs

    val=[]

    for v in keyss:
        keye = v ###recupere la cle de chaque element
        for i in k:
           if list(i)[0] == keye :
               val.append(list(i)[1])##liste des valeurs de chaque cle
    mysum = sum(val)
    val = []
    for i in g:
        c = list(i)[0]#liste de cle des effectifs
        p = i[c]
        val.append({c : (p/mysum)})


    return val

def quartile1(liste):

    if len(liste)%4==0:
        q1=liste[(len(liste)//4)-1]
    if len(liste)%4==1:
        q1=liste[((len(liste)+3)//4)-1]
    if len(liste)%4==2:
        q1=liste[((len(liste)+2)//4)-1]
    if len(liste) % 4 == 3:
        q1 = liste[((len(liste) +1)// 4) - 1]
    return q1

def quartile2(liste):
    if len(liste)%4==0:
        q3=liste[(len(liste)*3//4)-1]
    if len(liste)%4==1:
        q3=liste[((len(liste)+3)*3//4-2)-1]
    if len(liste)%4==2:
        q3=liste[((len(liste)+2)*3//4-2)]
    if len(liste)%4==0:
        q3=liste[((len(liste)+1)*3//4-1)]
    return q3
def coefficient_Pearson():
    print("desolee ce service est actuellement indisponible")
def tableau_freq_effect():
    p = recherche_entete()
    liste = liste_init(p)
    eff=effectif(liste)
    ele=eff.keys()
    eff_cumul=effectif_cumule(liste)
    freq=frequence(liste)
    freq_cumul=frequence_cumule(liste)
    print("Nombre \t\t Effectif \t\t Effectif cumulee\t\tFrequence\t\tFrequence cumulee\n")
    for i in range(len(eff)):
      print("  {}\t\t{}\t\t{}\t\t{}\t\t{}".format(ele[i],eff[i],eff_cumul[i],freq[i],freq_cumul[i]))

def sauvegarder(save):# save verifie si c'est la premiere fois qu'on sauvegarde
    pass
def Afficher_tout():
    pass

list1=[1,1,1,2,2,3,4,5]
eff=effectif(list1)
a=set(list1)
a=list(a)
b=[]
last = 0
#for i in a :
    #b.append({i: eff[i]+last })
    #last = eff[i]+last
keye = 1
#for i in b:
 #   print(list(i.values()))
  #  if list(i)[0] == keye :
   #     print(list(i.values()))
#j=effectif(list1)
#print("effectif",j)
#f=effectif_cumule(list1)
#print("effectif cumule",f)
#h=moyenne(list1)
#print("moyenne:",h)
#e=frequence(list1)
#print("frequence",e)
#g=frequence_cumule(list1)
#print("frequence_cumule",g)
#poo=({1:2},{4:3})
