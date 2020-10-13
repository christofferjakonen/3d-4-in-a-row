class Board:
    def __init__(self):
        self.layers = []
        for i in range(4):
            layer = Layer(i)
            self.layers.append(layer)

    def place_peg(self, x, y, player):
        for z in range(4):
            if self.layers[z].coordinates[y][x] == 0:
                self.layers[z].coordinates[y][x] = player
                print(f"Placed on x{x}, y{y}, z{z}")
                return True
        return False

    def top_color(self, x, y):
        for z in range(3, -1, -1):
            if self.layers[z].coordinates[y][x]:
                return self.layers[z].coordinates[y][x]
        return None


class Layer:
    def __init__(self, z):
        self.coordinates = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        self.z = z
