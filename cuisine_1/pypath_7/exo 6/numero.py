num_list = []
n = input("combien de numeros voulez vous saisir\n")
try:
    n = int(n)
except ValueError:
    false
for index in range(n):
    numero = input("veuillez saisir un numero\n")
    try:
        numero = int(numero)
    except ValueError:
        false
    if len(str(numero)) == 8:
        num_list.append("+2376"+ str(numero))
    elif len(str(numero)) == 9 :
        num_list.append("+237"+ str(numero))
    elif len(str(numero)) == 12:
        num_list.append("+"+ str(numero))
    else:
        print("veuillez saisir un numero correct")
        break
ordre = sorted(num_list)
with open("fic_numero.txt", "w") as f:
    for index in ordre:
        sorted(ordre)
        f.write("%s\n" % index)
    f.close()
