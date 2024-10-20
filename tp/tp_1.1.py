

# niveau 1 facile 10 essai
# niveau 2 moyen 5 essai
# niveau 3 difficile 3 essai
# si score = 0 afficher vous avez perdu
# demande si le joueur veut continer ou quitter

# TP 1: Deviner le nombre
import random
continuer = True

while continuer:
  print("\nBienvenu dans le jeu 'DEVINE LE NOMBRE'")
  print("Difficultes:")
  print("1. Niveau facile 10 essais")
  print("2. Niveau moyen 5 essais")
  print("3. Niveau Difficile 3 essais")
  print("4. Niveau expert 1 essais")

  choix_niveau = int(input("taper 1, 2, 3 ou 4: "))
  if choix_niveau == 1:
    essai_restant = 10
  elif choix_niveau == 2:
    essai_restant = 5
  elif choix_niveau == 3:
    essai_restant = 3
  elif choix_niveau == 4:
    essai_restant = 1
  else:
    essai_restant = 0


  nombre_mister = random.randint(0, 100)
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
      if essai_restant == 0:
        print(f"Partie terminee, vous avez perdu, le nombre mistere etait {nombre_mister}")

    

  rejouer = input("voulez vous rejouer ou quiter? taper q/r")
  if rejouer == "q":
    continuer = False




