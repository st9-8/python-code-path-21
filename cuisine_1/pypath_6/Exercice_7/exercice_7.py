from collections import Counter
from math import *
import def_func,platform,time

terminer=False
print("\t\tBienvenue !\n\t\t Statista tourne sur",platform.system())
save=False
try:
   while terminer == False:
     choix=def_func.Menu()
     if choix==1:
        p=def_func.recherche_entete()
        liste=def_func.liste_init(p)
        moyen=def_func.moyenne(liste)
        print("La moyenne vaut",moyen)
     elif choix==2:
        p = def_func.recherche_entete()
        liste = def_func.liste_init(p)
        median=def_func.mediane(liste)
        print("La mediane vaut", median)
     elif choix==3:
        p = def_func.recherche_entete()
        liste = def_func.liste_init(p)
        max=def_func.maximum(liste)
        print("Le max est",max)
     elif choix == 4:
        p = def_func.recherche_entete()
        liste = def_func.liste_init(p)
        min = def_func.minimun(liste)
        print("Le minimum est", min)
     elif choix == 5:
        p = def_func.recherche_entete()
        liste = def_func.liste_init(p)
        mod = def_func.mode(liste)
        print("Le mode est", mod)
     elif choix == 6:
        p = def_func.recherche_entete()
        liste = def_func.liste_init(p)
        q1 = def_func.quartile1(liste)
        print("Le premier quartile est", q1)
     elif choix == 7:
        p = def_func.recherche_entete()
        liste = def_func.liste_init(p)
        q2 = def_func.quartile2(liste)
        print("Le second quartile est", q2)
     elif choix == 8:
        p = def_func.recherche_entete()
        liste = def_func.liste_init(p)
        q2 = def_func.variance(liste)
        print("La variance est", q2)
     elif choix == 9:
        p = def_func.recherche_entete()
        liste = def_func.liste_init(p)
        q2 = def_func.ecart_type(liste)
        print("L'ecart -type est", q2)
     elif choix == 10:
        def_func.coefficient_Pearson()
     elif choix == 11:
         def_func.tableau_freq_effect()
     elif choix == 12:
        save = True
        def_func.sauvegarder()
     elif choix == 13:
        def_func.Afficher_tout()
     elif choix == 14:
        print("Fin du programme....")
        terminer = True
     else:
        print("Error")
except KeyboardInterrupt:
    print("Vous ne pouver quitter le programme qu'en appuyan sur quitter")