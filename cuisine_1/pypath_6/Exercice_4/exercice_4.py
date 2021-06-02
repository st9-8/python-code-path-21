
def trait_text(func):##DECORATEUR
        def ego(text,g=False,i=False,b=False):
               if g==False and i==False and b==False:
                   return func(text,g=False,i=False,b=False)
               if g== True :
                    text= "*"+text+"*"

               if i==True:
                   text="_"+text+"_"

               if b==True:
                   text="~"+text+"~"


               return func(text,g=False,i=False,b=False)
        return ego
@trait_text
def style (text ,g=False,i=False,b=False):
    return text

print(style("bonjour",g=True,i=True,b=True))