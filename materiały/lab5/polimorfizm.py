class Car:
    def __init__(self, marka, kolor):
        self.marka = marka
        self.kolor = kolor
 

class SUV(Car):
    def __init__(self, marka, kolor, naped4x4):
        super().__init__(marka, kolor)
        self.naped4x4 = naped4x4
        
    def jedz_po_krawezniku(self):
        print("Jade po krawezniku.")
        

class MiniVan(Car):
    def __init__(self, marka, kolor, drzwi_przesuwne):
        Car.__init__(self, marka, kolor)
        self.drzwi_przesuwne = drzwi_przesuwne
        
    def przesun_drzwi(self):
        print("przesuwam drzwi przesuwne.")
        

class Sport(Car):
    def __init__(self, marka, kolor, vmax):
        Car.__init__(self, marka, kolor)
        self.vmax = vmax
        
    def sciga(self):
        print("Scigam się z innym samochodem.")
        
        
class SportowyMiniVan(MiniVan, Sport):
    def __init__(self, marka, kolor, drzwi_przesuwne, vmax):
      MiniVan.__init__(self, marka, kolor, drzwi_przesuwne)
      Sport.__init__(self, marka, kolor, vmax)


class SportowySUV(SUV, Sport):
    def __init__(self, marka, kolor, naped4x4, vmax):
      SUV.__init__(self, marka, kolor, naped4x4)
      Sport.__init__(self, marka, kolor, vmax)

      
if __name__ == "__main__":         
  smv = SportowyMiniVan('Dodge', 'Czerwony', True, 160)
  smv.sciga()
  smv.przesun_drzwi()
