# ordre alphabetique des noms

nom_1 = input("Entrer un nom: ")
nom_2 = input("Entrer un nom: ")
nom_3 = input("Entrer un nom: ")

if nom_1 < nom_2 and nom_2 < nom_3:
    print(f"les noms {nom_1}, {nom_2} et {nom_3} sont dans l'ordre alphabetique")
else:
    print(f"les noms {nom_1}, {nom_2} et {nom_3} ne sont pas dans l'ordre alphabetique")

