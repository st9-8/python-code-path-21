import random,os

def ch_word():##choisi un nombre au hasard dans le fichier
    fichier=open("SOWPODS.txt","r")
    c = fichier.readlines()
    fichier.close()
    return random.choice(c)

def deviner():#fonction deviner un nombre
    word = ch_word()
    found = ["_" for i in range(len(word)-1)]#initialisation de la liste de "-"
    n = 6
    print("Bievenue sur le jeu du Pendu!\n")
    print("Les lettres doivent etre entree en majuscule dans le cas contraire elles seront compter comme fausse")

    while n != 0:
        letter = input("deviner votre lettre:\t")
        if letter in word and len(letter) == 1:
            pos = [i for i in range(len(word)) if letter == word[i]]#liste des positions d'un mot
            for j in range(len(pos)):
                found[pos[j]] = letter #met la lettre a la position j dans found
        else:
            n -= 1
            print("Incorrect!, -", n, "tentatives!")

        print(" ".join(found)) #join la liste found en une chaine de charactere
        if "_" not in found : #s'il n'ya plus de tiret dans la chaine alors tout es mot ont ete decouvert
            print("Vous avez devine le mot! ")
            try_again()
        elif n==0: # n est egal a zero alors nombres de chance ecoulee
            print("Nombre de tentatives ecoulees")
            print("le mot etait ",word)
            try_again()

def try_again():
    ans = "p"
    while ans != "o" and ans != "O" and ans != "n" and ans != "N":
        ans = input("Voulez-vous reessayer? 1:oui 2:non\t\t")
        if ans == "1" :
            os.system("clear")
            deviner()
        elif ans == "2":
            print("Thank you!")

        else:
            ans= input ("entrer 1 ou 2")

deviner()



