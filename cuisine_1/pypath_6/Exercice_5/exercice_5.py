def exo5(x,y,z,n):
    a=[i for i in range(x+1)]# definition de la liste des elements de x
    b=[i for i in range(y+1)]#definition de la liste des elements de y
    c=[i for i in range(z+1)]#definition de la liste des elements de z
    k=[[i,j,k] for i in a for j in b for k in c if i+j+k <=n]
    print(k)
exo5(1,1,2,3)