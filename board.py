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
                print(f"Player {player} placed on x{x}, y{y}, z{z}")
                return True
        return False

    def top_color(self, x, y):
        for z in range(3, -1, -1):
            if self.layers[z].coordinates[y][x]:
                return self.layers[z].coordinates[y][x]
        return None

    def check_for_win(self):
        for z in range(4):
            result = self.layers[z].four_in_a_row()
            if result:
                return result
        for xy in range(16):
            counter = []
            for z in range(4):
                if self.layers[z].coordinates[xy%4][xy//4]:
                    counter.append(self.layers[z].coordinates[xy%4][xy//4])
            if counter == [1,1,1,1]:
                return 1
            if counter == [2,2,2,2]:
                return 2

        counter1 = []
        counter2 = []
        counter3 = []
        counter4 = []

        for i in range(4):
            if self.layers[i].coordinates[i][i]:
                counter1.append(self.layers[i].coordinates[i][i])
            if self.layers[i].coordinates[i][3-i]:
                counter2.append(self.layers[i].coordinates[i][i])
            if self.layers[3-i].coordinates[i][i]:
                counter3.append(self.layers[i].coordinates[i][i])
            if self.layers[3-i].coordinates[i][3-i]:
                counter4.append(self.layers[i].coordinates[i][i])

        if counter1 == [1,1,1,1] or counter2 == [1,1,1,1] or counter3 == [1,1,1,1] or counter4 == [1,1,1,1]:
            return 1
        if counter1 == [2,2,2,2] or counter2 == [2,2,2,2] or counter3 == [2,2,2,2] or counter4 == [2,2,2,2]:
            return 2

        return False

class Layer:
    def __init__(self, z):
        self.coordinates = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        self.z = z

    def four_in_a_row(self):
        for i in range(4):
            if self.coordinates[i] == [1,1,1,1]:
                return 1
            if self.coordinates[i] == [2,2,2,2]:
                return 2
        for column in range(4):
            counter = []
            for row in range(4):
                counter.append(self.coordinates[row][column])
            if counter == [1, 1, 1, 1]:
                return 1
            if counter == [2, 2, 2, 2]:
                return 2
        if not self.coordinates[0][0] == 0 and self.coordinates[0][0] == self.coordinates[1][1] == self.coordinates[2][2] == self.coordinates[3][3]:
            return self.coordinates[0][0]
        if not self.coordinates[0][3] == 0 and self.coordinates[0][3] == self.coordinates[1][2] == self.coordinates[2][1] == self.coordinates[3][0]:
            return self.coordinates[0][3]
        return False
