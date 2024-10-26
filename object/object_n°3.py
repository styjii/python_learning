class Voiture :
    voiture_creer = 0
    def __init__(self, marque, vitesse, prix) :
        Voiture.voiture_creer += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    # methode de classe
    @classmethod
    def lamborghini(cls) :
        return cls(marque="Lamborghini", vitesse=250, prix=200000)
    
    @classmethod
    def porsche(cls) :
        return cls(marque="Porsche", vitesse=200, prix=180000)
    
    # methode statique
    @staticmethod
    def affiche_nombre_voiture() :
        print(f"Vous avez {Voiture.voiture_creer} voiture dans votre garage")
    
lamborghini = Voiture.lamborghini()
porsche = Voiture.porsche()
Voiture.affiche_nombre_voiture()