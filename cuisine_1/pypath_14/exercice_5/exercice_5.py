
def cuboide(x,y,z,n):

    """
        cette fonction permet de representet tout les points de i , j et k  dans la base x,y et
        z tels que i+j+k   soit different de n

    """

    coordonnes = [[i,j,k] for i in range(x+1) for j in  range(y+1) for k in range(z+1) if i+j+k != n]
    
    return coordonnes



print(cuboide(1,1,2,3))