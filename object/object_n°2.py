class Voiture :
    def __init__(self, marque) :
        self.marque = marque

    def affiche_marque(self, vitesse) :
        print(f"La voiture est une {self.marque} de {vitesse}km/h")

voiture_01 = Voiture("Lamborghini")
voiture_01.affiche_marque(150)

voiture_02 = Voiture("Pegeot")
voiture_02.affiche_marque(70)
