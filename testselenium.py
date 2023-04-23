# Klasa jest szablonem (przepisem),
class Czlowiek:
    gatunek = "homo sapiens"
    # Ciało klasy
    def __init__(self, imie):
        """Metoda inicjalizacyjna"""
        print("Tworzę nowego Czlowieka o imieniu", imie)
        self.imie = imie

    def przedstaw_sie(self):
        print("Hej, jestem", self.imie)

class Dziecko(Czlowiek):
    def baw_sie(self):
        print("Ale zabawa, juhuuu!")

    def przedstaw_sie(self):
        print("Ceść, jestem", self.imie)

# .. z którego powstaje obiekt (danie)
# Instancja klasy
adam = Czlowiek("Adam") # adam.imie = "Adam"
ewa = Czlowiek("Ewa") # ewa.imie = "Ewa"

print(type(adam))
print(type(ewa))

print(adam.imie)
print(ewa.imie)

adam.przedstaw_sie()

kain = Dziecko("Kain")
kain.przedstaw_sie()
kain.baw_sie()