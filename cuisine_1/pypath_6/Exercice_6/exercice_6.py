#decorateur qui va ajouter +237 sur chaque nombre
def ajout(func):

    def ego():
        data = func()
        for i in range(1, len(data)):
            data[i] = "+2376"+data[i]

        return data
    return ego
#fonction qui trie tout les numeros du fichier
@ajout
def trier():
    c = []
    data = []
    fichier=open("data_exo_6.txt","r")
    c = fichier.readlines()#recupere toute les lignes du fichier

    fichier.close()

    for i in range(len(c)):
       if c[i].startswith("+2376"):#si le nombre commence par +2376 alors on ajoute dans data les chiffres qui suit
          data.append(int(c[i][4:]))

       elif c[i].startswith("2376"):#meme logique que le if precedent
          data.append(int(c[i][3:]))
       elif c[i].startswith("6"):
          data.append(int(c[i][1:]))
       else:
         data.append(int(c[i]))
    data.sort()
    for i in range(1, len(data)):
        data[i] = str(data[i])
        if len(data[i])<8:#si apres transformation le nombre n'est pas egal a 8 on le complete avec 0
            data[i] ="0"*(8-len(data[i]))+data[i]
    return data
c=trier()
print(c)
