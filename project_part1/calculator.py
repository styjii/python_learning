a, b = ""

while not a.isdigit() or not b.isdigit() :
    a = input("Entrer un premier nombre : ")
    b = input("Entrer un deuxième nombre : ")
    if not (a.isdigit() and b.isdigit()) :
        print("Veuillez entrer deux nombres valides")

print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")