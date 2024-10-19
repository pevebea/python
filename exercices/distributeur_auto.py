 
message1 = "1 Coca-cola : 1000 GNF"
message2 = "2 Jus d'orange : 1500 GNF"
message3 = "3 Eau : 500 GNF"
print(message1)
print(message2)
print(message3)

# Prix des marchandises
coca = 1000
orange = 1500
eau = 500

# Demander l'utilisateur
choix_utilisateur = int(input("faites votre choix, saisir 1, 2 ou 3: "))
montant = int(input("Veuiller saisir votre montant: "))

# Cas ou le montant est suffisant
if choix_utilisateur == 1 and montant >= coca:
    monaie = montant - coca
    print(f"vous povez recuperer votre boisson !!! La monaie est: {monaie} GNF")
elif choix_utilisateur == 2 and montant >= orange:
    monaie = montant - orange
    print(f"vous povez recuperer votre boisson !!! La monaie est: {monaie} GNF")
elif choix_utilisateur == 3 and montant >= eau:
    monaie = montant - eau
    print(f"vous povez recuperer votre boisson !!! La monaie est: {monaie} GNF")
# Cas ou le montant n'est passuffisant
elif choix_utilisateur == 1 and montant <= coca:
    rest_a_payer = coca - montant
    print(f"solde insuffisant !!! il vous reste : {rest_a_payer} GNF")
elif choix_utilisateur == 2 and montant <= orange:
    rest_a_payer = orange - montant
    print(f"solde insuffisant !!! il vous reste : {rest_a_payer} GNF")
elif choix_utilisateur == 3 and montant <= eau:
    rest_a_payer = eau - montant
    print(f"solde insuffisant !!! il vous reste : {rest_a_payer} GNF")
    
