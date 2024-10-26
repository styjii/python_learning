import os
import sqlite3


CURR_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(CURR_DIR, "database.db")

cx = sqlite3.connect(FILE)

cu = cx.cursor()

cu.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text
)
""")

# recuperer le donnees dans le database qui a le prenom Paul
cu.execute("SELECT * FROM employees WHERE prenom=:prenom", {"prenom": "Pierre"})
donnees = cu.fetchall()
print(donnees)

print("-" * 50)

# recuperer tous les donnees dans le database
cu.execute("SELECT * FROM employees")
donnees = cu.fetchall()
print(donnees)

print("-" * 50)

# recuperer une par une tous les elements dans le database (dans cette exemple 4 elements)
cu.execute("SELECT * FROM employees")
premier = cu.fetchone()
print(premier)
deuxieme = cu.fetchone()
print(deuxieme)
troisieme = cu.fetchone()
print(troisieme)

print("-" * 50)

cx.commit()
cx.close()