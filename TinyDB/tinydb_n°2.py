import os

from tinydb import TinyDB, Query, where

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(CURR_DIR, "data.json")

with TinyDB(FILE, indent=4) as db:
    # mettre à jour un éléments dans la base de donnée
    # db.update({"score": 10}, where("name") == "Patrick")
    
    # rajoutée des informations à la base de données
    # => donner un rolé à tous les éléments (sans condition) dans la base de données
    # db.update({"roles" : ["Junior"]})
    # db.update({"roles": ["Pythonista"]}, where("name") == "Patrick")
    
    # inserer où mettre à joir des données || s'il existe il met à jour sinon il ajouter
    db.upsert({"name": "Pierre", "score": 10, "roles": ["Senior"]}, where("name") == "Pierre")
    
    # supprimer des éléments precis dans la base de données
    # db.remove(where("score") == 0)
    
    # supprimer tous les éléments dans la base de données
    # db.truncate()