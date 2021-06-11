import os, platform


def str_to_list(l=""):
    """Permet de transformer une chaine de caractere en une liste"""
    liste = []
    for el in l:
        liste.append(el)
    return liste


def list_to_str(liste=[]):
    """Permet de transformer une liste en une chaine de caractere"""
    mot = ""
    for el in liste:
        mot = mot + el
    return mot

def clear():
    """Cette fonction efface la console"""
    
    if platform.system() == "Linux":
        os.system('clear')
    if platform.system() == "Windows":
        os.system('cls')