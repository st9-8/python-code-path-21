def pretty_printing(fonction):

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
    print(text)


style("leandra", i=True,g=True,b=True)

