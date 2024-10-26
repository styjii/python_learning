from pprint import pprint
import random


MENU = "Trouvez le nombre mistère.\n👉 "

# nombre d'essai
essai = 5

# nombre aleatoire
nombre_mystere = random.randint(0, 100)

# si le nombre d'essai est supérieur à 0
while essai > 0 :
    print(f"Il reste {essai} essai{'s' if essai > 1 else ''}.")
    essai -= 1
    # entrer par l'utilisateur
    user = input(MENU)
    # si l'utilisateur entre n'importe quoi
    while not user.isdigit() :
        print("Veuillez entre un nombre !")
        user = input(MENU)

    if nombre_mystere > int(user) :
        print("Votre nombre plus petit.")
    elif nombre_mystere < int(user) :
        print("Votre nombre est plus grand")
    else :
        break

    print("-" * 50)

# Si l'utilisateur trouve le bon nombre
if int(user) == nombre_mystere :
    print(f"Vous avez gagne en {5 - essai} essai{'s' if (5 - essai) > 1 else ''}")
else :
    print(f"Vous avez perdu. Le nombre mystère est {nombre_mystere}")