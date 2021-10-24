# Zadanie 2
class Rocket:
    def __init__(self, mass, fuel):
        self.mass = mass
        self.fuel = fuel
        
    def fuel_usage_to_fly_to_height(self, height):
        return 2 * self.mass * height
    
    def can_i_fly_to_height(self, height):
        required_usage = self.fuel_usage_to_fly_to_height(height)
        if required_usage < self.fuel:
            return True
        else:
            return False
          
if __name__ == "__main__":
    r = Rocket(1000, 2000)
    rocket_to_the_space = r.can_i_fly_to_height(20)
    print(f"Czy rakieta może wzbić się na 20metrów? {rocket_to_the_space}")
