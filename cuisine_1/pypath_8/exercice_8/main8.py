from f_usuelles import *

class Lettre:

    def __init__(self, valeur_reelle, valeur_crypte):
        self.valeur_reelle = valeur_reelle
        self.valeur_crypte = valeur_crypte

    def afficher(self):
        print('{} -> {}'.format(self.valeur_reelle, self.valeur_crypte))

    
class Alphabet:

    def __init__(self):
        self.lettre = []

    def afficher(self):
        for lettre in self.lettre:
            lettre.afficher()
            
def init():
    "Fonction qui permet de creer les objets lettres avec les deux alphabets clair et crypte"
    
    clair = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    crypte = ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']

    alphabet = Alphabet()
    for i in range(0, len(clair)):
        for j in range(0, len(crypte)):
            if i==j:
                lettre = Lettre(valeur_reelle=clair[i], valeur_crypte=crypte[j]) 
                alphabet.lettre.append(lettre)
            else:
                pass
    return alphabet.lettre


def encoder(text = ""):
    """Encodage utilisant le chiffrement de Cesar"""

    alphabet = init()
    
    new = str_to_list(text.upper())

    for k in range(0,len(new)):
        for l in alphabet:
            if new[k] == l.valeur_reelle:
                new[k] = l.valeur_crypte
                break
            
    return list_to_str(new)


def decoder(text = ""):
    """Decodage utilisant le chiffrement de Cesar"""

    alphabet = init()
    
    new = str_to_list(text.upper())

    for k in range(0,len(new)):
        for l in alphabet:
            if new[k] == l.valeur_crypte:
                new[k] = l.valeur_reelle
                break
            
    return list_to_str(new)

def menu():

    """Cette fonction affiche le menu"""
    
    print( 
          """ \033[36;2;132;220;51;1;48;2m
                             MENU: Chiffrement de Cesar*

    Vous pouvez encoder ou decoder un texte
            1- Encoder
            2- Decoder
            
          \033[00m""")
    