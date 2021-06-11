import time
from main7 import *


f = init()


print(
        """ \033[38;2;132;220;51;1;48;2m
            * * * *     *       *      * * * * *     *     *       * * * *     *        *  
            *     *       *   *            *         *     *       *     *     *  *     *
            * * * *         *              *         * * * *       *     *     *    *   *
            *               *              *         *     *       *     *     *      * *
            *               *              *         *     *       * * * *     *        * ...PATH
        \033[00m""")
  
time.sleep(1)
print(
        """ \033[36;2;132;220;51;1;48;2m
          +---------------------------------------+
          |              STATISTAS                |
          +---------------------------------------+
        \033[00m""")

input("        \033[31;2;132;220;51;1;48;2mAppuyer sur entrée pour continuer...\033[00m")
clear()
print( 
          """ \033[38;2;132;220;51;1;48;2m
        Bien commencons!!!

        Voici les elements sur lesquels vous pouvez effectuer des calculs.
        \033[00m""")
time.sleep(1)
print(first_line())

mot = input( 
          """ \033[35;2;132;220;51;1;48;2m
        Sur quel element souhaitez vous effectuer un calcul?
        \033[00m""")

liste = init_list(mot, f)
liste = trans_liste(liste)

while mot not in first_line():
      print( 
                """ \033[31;2;132;220;51;1;48;2m
                  Element non existant!!!
                \033[00m""")
      mot = input( 
          """ \033[35;2;132;220;51;1;48;2m
        Sur quel element souhaitez vous effectuer un calcul?
        \033[00m""")


menu()
choix = input( 
          """ \033[38;2;132;220;51;1;48;2m
        Quel calcul souhaitez vous effectuer sur l'element {}?
        \033[00m""".format(mot))
try:
    choix = int(choix)
except:
  print( """ \033[31;2;132;220;51;1;48;2m
                  Veuillez entrer des entiers entre 1 et 12!!!
                \033[00m""") 

med=moy=max=min=p_q=t_q=var=0
mode=[]

while choix != 13:
  try:
    if choix not in [1,2,3,4,5,6,7,8,9,10,11,12,13] :
      print( 
                """ \033[31;2;132;220;51;1;48;2m
                Veuillez entrer des entiers entre 1 et 12!!!
                \033[00m""")

    if choix == 1:
      moy = moyenne(liste)
      print( """ \033[36;2;132;220;51;1;48;2m
                  La moyenne de {} est {}
                  \033[00m""".format(mot,moy))

    if choix == 2:
      med = mediane(liste)
      print( """ \033[36;2;132;220;51;1;48;2m
                  La mediane de {} est {}
                  \033[00m""".format(mot,med))
    if choix == 3:
      max = maxi(liste)
      print( """ \033[36;2;132;220;51;1;48;2m
                  Le maximum de {} est {}
                  \033[00m""".format(mot,max))

    if choix == 4:
      min = mini(liste)
      print( """ \033[36;2;132;220;51;1;48;2m
                  Le minimum de {} est {}
                  \033[00m""".format(mot,min))

    if choix == 5:
      p_q = premier_quartile(liste)
      print( """ \033[36;2;132;220;51;1;48;2m
                    Le premier quartile de {} est {}
                    \033[00m""".format(mot,p_q))

    if choix == 6:
      t_q = troisieme_quartile(liste)
      print( """ \033[36;2;132;220;51;1;48;2m
                    Le troisieme quartile de {} est {}
                    \033[00m""".format(mot,t_q))

    if choix == 7:
      try:
        mode = mode(liste)
        print( """ \033[36;2;132;220;51;1;48;2m
                    Le mode de {} est {}
                    \033[00m""".format(mot,mode))
      except TypeError:
        print( """ \033[36;2;132;220;51;1;48;2m
                    La liste a un probleme \033[00m""")
        

    if choix == 8:
      ect = ecart_type(liste)
      print( """ \033[36;2;132;220;51;1;48;2m
                    L'ecart type de {} est {}
                    \033[00m""".format(mot,ect))

    if choix == 9:
      var = variance(liste)
      print( """ \033[36;2;132;220;51;1;48;2m
                    La variance de {} est {}
                    \033[00m""".format(mot,var))

    if choix == 10:

      ecrire_fichier(mot,med,moy,max,min,p_q,t_q,var,mode)
      print( """ \033[36;2;132;220;51;1;48;2m
                    Sauvegarde reuissit!!!
                    \033[00m""")

    if choix == 11:
      try:
        print( """ \033[36;2;132;220;51;1;48;2m
                  Liste de toutes les listes et calculs ayant deja ete faites
                  -----------------------------------------------------------
                  \033[00m""")
                    
        lire_fichier()
      except:
        print(""" \033[31;2;132;220;51;1;48;2m
                  Une Erreur est survenue essayer ulterieurement!!!
                  \033[00m""")

    if choix == 13:
      quitter()

    if choix == 12:
      clear()
      print( 
            """ \033[38;2;132;220;51;1;48;2m
          Bien commencons!!!

          Voici les elements sur lesquels vous pouvez effectuer des calculs.
          \033[00m""")
      time.sleep(1)
      print(first_line())

      mot = input( 
            """ \033[35;2;132;220;51;1;48;2m
          Sur quel element souhaitez vous effectuer un calcul?
          \033[00m""")

      liste = init_list(mot, f)
      liste = trans_liste(liste)

      while mot not in first_line():
        print( 
                  """ \033[31;2;132;220;51;1;48;2m
                    Element non existant!!!
                  \033[00m""")
        mot = input( 
            """ \033[35;2;132;220;51;1;48;2m
          Sur quel element souhaitez vous effectuer un calcul?
          \033[00m""")


      menu()
      choix = input( 
            """ \033[38;2;132;220;51;1;48;2m
          Quel calcul souhaitez vous effectuer sur l'element {}?
          \033[00m""".format(mot))
      try:
          choix = int(choix)
      except:
        print( """ \033[31;2;132;220;51;1;48;2m
                        Veuillez entrer des entiers entre 1 et 12!!!
                      \033[00m""") 



      med=moy=max=min=p_q=t_q=var=0
      mode=[]

    menu()
    choix = input( 
              """ \033[38;2;132;220;51;1;48;2m
            Quel calcul souhaitez vous effectuer sur l'element {}?
            \033[00m""".format(mot))
    try:
        choix = int(choix)
    except:
      print( """ \033[31;2;132;220;51;1;48;2m
                    Veuillez entrer des entiers entre 1 et 12!!!
                  \033[00m""") 
    

  except KeyboardInterrupt:
    print(  """ \033[31;2;132;220;51;1;48;2m
                  Pour quitter le programme choisir l'option QUitter du menu
                  \033[00m""")









