films = {
    "Le Seigneur des Anneaux" : 12,
    "Harry Potter" : 9,
    "Blade Runner" : 7.5
}
prix = 0

for valeur in films :
    prix += films[valeur]

print(f"{prix}€")