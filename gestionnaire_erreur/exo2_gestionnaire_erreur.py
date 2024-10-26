from pathlib import Path

fichier = Path(input("Entrer le chemin de votre fichier : "))

try:
  with open(fichier, "r") as f:
    print(f.read())
except FileNotFoundError:
  print('le fichier {file} est introuvable'.format(file = fichier.name))
except PermissionError:
   print("Vous n'avez pas de permission !")