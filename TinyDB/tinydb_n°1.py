import os

from tinydb import TinyDB, Query, where

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(CURR_DIR, "data.json")

with TinyDB(FILE, indent=4) as db:
    # ajouter une seul élément
    # db.insert({"name" : "patrick", "score": 0})
    # ajouter plusieur éléments
    # db.insert_multiple([
    #     {"name" : "Julie", "score": 50},
    #     {"name" : "Paul", "score": 120}
    # ])

    # cherche des éléments precis (User.name == Patrick) dans le base de données
    User = Query() # utiliser pour pouvoir utiliserle clée
    patrick = db.search(User.name == "Patrick")
    # chercher un éléments unique
    patrick_unique = db.get(User.name == "Patrick")
    
    # chercher par une sctructure conditionnelle
    paul = db.search(where("name") == "Paul")
    hight_score = db.search(where("score") > 0)
    
    # verifier un éléments dans la base de données
    exist_jean = db.contains(User.name == "Jean")
    
    # counté le nombre d'éléments qui rancontre cette condition :
    nombre_patrick = db.count(User.name == "Patrick")
    print(nombre_patrick)