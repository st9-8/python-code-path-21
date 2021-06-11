def pretty_printing(fonction):
    """
        ce decorateur permert de mettre le  texte en gras en italique et barre
    """

    def inner(text,g=False,i=False,b=False):
        deco=""
        if g:
            deco += "*"
        if i :
            deco += "_"
        if b :
            deco += "~"
        deco =  text.join([deco, deco[::-1]])
        print(deco)


       

    return inner


@pretty_printing
def style(text ,g=False, i=False, b=False):
    return text

style("python", i=True,g=True,b=True)

