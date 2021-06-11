#fonctions exercice4


def file_to_list(file = "data_exo_6.txt"):
    "Fonction pour mettre les numeros du fichier dans une liste"

    numero = []
    with open(file, 'r') as numFile:
        #numFile.seek(1)
        lines = numFile.readlines()
        for line in lines:
            numero.append(line)

    return numero

def list_to_file(liste=[]):
    "Fonction pour mettre les numeros de la liste dans un fichier"
    
    with open("data_exo_6_new.txt","w+") as file:
        for el in liste:
            file.write(el)


def deco_standard(trier_numero):
    "Fonction decoratrice pour standardiser les numeros"
    def stand(numListe = []):
        
        for i in range(0,len(numListe)):
            if len(numListe[i])==14:
                numListe[i] = numListe[i]

            elif len(numListe[i])==13:
                numListe[i] = '+' + numListe[i]

            elif len(numListe[i])==10:
                numListe[i] = '+237' + numListe[i]

            elif len(numListe[i])==9:
                numListe[i]= '+2376'+ numListe[i]

        return numListe

    return stand



@deco_standard
def trier_numero(numListe):
    
    "Fonction pour trier les numeros"
    
    new_numListe = numListe.sort()
    
    return new_numListe


def finalisation(liste):
    "Fonction pour quitter de +237697138574 a +237 697138574 "
    t = ''
    new_l = ''
    new_liste = []
    for l in liste:
        if len(l) < 14:
            pass
        else:
            t = l[4:]
            new_l = '+237'+' '+t
            new_liste.append(new_l)
    
    return new_liste


