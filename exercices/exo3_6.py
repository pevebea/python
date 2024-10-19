# category dun enfant

age = int(input("Saisir l'age de l'enfant: "))

if age >= 12:
    category = "Cadet"
elif age >= 10:
    category = "Mimine"
elif age >= 8:
    category = "Pupille"
elif age >= 6:
    category = "Poussin"

else:
    category = "Inconnu"

print(f"Cet enfant est: {category}")