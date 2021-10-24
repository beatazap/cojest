# Zadanie 1
class Alien:
    def __init__(self, name, age, planet):
        self.name = name
        self.age = age
        self.planet = planet
        
if __name__ == "__main__":
    alien1 = Alien('Obcy1', 50, "Kepler-186f")
    alien2 = Alien('Obcy2', 60, "Kepler-452b")

    print(f"Mam na imię {alien1.obcy}, mam {alien1.age} lat i pochodzę z planety {alien1.planet}")
    print(f"Mam na imię {alien2.obcy}, mam {alien2.age} lat i pochodzę z planety {alien2.planet}")
