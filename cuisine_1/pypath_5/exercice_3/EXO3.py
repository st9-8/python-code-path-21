#importation des bibliotheques
import numpy
import random
import colorama

#...........la fonction qui definie le jeu
def jouer():
    ordi=random.randint(1,3);
    print("\n Le choix de l'ordinateur est: ",ordi)

    choix=input('\n Faites un choix: ')
    if choix=='1':
        if ordi==1:
            print('\n EGALITÉ')
        elif ordi==2:
            print('\n PERDU!!! Votre score est de: ',score)
        elif ordi==3:
            print('\n La Pierre bat le Ciseau')
            print('\n FELICITATIOOOONS!!! votre score est de:',score+5,'POINTS')

    elif choix=='2':
        if ordi==1:
            print('\n La Feuille bat la Pierre')
            print('\n FELICITATIOOOONS!!! votre score est de:',score+5,'POINTS')
        elif ordi==2:
            print('\n EGALITÉ')         
        elif ordi==3:
            print('\n PERDU!!! Votre score est de: ',score)

    elif choix=='3':
        if ordi==1:
            print('\n PERDU!!! Votre score est de: ',score)
        elif ordi==2:
            print('\n Le ciseau bat la Pierre')
            print('\n FELICITATIOOOONS!!! votre score est de:',score+5,'POINTS')
        elif ordi==3:
            print('\n EGALITE')     

    else:
         print('\n Entrer de bonnes valeurs')

       
#...........Programme principale
menu={}
menu['1']= 'Pierre'
menu['2']= 'Feuille'
menu['3']= 'Ciseau'

score=0
print('***** MENU: *****',menu)

   #..........Appel de la fonction de jeu
while True:
     jouer()

   #.........l'utilisateur peut choisir de continuer le jeu ou arreter le jeu
     decision={}
     decision['1']='OUI'
     decision['2']='NON'

     print('***** voulez vous continuer le jeu? *****',decision)

     reponse=input('\n Quel est votre choix? ')
     if reponse=='1':
       jouer()
     elif reponse=='2':
       exit()
     else:
         print('Faites un choix correct')
         exit()
         
