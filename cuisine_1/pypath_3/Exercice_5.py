print("Entrez les valeurs a generer les listes ")
A = int(input(">>> Entrez A: "))
B = int(input(">>> Entrez B: "))
C = int(input(">>> Entrez C: "))
N = int(input(">>> Entrez N: "))

listeGenerateur = [[a,b,c] for a in range(A+1) for b in range(B+1) for c in range(C+1) if a+b+c != N]
print(">>> ",listeGenerateur)

