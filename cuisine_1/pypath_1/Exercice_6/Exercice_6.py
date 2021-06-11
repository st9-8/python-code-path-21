#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# cette foonction permet de retirer les elements avant les numeros afin de les comparer
def clean_numero():
    fichier=open('data_exo_6.txt','r')
    numero_brut =fichier.readlines()
    contact=[num.strip() for num in numero_brut]
    numero=[]
    for i in contact:
        if len(i)==13:
            num="".join(list(i)[5:])
            numero.append(num)
        if len(i)==12:
            num="".join(list(i)[4:])
            numero.append(num)
        if len(i)==9:
            num="".join(list(i)[1:])
            numero.append(num)  
        if len(i)==8:
            num="".join(list(i)[0:])
            numero.append(num)
    return numero
# affecter le resultat du nettoyage des numero a une variable 
contacts=clean_numero()
#decorateur pour ajouter +237
def deco(order_contact):
    def inner(contacts):
        # recuperer le resultat de la fonction order_contact car c'est ce resultat qu'on veux decorer
        numero=order_contact(contacts)
        liste_contact=[]
        for i in numero:
            standarise="+237 6"+i
            liste_contact.append(standarise)
        return liste_contact 
    return inner    
        
@ deco
def order_contact(contacts):
    contacts.sort()
    return contacts       
            
num_decorer=order_contact(contacts) # recuperer les numeros decore
# ecriture des numeros dans un fichier
for i in num_decorer:
    f=open('contact.txt','a')
    f.write(i)
    f.write("\n")
f.close()    
