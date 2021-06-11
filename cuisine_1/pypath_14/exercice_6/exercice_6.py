

def standardisation(func):
    """
        ce derateur permet d'ajouter le prefixe aux numeros
    """

    def  inner(contact):

        contact_trie  = func(contact)
        stantard = ["+237 6"+numero for numero in contact_trie]

        return stantard
    return inner


@standardisation
def trie_contact(mes_contact):

    """
        cette fonction prend en paramettre une liste de contats
        faire une pretraitement dessus (enlever +2376, enlever 2376 et 6)
        avant de range dans l'ordre 

    """


    mes_numeros =["".join(list(numero)[-8:]) for numero in mes_contact if len(numero)>= 8]
    # ici on se preoccupe pas du format sous lequel est le numero , on recupere les 8  derniers
    # chiffres et j'obtiens un numero sans prefixe 
    # la condition est pour supprimer les numeros eventuellement mal ecrit

    mes_numeros.sort() # on trie la liste de numero puis on la renvois
    return mes_numeros

    """
        for i in range(1,len(mes_contact)) :
            me
            
            if len(mes_contact[i]) == 13 :
                mes_numeros.append("".join(list(mes_contact[i])[5:]))
                #on est sur le format +2376 xxxxxxxx
                #sur la ligne on recupere le contact  comme c'est une  chaine de caractère
                #on le cast en liste puis je lui retire les 5 premier caractére en commencant par l'indice 5
            elif len(mes_contact[i]) == 12:
                mes_numeros.append("".join(list(mes_contact[i])[4:]))
                #on  est dans le cas où on commence pa 237 6

            elif len(mes_contact[i]) == 9:
                mes_numeros.append("".join(list(mes_contact[i])[1:]))

            else : 
                mes_numeros.append(mes_contact[i])
    """
   
   




def  save (contact):
    """ 
        cette foction permet de sauvegarder les contacts dans un fichier
    """
    with open("resultat.txt" ,'w') as f : 
        for i in contact : 
            f.write(i+'\n')



mes_contact = [ numero.strip() for numero in open("data_exo_6.txt")]
save(trie_contact(mes_contact))








    