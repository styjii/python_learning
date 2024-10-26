premier_nombre = deuxieme_nombre = ""
while not (premier_nombre.isdigit() and deuxieme_nombre.isdigit()) :
    premier_nombre = input("Entrer un premier nombre : ")
    deuxieme_nombre = input("Entrer un deuxième nombre : ")

    if not (premier_nombre.isdigit() and deuxieme_nombre.isdigit()) :
        print("Veuillez entrer deux nombres valides.")

addition = int(premier_nombre) + int(deuxieme_nombre)
print(f"Le résultat de l'addition de {premier_nombre} avec {deuxieme_nombre} est égal à {addition}")