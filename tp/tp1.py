# TP 1: Deviner le nombre
import random

nombre_mister = random.randint(0, 100)
essai_restant  = 10 # nombre de tentatives de l'utilisateur

while essai_restant > 0:
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



