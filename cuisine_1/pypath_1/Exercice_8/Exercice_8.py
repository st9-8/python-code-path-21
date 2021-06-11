#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

"""  
    fonction de cryptage qui  remplace les lettres par leur 
valeur dans le cryptage et vise vera pour le decryptage 
"""
def Cryptage(phrase,dico_cryptage):
    crypter=""
    for i in phrase:
        if i==" ":
            crypter= crypter + " "
        else:
            crypter=crypter + dico_cryptage[i]
    return crypter        
   

def Decryptage(phrase,dico_decryptage):
    decrypter=""
    for i in phrase:
        if i==" ":
            decrypter= decrypter + " "
        else:
            decrypter=decrypter + dico_decryptage[i]
    return decrypter   

def main():
    print("BIENVENENU SUR LE PROGRAMME DE CRYPTAGE DECRYPTAGE ")
    phrase=input("veillez entrer la phase que vous voulez crypter ")
    k=int(input("entrer un entier correspondant au decalage de votre chaine "))
    
        # creation d'une liste  conteant les caracteres de l'alphabet avec la fonction string
    alphabet=list(string.ascii_lowercase)
    #creation d'une liste  en fonction du decalage entree par l'utilisateur
    j=26-k
    decalage=alphabet[-k:]+alphabet[:j]
    """
    creation de dictionnaire ayant pour cle les caracteres a crypter
     et pour valeur les equivalents dans le cryptages et vise versa
     """
    i=0
    dico_cryptage={}
    dico_decryptage={}
    while i<=25:
        dico_cryptage[alphabet[i]]=decalage[i]
        dico_decryptage[decalage[i]]=alphabet[i]
        i+=1
        
    print("la chaine crypte est la suivante") 
    crypt=Cryptage(phrase,dico_cryptage)
    print(crypt,"\n")
    print("voulez vous decrypter cette chaine?")
    print("1.oui  merci de decrypter")
    print("2.non merci")
    choix=int(input(" entrer votre choix "))
    if choix==1:
        print(Decryptage(crypt,dico_decryptage))
        print("merci d'avoir utilisé notre programme")
        
    else:
        print("merci d'avoir utilisé notre programme")
        
main()        
           
    
    
    
    
    
    