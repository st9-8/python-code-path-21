import random,os,platform

def clean():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('clear')

def ch_word():##choisi un nombre au hasard dans le fichier
    fichier=open("SOWPODS.txt","r")
    c = fichier.readlines()
    fichier.close()
    return random.choice(c)

def deviner():#fonction deviner un nombre
    word = ch_word()
    print(word)
    word1=word.lower()
    found = ["_" for i in range(len(word)-1)]#initialisation de la liste de "-"
    n = 6
    print("Bievenue sur le jeu du Pendu!\n")
    print("_".join(found))


    while n != 0:
      letter = input("deviner votre lettre:\t")
      if (letter in word or letter in word.lower()) and len(letter) == 1:
            pos = [i for i in range(len(word)) if (letter == word[i]) or (letter == word1[i]) ]#liste des positions d'un mot
            for j in range(len(pos)):
              letter = letter.upper()
              found[pos[j]] = letter #met la lettre a la position j dans found
      else:
            n -= 1
            print("Incorrect!, -", n, "tentatives!")

      print(" ".join(found)) #join la liste found en une chaine de charactere
      if "_" not in found :#s'il n'ya plus de tiret dans la chaine alors toutes les lettres ont ete decouvert
            n=0
            print("Vous avez devine le mot! ")
            try_again()
      elif n==0: # n est egal a zero alors nombres de chance ecoulee
            print("Nombre de tentatives ecoulees")
            print("le mot etait ",word)
            try_again()

def try_again():
    ans = "p"
    while ans != "1"  and  ans != "2":
        ans = input("Voulez-vous reessayer? 1:oui 2:non\t\t")
        if ans == "1" :
            clean()
            deviner()
        elif ans == "2":
            print("Thank you!")

        else:
            ans= input("entrer 1 ou 2")

deviner()



