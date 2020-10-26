class Board:
    def __init__(self):
        self.layers = []
        for i in range(4):
            layer = Layer(i)
            self.layers.append(layer)

    def place_peg(self, x, y, player):
        for z in range(4):
            if self.layers[z].coordinates[x][y] == 0:
                self.layers[z].coordinates[x][y] = player
                # print(f"Player {player} placed on x{x}, y{y}, z{z}")
                return True
        return False

    def top_color(self, x, y):
        for z in range(3, -1, -1):
            if self.layers[z].coordinates[x][y]:
                return self.layers[z].coordinates[x][y]
        return 0

    def check_for_win(self):
        # check for vertical, horizontal or diagonal 4-in-a-row on a single plane, for every plane
        for z in range(4):
            result = self.layers[z].four_in_a_row()
            if result:
                return result

        check = self.check_z()
        if check:
            return check
        check = self.check_vertical()
        if check:
            return check
        check = self.check_horizontal()
        if check:
            return check
        check = self.check_diagonal()
        if check:
            return check

        return 0

    def check_horizontal(self):
        # check horizontal multi-plane, rising
        for y in range(4):
            counter = [self.layers[i].coordinates[y][i] for i in range(4) if self.layers[i].coordinates[y][i]]
            if counter == [1, 1, 1, 1]:
                return 1
            if counter == [2, 2, 2, 2]:
                return 2

        # check horizontal multi-plane, falling
        for y in range(4):
            counter = [self.layers[i].coordinates[y][3 - i] for i in range(4) if self.layers[i].coordinates[y][3 - i]]
            if counter == [1, 1, 1, 1]:
                return 1
            if counter == [2, 2, 2, 2]:
                return 2

        return 0

    def check_z(self):
        # check every xy coordinate for a 4-in-a-row on the z axis
        for xy in range(16):
            counter = [self.layers[z].coordinates[xy//4][xy%4] if self.layers[z].coordinates[xy//4][xy%4] else 0 for z in range(4) ]
            if counter == [1, 1, 1, 1]:
                return 1
            if counter == [2, 2, 2, 2]:
                return 2

        return 0

    def check_vertical(self):
        # check vertical multi-plane, rising
        for x in range(4):
            counter = [self.layers[i].coordinates[i][x] if self.layers[i].coordinates[i][x] else 0 for i in range(4)]
            if counter == [1, 1, 1, 1]:
                return 1
            if counter == [2, 2, 2, 2]:
                return 2

        # check vertical multi-plane, falling
        for x in range(4):
            counter = [self.layers[i].coordinates[3 - i][x] if self.layers[i].coordinates[3 - i][x] else 0 for i in range(4)]
            if counter == [1, 1, 1, 1]:
                return 1
            if counter == [2, 2, 2, 2]:
                return 2

        return 0

    def check_diagonal(self):
        # check diagonal multi-plane lines
        counter1 = [self.layers[i].coordinates[i][i] for i in range(4)]
        counter2 = [self.layers[i].coordinates[i][3-i] for i in range(4)]
        counter3 = [self.layers[3-i].coordinates[i][i] for i in range(4)]
        counter4 = [self.layers[3-i].coordinates[i][3-i] for i in range(4)]

        if counter1 == [1, 1, 1, 1] or counter2 == [1, 1, 1, 1] or counter3 == [1, 1, 1, 1] or counter4 == [1, 1, 1, 1]:
            return 1
        if counter1 == [2, 2, 2, 2] or counter2 == [2, 2, 2, 2] or counter3 == [2, 2, 2, 2] or counter4 == [2, 2, 2, 2]:
            return 2

        return 0


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
        # check rows
        for i in range(4):
            if self.coordinates[i] == [1, 1, 1, 1]:
                return 1
            if self.coordinates[i] == [2, 2, 2, 2]:
                return 2
        # check columns
        for column in range(4):
            counter = [self.coordinates[row][column] for row in range(4)]
            if counter == [1, 1, 1, 1]:
                return 1
            if counter == [2, 2, 2, 2]:
                return 2
        # check diagonals
        if self.coordinates[0][0] and self.coordinates[0][0] == self.coordinates[1][1] == self.coordinates[2][2] == self.coordinates[3][3]:
            return self.coordinates[0][0]
        if self.coordinates[0][3] and self.coordinates[0][3] == self.coordinates[1][2] == self.coordinates[2][1] == self.coordinates[3][0]:
            return self.coordinates[0][3]

        return 0
