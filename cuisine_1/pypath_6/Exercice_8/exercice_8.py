
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet1=[]
for i in range(len(alphabet)):
    alphabet1.append(alphabet[i])
for i in range(len(alphabet1)):
    alphabet1.append(alphabet1[i])
######Ma fonction encrypte et decrypte en fonction du decalage
def encryptage():
  message=input("Entrer votre message\n")
  decale=input("Entrer le decalage, on notera - signifie vers la gauche et positif pour la droite")
  try:
      decale=int(decale)
  except:
       pass

  def coder(lettre,alphabet1,decale):
    for i in range(len(alphabet1)):
        if lettre==" ":
            return " "
        elif alphabet[i]== lettre:
            return str(alphabet1[i+decale])
    return "?"
  message_coder=str()
  for lettre in message:
    message_coder+=coder(lettre,alphabet1,decale)
  print(message_coder)



encryptage()