#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import time


def Exercice_3():
    #menu du jeu
    print("******************************************BIENVENUE SUR LE JEU********************************")
    print("\n\n","*****************voici les règles du jeu*****************")
    print("********** les règles sont simple ici vous jouez contre la machine il s'agit du très célèbre jeu PIERRE, FEUILLE, CISEAU")
    print("\n\n","1. la pierre bat le ciseau")
    print("2.le ciseau bat la feuille")
    print("3.la feuille bat la pierre")
    print("la machine fera son choix et vous essayer de la battre")
    print("c'est partie vous pouvez commencer")
    k=0
    Victoire=0
    #initialisation des victoires
    while k!=-1:
        
        liste = ['pierre','feuille','ciseau' ]
        #choix aleatoire du mot 
        choix_machine=random.choice(liste)
        print("la machine a fait son choix faite le votre.....")
        i=0
        while i!=-1:
            choix=str(input("votre choix est   "))
            choix=choix.lower()
            # se rassurer que l'utilisateur entre un element qui est dans la liste
            if choix in liste:
                i=-1
            else:
                print("votre choix n'est pas valide veillez recommencer" )
                i=i+1
        #  mettre une pause pour le suspend avec un compte        
        for i in range(0,4):
            print(i)
            time.sleep(1)  
        print("\n")
        #verification du choix de l'utilisateur et comparaison avec celui de la machine
        if choix_machine=='pierre' and choix=='feuille':
            print("le choix de la machine est ",choix_machine)
            print("\n Felicitation vous  gagnez !!!!!!!!!!!!!!!!")
            Victoire= Victoire + 1
            
        if choix_machine=='ciseau' and choix=='pierre':
            print("le choix de la machine est ",choix_machine)
            print("\n Felicitation vous  gagnez !!!!!!!!!!!!!!!!")
            Victoire= Victoire + 1
            
        if choix_machine=='feuille' and choix=='ciseau':
            print("le choix de la machine est ",choix_machine)
            print("\n Felicitation vous  gagnez !!!!!!!!!!!!!!!!")
            Victoire= Victoire + 1
        if choix == choix_machine:
              print("le choix de la machine est ",choix_machine)
              print("\n Felicitation vous  gagnez !!!!!!!!!!!!!!!!")
              Victoire= Victoire + 1
        else:
            print("le choix de la machine est ",choix_machine)
            print("\n OOOoooops désolé vous avez perdu !!!")
        
        print("\n\n","voulez vous refaire une partie??  entere O pour oui et N pour non")
        #recuper la reponse de l'utilisateur
        i=0
        while i!=-1:
            
             ch=str(input(" "))
             ch=ch.lower()
             if ch =='o' or ch =='n':
                i=-1
             else:
                 print("votre choix n'est pas valide veillez recommencer" )
                 i=i+1
                
       
        if ch== 'o':
            k += 1
        else:
            print(" merci d'avoir pris par à ce jeu")
            print("votre score est ", Victoire)
            k=-1
Exercice_3()

