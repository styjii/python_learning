from random import randint

# Les vies inititales
PLAYER_HEART = ENEMY_HEART = 50
# nombre initial de portions
NUMBER_OF_POTIONS = 3

while PLAYER_HEART >= 0 and ENEMY_HEART >= 0 :
    user_choice = ""
    while user_choice not in ["1", "2"] : # choix de l'utilisateur
        user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    # potion
    potions = randint(15, 50)
    # les point d'attaques
    player_attack, enemy_attack = randint(5, 10), randint(5, 15)

    if user_choice == "1" : # S'il veux attaquer
        ENEMY_HEART -= player_attack
        PLAYER_HEART -= enemy_attack
        
        print(f"Vous avez inflige {player_attack} points de degats a l'ennemi")
        print(f"L'ennemi vous a inflige {enemy_attack} points de degats")
    else : # S'il veux ajouter du portions
        if NUMBER_OF_POTIONS == 0 :
            print("Vous n'avez plus de portions...")
        else :
            NUMBER_OF_POTIONS -= 1
            PLAYER_HEART += potions
            PLAYER_HEART -= enemy_attack
            
            print(f"Vous recuperez {potions} points de vie ({NUMBER_OF_POTIONS} restante{'s' if NUMBER_OF_POTIONS > 1 else ''})")
            print(f"L'ennemi vous a inflige {enemy_attack} points de degats")
            # indication de leurs vie
            if PLAYER_HEART >= 0 and ENEMY_HEART >= 0 :
                print(f"Il vous reste {PLAYER_HEART} points de vie.")
                print(f"Il reste {ENEMY_HEART} points de vie a l'ennemi.")
                print("-" * 50)
            
            # passer du tours
            PLAYER_HEART -= enemy_attack
            print("Vous passez votre tour...")
            print(f"L'ennemi vous a inflige {enemy_attack} points de degats")
    
    if PLAYER_HEART >= 0 and ENEMY_HEART >= 0 : # indication de leurs vie
        print(f"Il vous reste {PLAYER_HEART} points de vie.")
        print(f"Il reste {ENEMY_HEART} points de vie a l'ennemi.")
        print("-" * 50)
    
# perdue ou gagner
if PLAYER_HEART > ENEMY_HEART :
    print("Tu as gagne")
else :
    print("Tu as perdue")

print("Fin de partie")