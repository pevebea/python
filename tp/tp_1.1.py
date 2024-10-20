# niveau 1 facile 10 essai
# niveau 2 moyen 5 essai
# niveau 3 difficile 3 essai
# si score = 0 afficher vous avez perdu
# demande si le joueur veut continer ou quitter

# TP 1: Deviner le nombre
import random
continuer = True

while not continuer:
    print("Bienvenu dans le jeu du devinette:\n1.Facile\n2.Moyen\n3.Difficile")
    choix_utilisateur = int(input("choisir le niveau: "))
    if choix_utilisateur == 1:
        essai_restant = 10
    elif choix_utilisateur == 2:
        essai_restant = 5
    elif choix_utilisateur == 3:
        essai_restant = 3

    player_number = int(input("Deviner le nombre entre (1 et 100): "))

    if nombre_mister > player_number:
        print("plus grand !")
    elif nombre_mister < player_number:
        print(f"plus petit !")
    else:
        print("FELICITATION, VOUS AVEZ TROUVER LE NOMBRE A DEVINER !!!")
        exit() # stopper le programme si le mombre est trouver
    
    essai_restant -= 1  # essai_restant = essai_restant - 1
    print(f"il vous reste {essai_restant} tentatives")

    if essai_restant == 0:
        print("Game over Vous avez perdu !!!")
    
    print("Voulez vous continuer ?\nAppuer sur n'importe quelle touche pour quitter ou y pour continuer")
    choix_utilisateur = input("taper y / n: ")
    if choix_utilisateur == "y":
        continuer = True

    
    



