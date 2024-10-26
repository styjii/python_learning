class Voiture :
    def __init__(self, marque, vitesse) :
        self.marque = marque
        self.vitesse = vitesse
    
    # methode str
    def __str__(self) -> str:
        return f"Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse}"

lamborghini = Voiture("Lamborghini", 250)
print(lamborghini)