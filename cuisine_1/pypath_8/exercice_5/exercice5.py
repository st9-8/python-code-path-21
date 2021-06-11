from main5 import *

print("""
*MENU CUBOIDE*
""")

x = input("Entez x ")
y = input("Entez y ")
z = input("Entez z ")
n = input("Entez n ")

print( 
          """ \033[36;2;132;220;51;1;48;2m
          Le cuboide obtenu est -> {}
          \033[00m""".format(cuboide(int(x),int(y),int(z),int(n))))