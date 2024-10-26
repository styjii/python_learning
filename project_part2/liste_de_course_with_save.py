import sys, os, json

OPTIONS = ["1", "2", "3", "4", "5"]
MENU = f"Choisissez parmi les {len(OPTIONS)} options suivantes\n1: Ajouter un élément à la liste\n2: Retirer un élément de la liste\n3: Afficher la liste\n4: Vider la liste\n5: Quitter\n👉 Votre choix : "

file_path = os.path.dirname(__file__)
file_path = os.path.join(file_path, "liste.json")

if os.path.exists(file_path) :
    with open(file_path, "r") as f :
        LISTES = json.load(f)
else :
    LISTES = []

while True :
    # Choix de l'utilisateur
    user_choice = input(MENU)
    # Quand l'utilisateur entre autre choix
    while user_choice not in OPTIONS :
        user_choice = input(MENU)

    # Ajouter un élément à la liste
    if user_choice == "1" :
        ajouter = input("Entrez le nom d'un élement à ajouter à la liste de courses : ")
        LISTES.append(ajouter)
        print(f"L'élément {ajouter} à bien été ajouter à la liste")
    # Retirer un élément de la liste
    if user_choice == "2" :
        retirer = input("Entrez le nom d'un élement à retirer de la liste de courses : ")
        if retirer in LISTES :
            LISTES.remove(retirer)
            print(f"L'élément {retirer} à bien été supprimé de la liste")
        else :
            print(f"L'élément {retirer} n'est pas dans la liste.")
    # Afficher la liste
    if user_choice == "3" :
        if len(LISTES) > 0 :
            print("Voici le contenu de votre liste :")
            for i in range(len(LISTES)) :
                print(f"{i+1}. {LISTES[i]}")
        else :
            print("Votre Liste ne contient aucun élément.")
    # Vider la liste
    if user_choice == "4" :
        LISTES.clear()
        print("La liste à été vidée de son contenu.")
    # Quitter et sauver
    if user_choice == "5" :
        with open(file_path, "w") as f:
            json.dump(LISTES, f, indent=4)
        print("A Bientôt !")
        sys.exit()
    print("-" * 50)