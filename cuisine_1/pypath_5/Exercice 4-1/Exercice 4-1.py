def decorateur(funct):
    ''' decorateur qui permettra d'encardrer un text selon sa mise en forme'''
    
    def decore(text,g=False,i=False,b=False):

        # en fonction de la mise en forme, on encardre le texte par le symbole correspondant 
                                      
        if g == True :
            text = "*"+text+"*"

        if i == True :
           text = "_"+text+"_"

        if b == True:
             text = "~"+text+"~"
             
        return funct(text)          

                         
    return decore


# on applique le décorateur à notre fonction

@decorateur
def style(text, g=False, i=False, b=False):

    return text

# test
print(style("Bonjour", g  = True, i = True, b = True))
print(style("SEED", i= True, g  = True) )
print(style("path python", b = True))



