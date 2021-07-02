import random
import array


def MotDePasse( taille_maximum):
    Nombre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lettres_miniscules = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                          'z']

    lettres_majuscules = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                          'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                          'Z']

    symboles = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']

    list_combinés = Nombre + lettres_majuscules + lettres_miniscules + symboles
    rand_Nombre = random.choice(Nombre)
    rand_lettres_miniscules = random.choice(lettres_miniscules)
    rand_lettre_majuscules = random.choice(lettres_majuscules)
    rand_symboles = random.choice(symboles)
    liste_random = rand_Nombre + rand_lettre_majuscules + rand_lettres_miniscules + rand_symboles

    for x in range(taille_maximum - 4):
        liste_random = liste_random + random.choice(list_combinés)
        liste_random_table = array.array('u', liste_random)
        random.shuffle(liste_random_table)
    mot_de_passe = ""
    for i in liste_random_table:
        mot_de_passe = mot_de_passe + i
    print(mot_de_passe)


def MotDePasse1(taille_maximum):
    Nombre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lettres_miniscules = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                          'z']

    lettres_majuscules = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                          'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                          'Z']

    symboles = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']


    list_combinés = Nombre + lettres_miniscules + symboles
    rand_Nombre = random.choice(Nombre)
    rand_lettres_miniscules = random.choice(lettres_miniscules)
    rand_lettre_majuscules = random.choice(lettres_majuscules)
    rand_symboles = random.choice(symboles)
    liste_random = rand_Nombre + rand_lettres_miniscules + rand_symboles

    for x in range(taille_maximum - 3):
        liste_random = liste_random + random.choice(list_combinés)
        liste_random_table = array.array('u', liste_random)
        random.shuffle(liste_random_table)
    mot_de_passe = ""
    for i in liste_random_table:
        mot_de_passe = mot_de_passe + i
    print(mot_de_passe)


def MotDePasse2(taille_maximum):
    Nombre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lettres_miniscules = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                          'z']

    lettres_majuscules = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                          'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                          'Z']

    symboles = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']


    list_combinés = lettres_majuscules + lettres_miniscules + symboles
    rand_Nombre = random.choice(Nombre)
    rand_lettres_miniscules = random.choice(lettres_miniscules)
    rand_lettre_majuscules = random.choice(lettres_majuscules)
    rand_symboles = random.choice(symboles)
    liste_random = rand_lettre_majuscules + rand_lettres_miniscules + rand_symboles

    for x in range(taille_maximum - 3):
        liste_random = liste_random + random.choice(list_combinés)
        liste_random_table = array.array('u', liste_random)
        random.shuffle(liste_random_table)
    mot_de_passe = ""
    for i in liste_random_table:
        mot_de_passe = mot_de_passe + i
    print(mot_de_passe)


choix_de_mot_de_passe = input("veuillez entrer un choix \n"
                              "1-mot de passe sans majuscule \n"
                              "2-mot de passe sans chiffre \n"
                              "3-mot de passe complet \n")
choix_de_taille = input("entrer la taille de votre mot de mot de passe \n")
choix_de_taille = int(choix_de_taille)
if choix_de_mot_de_passe == "1":
    print(MotDePasse1(choix_de_taille))
elif choix_de_mot_de_passe == "2":
    print(MotDePasse2(choix_de_taille))
elif choix_de_mot_de_passe == "3":
    print(MotDePasse(choix_de_taille))
else:
    pass
