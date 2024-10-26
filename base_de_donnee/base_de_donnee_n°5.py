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

# deleter une element dans le database
cu.execute("DELETE FROM employees WHERE prenom='Paul'")

# detleter tous les elements dans la database
cu.execute("DELETE FROM employees")

cx.commit()
cx.close()