from main6 import *

#lecture du fichier
numListe = file_to_list(file = "data_exo_6.txt")

#tier la liste de numero
a = trier_numero(numListe)

#finalisation de la liste de numero
f = finalisation(a)

#reecriture dans une nouvelle liste 
list_to_file(f)

print("Ouvrez le fichier data_exo_6_new.txt pour voir le resultat")