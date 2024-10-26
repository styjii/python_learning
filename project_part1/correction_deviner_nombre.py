from random import randint

# Numbre mister
number_to_find = randint(0, 100)

# Trial times
remaining_attemps = 5

while remaining_attemps > 0 :
    print(f"Il reste {remaining_attemps} essai{'s' if remaining_attemps > 1 else ''}")
    user_choice = input("Deviner le nombre : ")
    if not user_choice.isdigit() :
        print("Veuillez entrer un nombre")
        continue
    
    user_choice = int(user_choice)
    
    if number_to_find > user_choice : # plus grand
        print(f"Le nombre mistere est plus grand que {user_choice}")
    elif number_to_find < user_choice : # plus petit
        print(f"Le nombre mistere est plus petit que {user_choice}")
    else : # egale
        break
        
    remaining_attemps -= 1
    
# Gagner ou perdue
if remaining_attemps == 0 :
    print(f"Domage ! Le nombre mistere etait {number_to_find}")
else :
    print(f"Bravo ! Le nombre mistere etait bien {number_to_find}")
    print(f"Tu as trouver le nombre en {6 - remaining_attemps} essai{'' if 6 - remaining_attemps == 1 else 's'}")

print("Fin du jeux.")