import random

reponse = input("veuillez entrer un nombre entre 0 a 1000 \n")
reponse = int(reponse)
nbr_fois = 0
nbr_supposition = 0
var1 = 0
choix_ordinateur = random.randint(0, 1000)
print(choix_ordinateur)
if choix_ordinateur < 500 and reponse < 500:
    print("reponse trop petite")
    for number in range(0, 500):
        choix_ordinateur = choix_ordinateur + 1
        nbr_supposition = nbr_supposition + 1
        if choix_ordinateur == reponse:
            var1 = nbr_supposition + 1
    print(var1)
    print(choix_ordinateur)
elif choix_ordinateur < reponse and reponse > 500:
    print("reponse trop petite")
    for number in range(choix_ordinateur, reponse):
        choix_ordinateur = choix_ordinateur + 1
        nbr_supposition = nbr_supposition + 1
        if choix_ordinateur == reponse:
            var1 = nbr_supposition + 1
    print(var1)
    print(choix_ordinateur)


elif choix_ordinateur > reponse and reponse < 500:
    print("reponse trop élévé")
    for number in range(reponse, choix_ordinateur, -1):
        choix_ordinateur = choix_ordinateur - 1
        nbr_supposition = nbr_supposition + 1
        if choix_ordinateur == reponse:
            var1 = nbr_supposition + 1
    print(var1)
    print(choix_ordinateur)
elif choix_ordinateur > reponse > 500:
    print("reponse trop élévé")
    for number in range(500, 1000):
        choix_ordinateur = choix_ordinateur + 1
        nbr_supposition = nbr_supposition + 1
        if choix_ordinateur == reponse:
            var1 = nbr_supposition + 1
    print(var1)
    print(choix_ordinateur)
else:
    print("reponse non trouvé:")
