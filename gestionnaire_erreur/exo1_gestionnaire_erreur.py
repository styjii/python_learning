liste = [2, 7, "texte", 4]
liste = [f for f in liste if str(f).isdigit()]

total = sum(liste)
print(total)