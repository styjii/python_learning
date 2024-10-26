from pathlib import Path

file = Path.cwd().joinpath("project", "prenoms.txt")
new_file = file.parent.joinpath("prenoms_tri.txt")

if file.exists() :
    with open(file, "r") as f:
        prenoms = f.read().splitlines()

    # ajout chaque prenom dans une liste prenoms
    prenoms_final = []
    for prenom in prenoms :
        prenom = prenom.split(" ")
        prenoms_final.extend(prenom)

    prenoms_final = [prenom.strip(",. ") for prenom in prenoms_final]

    # ecrire le prenom dans une fichier prenoms_tri et triéer
    if not new_file.exists() :
        new_file.touch()
        with open(new_file, "w") as f:
            f.write("\n".join(sorted(prenoms_final)))
    else :
        print("Le fichier {file} est deja exist !".format(file = new_file.name))
else :
    print("le fichier {file} à triée n'existe pas !".format(file=file.name))