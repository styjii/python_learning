import os

from tinydb import TinyDB, Query, where

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(CURR_DIR, "data.json")

with TinyDB(FILE, indent=4) as db:
    # Utiliser plusieurs tables
    users = db.table("Users")
    roles = db.table("Roles")
    
    # inserer des éléments dans le table
    users.insert({"name": "Patrick", "salaire": 25000})
    users.insert({"name": "Paul", "salaire": 35000})
    users.insert({"name": "Julie", "salaire": 45000})
    
    roles.insert_multiple([
        {"name": "Pythonista"},
        {"name": "Javaista1"},
        {"name": "JavaScripta"}
    ])