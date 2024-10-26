projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]

class Utilisateur:
    def __init__(self, nom, prenom) :
        self.nom = nom
        self.prenom = prenom
    
    def __str__(self) -> str:
        return f"Utilisateur {self.nom} {self.prenom}"
        
    def affiche_projets(self) :
        for projet in projets :
            print(projet)
            
# Heritier Junior par Utilisateur => On peut utiliser tous les methode de la class Utilisateur
class Junior(Utilisateur):
    def __init__(self, nom, prenom) :
        super().__init__(nom, prenom)
        
    # surcharge => affiche_projets dans Utilisateur est ecrasé par cette nouvelle affiche_projets
    def affiche_projets(self) :
        for projet in projets :
            if not projet.startswith("pr_") :
                print(projet)


paul = Junior("Paul", "Durand")
print(paul)
paul.affiche_projets()