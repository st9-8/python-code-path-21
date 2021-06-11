#main exercice8

import main8, time

main8.menu()

text = input("Entrer votre texte: ")
print("\n")
choix = input("Que voulez vous faire de votre texte? \n")
choix = int(choix)

while choix not in [1,2]:
    print("Entrez un choix valide ")
    choix = input("Que voulez vous faire de votre texte? \n")
    choix = int(choix)

if choix == 1:
    time.sleep(1)
    print( 
          """ \033[33;2;132;220;51;1;48;2m
          {} encode est -> {}
          \033[00m""".format(text,main8.encoder(text)))
   
elif choix == 2:
    time.sleep(1)
    print( 
          """ \033[33;2;132;220;51;1;48;2m
          {} decode est -> {}
          \033[00m""".format(text, main8.decoder(text)))

   


    
    
