# LES FONCTIONS 
""" 
    les fonctions lambda
    f = lambda x: 2*x + 3               # une variable
    g = lambda x, y: 2*x**2 + 3*y**4    # deux variable
    .....

"""
f = lambda x: 2*x + 3               # une variable
g = lambda x, y: 2*x**2 -  3*y**4    # deux variable

print(f"f(1) = {f(1)}")
print(f"g(1, 2) = {g(1, 2)}")

def somme(a, b, c):
    resultat = a + b + c
    print("Le resultat est ", resultat)

# somme(1, 2, 3)

def multiplier(x, y):
    return x * y

def diviser(a, b):
    if b != 0:
        return a / b