"""on construit un decorateur qui va normalise les numéros de télépphones 
en ajoutant +237 sur chaque nombre et 6 où besoin se fait ressentir"""
def normalise(func):

    def num():
        x = func()
        k = len(x)
        for i in range (k):
            x[i] = "+2376"+x[i]

        return x
    return num
#On trie tout les numeros du fichier
@normalise
def ordre():
    table_numeros = []
    x = []
    Source = ""
    Source = open("data_exo_6.txt","r")
    table_numeros = Source.readlines()     #recupere les données de notre fichier
    Source.close()

    t = len(table_numeros)
    for i in range (t) :
       if table_numeros[i].startswith("+2376"):   #si le nombre commence par +2376 alors on ajoute dans x les chiffres qui suit
          x.append(int(table_numeros[i][5:]))

       elif table_numeros[i].startswith("2376"): #meme logique que le if precedent
          x.append(int(table_numeros[i][4:]))
       elif table_numeros[i].startswith("6"):
          x.append(int(table_numeros[i][1:]))
       else:
         x.append(int(table_numeros[i]))
    x.sort()
    """on peut avoir des nombres qui ne sont pas égal a 8 chiffres, on le complete avec des 0.
    On peut avoir des numéros en entier, on doit les transformés en chaine de caractères"""
    b = len(x)
    for i in range (b) :
        x[i] = str(x[i])
        if len(x[i])<8:     
            x[i] = "0"*(8-len(x[i]))+x[i]
    return x
table_numeros = ordre()
print(table_numeros)
