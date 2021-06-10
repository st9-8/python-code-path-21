def comprehension_liste(x,y,z,n):
    
    """ Manipulation des comprehension de liste sur les dimension d'un cuboide"""
    
    ma_liste = [[i,j,k] for i in range(x+1) for j in range(y+1)\
              for k in range(z+1) if i+j+k !=n]

    print(ma_liste)


print(comprehension_liste(1,1,2,3))  #test
