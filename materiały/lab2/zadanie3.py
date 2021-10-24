# Zadanie 3
class Box:
    #                  size = (l, w, h)
    def __init__(self, size):
        l, w, h = size
        self.volume = l * w * h
        self.space_left = self.volume
        self.inside_boxes = []
    
    def put_in(self, other_box):
        if other_box.volume < self.space_left:
            self.space_left -= other_box.volume
            self.inside_boxes.append(other_box)
        else:
            print("Brak miejsca!")
            
if __name__ == "__main__":
    b1 = Box(size=(5, 5, 5))  # volume = 125
    b2 = Box(size=(5, 4, 3))  # volume = 60
    b1.put_in(b2)
    print(f"Wolne miejsce: {b1.space_left}")
