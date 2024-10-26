import os
import sqlite3


CURR_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(CURR_DIR, "database.db")

cx = sqlite3.connect(FILE)

cu = cx.cursor()

cu.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text,
    salaire int
)
""")

# mettre à jourles donnees dans le database
obj = {"salaire": 2000, "prenom": "Paul", "nom": "Dupont"}
cu.execute("""
UPDATE employees SET salaire=:salaire WHERE prenom=:prenom AND nom=:nom
""", obj)

cx.commit()
cx.close()