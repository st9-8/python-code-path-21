import  random

with open('sowpods.txt') as f:
    words = list(f)
print(random.choice(words).strip())