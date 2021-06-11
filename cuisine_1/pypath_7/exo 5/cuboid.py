X = int(input("entrez la valeur de x\n"))
Y = int(input("entrez la valeur de y\n"))
Z = int(input("entrez la valeur de z\n"))
N = int(input("entrez la valeur de n\n"))
ans = [[i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i+j+k !=N]
print(ans)
