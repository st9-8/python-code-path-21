# definissons un decorateur qui va ajouter +237 sur chaque nombre
def ajouter(func):
    def egal():
        article = func()
        for i in range(1, len(article)):
            article[i] = "+2376" + article[i]

        return article

    return egal


# maitenant creons une fonction qui trie tout les numeros du fichier
@ajouter
def trie():
    a = []
    tableau = []  # ce tableau contiendra notre numero complet
    fichier = open("article_exo_7.txt", "r")
    a = fichier.readlines()  # recupere toute les lignes du fichier

    fichier.close()

    for i in range(len(a)):
        if a[i].startswith("+2376"):  # si le nombre commence par +2376 alors on ajoute dans tableau les chiffres qui suit
            tableau.append(int(a[i][5:]))

        elif a[i].startswith("237"):
            tableau.append(int(a[i][4:]))
        elif a[i].startswith("6"):
            tableau.append(int(a[i][1:]))
        else:
            tableau.append(int(a[i]))
    tableau.sort()
    for i in range(1, len(tableau)):
        tableau[i] = str(tableau[i])
        if len(tableau[i]) < 8:  # si apres transformation le nombre n'est pas egal a 8 on le complete avec 0
            tableau[i] = "0" * (8 - len(tableau[i])) + tableau[i]
    return tableau


a = trie()
print(a)
