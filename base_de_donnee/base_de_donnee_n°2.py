import os
import sqlite3


CURR_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(CURR_DIR, "database.db")

cx = sqlite3.connect(FILE)

cu = cx.cursor()

# creer une tableau
cu.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text,
    salaire int
)
""")

# inserer une valeur dans le database
obj = {"prenom": "Paul", "nom": "Dupont", "salaire": 1000}
cu.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", obj)

cx.commit()
cx.close()