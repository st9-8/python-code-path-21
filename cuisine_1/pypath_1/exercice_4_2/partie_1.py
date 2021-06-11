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
     
        

