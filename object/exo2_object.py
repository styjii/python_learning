class Voiture :
    def __init__(self) :
        self.essence = 100

    def afficher_reservoir(self) :
        print(f"La voiture contient {self.essence}L d'essence.")
    
    def roule(self, km) :
        if self.essence <= 0 :
            print("Vous n'avez plus d'essence, faite le plein !")
            return

        self.essence -= (km * 5) / 100
        
        if self.essence < 10 :
            print("vous n'avez bientot plus d'essence")

        self.afficher_reservoir()

    def faire_plein(self) :
        self.essence = 100
        print("Vous pouvez partir !")

if __name__ == "__main__" :
    voiture_01 = Voiture()
    voiture_01.afficher_reservoir()
    voiture_01.roule(25)
