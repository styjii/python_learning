import sys, random

# Etape 1 : nombre aleatoire entre 0 et 100
nombre_aleatoire = random.randint(0, 101)

# Etape 2 : Le joeur dispose 5 essais
nombre_d_essais, essais = 5, 0

menu = """ Il reste {essais} essais
Deviner le nombre : """

print("*** Le jeux de nombre mistere ***")
while True :
    nombre_utilisateur = ""
    while nombre_utilisateur != nombre_aleatoire :
        nombre_utilisateur = input(menu.format(essais = nombre_d_essais))
        # Etape 3 : Indication
        while not nombre_utilisateur.isdigit() :
            print("Veullez entrez une nombre")
            nombre_utilisateur = input(menu.format(essais = nombre_d_essais))
        if int(nombre_utilisateur) < nombre_aleatoire :
            print(f"Le nombre mistere est plus grand que {nombre_utilisateur}")
        elif int(nombre_utilisateur) > nombre_aleatoire :
            print(f"Le nombre mistere est plus petit que {nombre_utilisateur}")
        else :
            print(f"Bravo ! Le nombre mistere etait bien {nombre_aleatoire}\nTu as trouver le nombre en {essais} essai")
            print("Fin du jeux.")
            sys.exit()
            
        # Etape 4 : nombre d'essais par l'utilisateur 
        if nombre_d_essais == 1 :
            print(f"Domage ! Le nombre mistere etait {nombre_aleatoire}")
            print("Fin du jeux.")
            sys.exit()
        else :    
            nombre_d_essais -= 1
            essais += 1