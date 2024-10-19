
# Signe du produit de deux nombre
x = int(input("entrez un premier nombre: "))
y = int(input("entrez un second nombre: "))

if (x > 0 and y > 0) or (x < 0 and y < 0):
    signe = "Positif"
elif x == 0 or y == 0:
    signe = "Null"
else:
    signe = "Negatif"

print(f"le produit de {x} et {y} est {signe}")
