
#--------------------------------------------- Decorateur -------------------------------------------------#
def decorateur(fonction):
    def ma_fonction(liste):
        listeTemporaire = []
        for element in liste: 
            element = list(element) 
            if element[0] == "+" and element[1] == "2" and element[2] == "3" and element[3] == "7":  
                pass
            else:  
                if element[0] == "2" and element[1] == "3" and element[2] == "7":  
                    element.insert(0,"+")
                elif element[0] == "6" ""and len(element) == 9:
                    element.insert(0,"7")
                    element.insert(0,"3")
                    element.insert(0,"2")
                    element.insert(0,"+")
                else:  
                    element.insert(0,"6")
                    element.insert(0,"7")
                    element.insert(0,"3")
                    element.insert(0,"2")
                    element.insert(0,"+")
            element = ''.join(element)
            listeTemporaire.append(element)
            liste = listeTemporaire
            liste.sort()
        print(liste)
            
    return ma_fonction
#---------------------------------------------------------------------------------------------------------#
@decorateur
def trierContacts(liste): #Fonction
    liste.sort() 

#--------------------------------------------- Lecture du fichier -------------------------------------------------#
with open("data_exo_6.txt","r") as fichier:  
    liste = fichier.readlines()
    listeTemporaire = []
    for element in liste:
        listeTemporaire.append(element.strip("\n"))
    liste = listeTemporaire
    nombreContacts = liste[0]   
    liste.remove(nombreContacts)
 

trierContacts(liste)


    