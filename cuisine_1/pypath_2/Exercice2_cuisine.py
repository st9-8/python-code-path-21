# creons une fonction personnes non servi qui va executé nos operations

def personnes_non_servis(table_A, table_B, list_de_groupe=[]): #notre foncttion prend en parametre deux tables de type integer et une liste de type interger

    for nbr_personne in range(len(list_de_groupe)):#son paraccours la liste de groupe
        if list_de_groupe[nbr_personne] == 1 and table_A == 1:# on regarde si la premiere table peut faire assoeir un groupe d'une personne
            pass  # on passe a la condition suivante si c'est le cas
            if list_de_groupe[nbr_personne] == 1 and table_B == 1:# on verifier sil ya toutes les places de la table b sont libres
                pass  # on passe a la condition suivante si oui
            elif list_de_groupe[nbr_personne] == 1 and table_B == 2:# on verifie si une seul place est libre
                pass # on passe a la condition suivante si oui
            else:
                return list_de_groupe[nbr_personne] # si le groupe na pas de place on retourne leurs nombres
        else:
            if list_de_groupe[nbr_personne] == 2 and table_B == 1: # on verifie sil ya de la place pour un couple sur la table b
                return list_de_groupe[nbr_personne] # si la palce n'est pas suffisante on reourne leurs nombre
            else:
                return 0 # on retourne 0 soi aucune des conditions n'est verfier

table_A = input("entrer le nombre de place de la table_A disponible entre 0 et 1")
print("\n")
table_A = int(table_A)
table_B = input("entrer le nombre de place de la table_A disponible entre 1 et 2")
print("\n")
table_B = int(table_B)
nbr_de_groupe = input('entrer le nbr de groupe de personne entre 1 et 2 desirant etre sevi en espacent')
print("\n")
user_liste = nbr_de_groupe.split()
for i in range(len(user_liste)):
    user_liste[i] = int(user_liste[i])


print(personnes_non_servis(table_A, table_B, user_liste))
