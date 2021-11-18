
# from collections import namedtuple
# Figura = namedtuple('Figura', ['ranga', 'symbol'])

class Figura:
    def __init__(self, ranga, symbol):
        self.ranga = ranga
        self.symbol = symbol

        
# TBD
class Szachownica:
    def __init__(self):
        self.figury = []
    
    def dodaj_figure(self, ranga, symbol):
        figura = Figura(ranga, symbol)
        self.figury.append(figura)
