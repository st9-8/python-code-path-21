def decorateur(funct):
    def decore(text,g=False,i=False,b=False):
        result = funct(text)
                        
        if g == True and i==False and b==False:
            print ("*"+result+"*")

        elif i == True and g==False and b==False :
           print("_"+result+"_")

        elif b == True and g ==False and i==False:
            print("~"+result+"~")

        elif g == True and i == True and b== False:
            print("*_"+result+"_*")

        elif g == True and b == True and i == False:
            print("~*"+result+"*~")

        elif b == True and i == True and b == False:
            print("_~"+result+"~_")
            
        elif (g == True and i == True and b == True):
            print("*_~"+result+"~_*")
            
                
    return decore




@decorateur
def style(text, g=False, i=False, b=False):

    return text

style("Bonjour",g = True,i = True,b = True)



