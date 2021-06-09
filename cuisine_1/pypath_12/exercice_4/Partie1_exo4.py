
def choixmot():
    with open("sowpods.txt")as f:
        lines=csv.reader(f,delimiter=',')
        liste=list(lines)
        hasard = random.randint(0,len(liste)-1)
        motchoisi = liste[hasard]
        f.close() 
        print ("\n Un mot a été choisi parmi la base de donnée\n")
    return motchoisi


                         
