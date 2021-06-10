import random   #on utilise random pour le choix aléatoire
words = [word.strip() for word in open("sowpods.txt", encoding="utf-8")] #on recupère les mots dans une liste en enlevant les espaces autour de ceux-ci avec Strip()
taille = len(words)    #on recupère la taille de notre liste
print("\n Nous avons ", taille, " mots")
word = random.choice(words)   #choix au hasard d'un mot
print("\n Le mot aléatoire est ", word)
