# Zadanie 1
class Alien:
    def __init__(self, name, age, planet):
        self.name = name
        self.age = age
        self.planet = planet
        
if __name__ == "__main__":
    a = Alien('Obcy1', 50, "Kepler-186f")
    print(f"Mam na imię {a.obcy}, mam {a.age} lat i pochodzę z planety {a.planet}")
