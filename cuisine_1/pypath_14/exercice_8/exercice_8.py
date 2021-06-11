"""
encodage et  decodage cesar  

on vas remplacer chaque caractere par de l'aphabet normal par  celui de l'alphabet cesar
Alphabet en clair: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet cypher: XYZABCDEFGHIJKLMNOPQRSTUVW

"""
 
import  string 
 

alphabet = list(string.ascii_lowercase) #on recupere les lettres de l'aphabet
decalage = alphabet[-3:]+alphabet[:23]#on construit une nouvelle liste commencant par les 3  derniers caractère 
#print(decalage)



#print(dico_alphabet)
#print(dico_cesar)

def encodage(texte , decalage):
    if decalage <=26 :
        clair = list(string.ascii_lowercase) #on recupere les lettres de l'aphabet
        cypher = clair[-decalage:]+clair[:26-decalage] 
    
        dico_alphabet = {clair[i]:cypher[i] for i  in range(len(clair)) }
        crypto = ''
        for i in texte.lower() : 

            if i in dico_alphabet.keys(): 
                crypto += dico_alphabet[i]

            else : 
                crypto +=i 

        return crypto
    else:
        print("decalage trop grand")


def decodage(texte , decalage): 
    if decalage <=26 :
        clair = list(string.ascii_lowercase) #on recupere les lettres de l'aphabet
        cypher = clair[-decalage:]+clair[:26-decalage] 
        dico_cesar = {cypher[i]:clair[i] for i in range(len(clair))}

        decrypto = ''
        for i in texte.lower(): 
            if i in dico_cesar.keys(): 
                decrypto += dico_cesar[i]

            else : 
                decrypto +=i 
        return decrypto
    else :
        print("decalage trop grand")

print(encodage('THE QUICK, BROWN FOX JUMPS OVER THE LAZY DOG',4))
print(decodage(encodage('THE, QUICK BROWN FOX JUMPS OVER THE LAZY DOG',4),4))
print(decodage('qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald',40))

        






    