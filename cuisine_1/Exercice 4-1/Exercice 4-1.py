def decorateur(funct):
    ''' decoateur qui permettra d'encardre un text selon sa mise en forme'''
    
    def decore(text,g=False,i=False,b=False):
                                      
        if g == True :
            text = "*"+text+"*"

        if i == True :
           text = "_"+text+"_"

        if b == True:
             text = "~"+text+"~"
             
        return funct(text)

                         
    return decore




@decorateur
def style(text, g=False, i=False, b=False):

    return text

print(style("Bonjour", g  = True, i = True, b = True))



