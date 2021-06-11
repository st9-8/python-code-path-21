#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import random

def lecture():
    fichier= open('sowpods.txt','r')
    dico= fichier.readlines()
    liste_mot=[]
    for mot in dico:
        liste_mot.append(mot)
    choix_machine= random.choice(liste_mot)
    return choix_machine


    # fonction qui remplace dans le cod ela lettre trouvee
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
    k=1
    while k==1:    
        solution=lecture()
        solution =solution.lower()
        solution=solution.strip()
        solution=list(solution)
        affichage=""
        for i in solution:
            affichage= affichage + "_ "
        print("essaye de deviner le mot si tu peux ")
        print(affichage)
    
        essai=6
        lettres_trouvees=""
        
        while essai != 0:
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
                print(affichage)
            elif choix in solution:
                lettres_trouvees = lettres_trouvees + choix
                print("cool trouvé")
                affichage = Deviner(choix,solution,affichage)
                print(affichage)
                        
                if "_" not in affichage:
                      print(affichage,"\n")
                      print(" \n felicitation vous avez gagnez \n")
                      essai=0
                
                else:
                    print(affichage)
            else:
                print(affichage)
                print("desole incorrect") 
                essai= essai -1
                print("il vous reste",essai,"tentatives")
               
        print("voulez vous refaire une partie ? ")   
        print("1.oui  pourquoi pas")
        print("2.non merci")
        choix=int(input(" entrer votre choix "))
        if choix==1:
            k=1
            
        else:
            print("merci d'avoir joué") 
            k=-1
              
            

pendu()

