# reducteur de prix
# Ecreire un programme qui doit reduire le prix 
# d'un produit de 10% si le montant superieur à 50000
# sinon pas de reduction

# Recuperer le prix de l'utilisateur
price = input("Veillez saisir le prix à payer: ")
# Convertir le prix en nombre
# prix_convertie = float(price)
prix_convertie = int(price)
print(f"vous avez saisi {prix_convertie}")

if prix_convertie >= 50000:
    prix_convertie = prix_convertie - prix_convertie * .10

print(f"le prix reduit est {prix_convertie}")
