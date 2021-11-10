class PseudoLiczba:
    def __init__(self, value):
        self.value = int(value)
        
    def __int__(self):
        return int(self.value)
   
    def __add__(self, other):
        value = int(self) + int(other)
        return PseudoLiczba(value)
    
    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return int(self) < other

    
pl1 = PseudoLiczba(10)
pl2 = PseudoLiczba(12)
print(pl1 + pl2)
print(pl1 + pl2 + 30)
print(pl2 + 50)
