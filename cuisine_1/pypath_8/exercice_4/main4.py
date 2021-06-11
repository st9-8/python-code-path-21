#fonctions de l'exercie 4

def deco_style(style):
    "Fonction decoratrice de la fonction style"

    def appliquer(text, g=False, i=False, b=False):
        if g == True and i == True:
            text = '_'+'*'+text+'*'+'_'
        if g == True and b == True:
             text = '~'+'*'+text+'*'+'~'
        if i == True and b == True:
             text = '~'+'_'+text+'_'+'~'
        if i == True and b == True and g==True:
             text = '*'+'~'+'_'+text+'_'+'~'+'*'
        elif i==b== False and g == True:
            text = '*'+text+'*'
        elif g==b== False and i == True:
            text = '_'+text+'_'
        elif g==i==False and b == True:
            text = '~'+text+'~'

        else:
            text = text
        return style(text, g=False, i=False, b=False)
    return appliquer

@deco_style
def style(text, g=False, i=False, b=False):
    return text

