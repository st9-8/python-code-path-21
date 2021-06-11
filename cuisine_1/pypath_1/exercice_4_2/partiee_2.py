#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:55:05 2021

@author: mel
"""




    # foncytion qui remplace dans le cod ela lettre trouvee
def Deviner(lettre,mot,affichage):
    mot_1=list (mot)
    affichage=list(affichage)
    for i in range(len(mot_1)):
        if mot_1[i]==lettre:
            affichage[i]=lettre
    affiche="".join(affichage)       
    return affiche        

def pendu():
    print("*********************BIENVENU SUR LE JEU DU PENDU IL EST QUESTION DE DEVINER UN MOT LETTRE PAR LETTRE  JUSQU'A TROUVER LE MOT A DEVINER*********************")
    print("\n \n \n \n ")
    solution=lecture()
    solution =solution.lower()
    solution=solution.strip()
    solution=list(solution)
    affichage=""
    for i in solution:
        affichage= affichage + "_"
    print("essaye de deviner le mot si tu peux ")
    print(affichage)

    essai=0
    lettres_trouvees=""
    while essai == 0:
        k=0
        choix=""
        while k==0:
            choix= input("entrez une lettre   ")
            choix=choix.lower()
            if type(choix)==str:
                k=-1
            elif len(choix)!=1:
                print("veillez entrer un seul charactère \n")
            else:
                print("veillez entrer un caractere de l'alphabet \n")
        if choix in lettres_trouvees:
            print("vous avez deja deviné cette lettre")
        elif choix in solution:
            lettres_trouvees = lettres_trouvees + choix
            print("cool trouvé")
            affichage = Deviner(choix,solution,affichage)
            print(affichage)
                    
            if "_" not in affichage:
                  print(affichage,"\n")
                  print(" \n felicitation vous avez gagnez \n")
                  essai=-1
            
            else:
                print(affichage)
        else:
            print(affichage)
            print("desole incorrect")                
           
                
              
            

pendu()
