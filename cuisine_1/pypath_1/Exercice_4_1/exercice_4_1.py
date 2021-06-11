#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# definition du decorateur
def decorateur(fonction):
    def inner(texte,g=False,i=False,b=False):
        if g==True:
            texte="*"+texte+"*"
        if i==True:
            texte="_"+texte+"_"
        if b==True:
            texte="~"+texte+"~"
        print(texte) 
    return inner
#utilisation du decorateur
@ decorateur
def fonction(texte,g=False,i=False,b=False):
    return texte

fonction("SEED_COMMUNITY #PATH_PYTHON 2k21",g=True,i=True,b=True)
