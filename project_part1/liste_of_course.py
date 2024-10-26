import sys

# Les variables
LISTE = []
MENU = """Choisir parmi les 5 options suivantes :
1:  Ajouter  un élément à la  liste de  courses
2:  Retirer  un élément de la  liste de  courses
3:  Afficher  les éléments de  la liste  de  courses
4:  Vider  la liste  de  courses
5:  Quitter  le programme
👉 Votre choix : """
MENU_CHOICE = ["1", "2", "3", "4", "5"]

while True :
    user_choice = ""
    while user_choice not in MENU_CHOICE :
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICE :
            print("Veuillez choisir une option valide...")
    
    # premier choix : ajout element
    if user_choice == MENU_CHOICE[0] :
        # demander à l'utilisateur l'élément à ajouter
        add_liste = input("Entrer le nom d'un élément à ajouter à la liste de courses : ")
        # ajout à la liste
        LISTE.append(add_liste)
        print(f"L'élement {add_liste} à été bien ajouté à la liste")
    # deuxième choix : retirer element
    elif user_choice == MENU_CHOICE[1] :
        # demander à l'utilisateur l'élément à supprimer
        rm_liste = input("Entrer le nom d'un élément à retirer de la liste course : ")
        # supprime à la liste s'il existe à la liste
        if rm_liste in LISTE :
            LISTE.remove(rm_liste)
            print(f"L'élément {rm_liste} à été bien retirer de la liste")
        else :
            print(f"L'élément {rm_liste} n'est pas dans la liste")
    # troisieme choix : affiche menu
    elif user_choice == MENU_CHOICE[2] :
        # afficher à l'utilisateur tous les contenu dans la liste
        print("Voici le contenu de votre liste : ")
        for i in range(len(LISTE)) :
            print(f"{i+1}. {LISTE[i]}")
    # Quatriene choix : Clear liste
    elif user_choice == MENU_CHOICE[3] :
        LISTE.clear()
        print("La liste à été vidée de son contenu.")
    # Cinquieme choix : Quitter le script
    elif user_choice == MENU_CHOICE[4] :
        # Quiter le programme
        print("À bientôt !")
        sys.exit()
    
    print("-" * 50)