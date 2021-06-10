def decorateur(fonction):
    """ cette fonction permet d'effectuer la mise en forme sur les numéros de téléphone \
    triés ie ajouter le prefixe +237 6 au numero xxxxxxxx puis met le resultat dans un fichier text"""
    
    def decore(liste):
        ma_liste = fonction(liste)
        # on effectue la mise en forme sur les numéros
        nouvel_liste = []
        for numero in ma_liste:
            nouvel_liste.append("+237 6"+numero)

        # ensuite on ecrit le resultat dans un fichier
    
        with open("data6.txt",'w') as fichier:
            for numero in nouvel_liste:
                fichier.write(numero + "\n")   
            
    return decore


@decorateur
def trier(liste):

    """ trie une liste de numéro de telephone contenant exactement 8 chiffres """
    
    ma_liste = []
    
    for numero in liste:                                      # pour  chaque numero dans la liste
        
        longueur = len(numero)
        
        if longueur >= 8:                                     # si la longueur est superieur à 8
           
            numero_reduit = ''
            
            for j in range(longueur-1,longueur-9,-1):          # on réduit le numéro en concervant uniquement les 8 derniers chiffres

                numero_reduit = numero[j] + numero_reduit
                
            ma_liste.append(numero_reduit)
            
        else:
            print("numéro invalide")                          # les numeros de longueur inferieur à 8 sont invalides
            
   
    return sorted(ma_liste)                                   # retoune la liste des numéro trier

   

# Dans le bloc qui suit, on recupere les donnees du fichier (les numeros de telephone qui sont le fichier) dans une liste puis on appelle la fonction trier avec

try:
    f = open("data_exo_6.txt", "r", encoding = "utf_8")
    fichier = f.read().split('\n')
    ma_liste = []
    for ligne in fichier:
        ma_liste.append(ligne)
    #print(ma_liste)
    f.close
except IOError:
    print("!!!!!!! fichier introuvable ")

trier(ma_liste)

 # lecture du fichier contenant les numéros triés et mis en forme
 
f = open("data6.txt","r", encoding = "utf_8")
print(f.read())
f.close



    
#trier = decorateur(trier)

#print(trier(["678954621","237691987564","+237691959698","76393936"]))
