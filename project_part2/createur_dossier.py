from pathlib import Path

chemin = Path.cwd().joinpath("project", "folder_project")
chemin.mkdir(exist_ok=True)

d = {
    "Films" : [
        "Le seigneur des anneaux",
        "Harry Potter",
        "Moon",
        "Forrest Gump"
    ],
    "Employer" : [
        "Paul",
        "Pierre",
        "Marie"
    ],
    "Exercices" : [
        "les_variables",
        "les_fichiers",
        "les_boucles"
    ]
}

# chemin de tous les dossier Films, Employer, Exercices avec leur sous dossier
for folder in d:
    for f in d[folder] :
        dirs = chemin.joinpath(folder, f)
        # créer tous les dossier
        dirs.mkdir(parents=True, exist_ok=True)