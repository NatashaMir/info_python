import random


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):

        while True:
            if self.player1.isfreecell():
                self.player1.step()
            else:
                print('Draw')
                break
            if self.player1.iswin():
                print('Player1 is winner!')
                break
            if self.player2.isfreecell():
                self.player2.step()
            else:
                print('Draw')
                break
            if self.player2.iswin():
                print('Player2 is winner!')
                break


class Player:
    def __init__(self, field, field_self):
        self.field = field
        self.field_self = field_self

    def isfreecell(self):
        return self.field.isfreecell()

    def step(self):
        x, y = self.getstepcoord()
        self.field.shot(x, y)
        self.field.show()
        self.field_self.show_self()

    def iswin(self):
        return self.field.allsunk()

    def getstepcoord(self):
        pass


class Human(Player):
    def __init__(self, field, field_self):
        Player.__init__(self, field, field_self)

    def getstepcoord(self):
        while True:
            x = int(input('Enter x in [0, 9]'))
            y = int(input('Enter y in [0, 9]'))
            # print("x %s, y is %s" % (x, y))
            if x not in range(0, 10) or y not in range(0, 10):
                print("Coordinate in an incorrect range")
            else:
                return x, y


class Computer(Player):
    def __init__(self, field, field_self):
        Player.__init__(self, field, field_self)

    def getstepcoord(self):
        x, y = self.field.getfreecell()
        # print(x)
        # print(y)
        return x, y


class Cell():
    def __init__(self):
        self.status = "p"


class Ship:
    def __init__(self, ship_type, cells):
        self.ship_type = ship_type
        self.cells = cells
        self.shoots = []
        self.state = 'Whole'

    def get_state(self):
        if len(self.shoots) == 0:
            pass
        elif len(self.shoots) == self.ship_type:
            self.state = 'Sunk'
        else:
            self.state = 'Damaged'
        return self.state

    def get_cells(self):
        all_ship_cells = []
        for cell in self.cells:
            all_ship_cells.append(cell)
        return all_ship_cells

    def get_shot(self, shot):
        self.shoots.append(shot)


class Field:
    def __init__(self):
        self.cells = []
        for i in range(0, 10):
            tmp = []
            for j in range(0, 10):
                tmp.append(Cell())
            self.cells.append(tmp)
        self.ships_type = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.ships = []
        self.aureole = []
        self.shipscreate()

    # The function displays the field and cell statuses
    def show(self):
        for i in range(0, 10):
            for j in range(0, 10):
                print(self.cells[i][j].status + " ", end='')
            print()
        print()

    def show_self(self):
        all_cells = self.show_ships_cells()
        for i in range(0, 10):
            for j in range(0, 10):
                if [i, j] in all_cells:
                    print('d' + " ", end='')
                else:
                    print('*' + " ", end='')
            print()

    # Function checks for empty cells

    def isfreecell(self):
        for i in range(0, 10):
            for j in range(0, 10):
                if self.cells[i][j].status == 'p':
                    return True
        return False

    # The function returns the first free cell
    def getfreecell(self):
        step = True
        while step == True:
            for i in range(0, 10):
                for j in range(0, 10):
                    if self.cells[i][j].status == 'p':
                        return i, j
                        step = False

    # Create ships
    # The function shipscreate() goes through an array of ship sizes and calls a function shipprint()
    def shipscreate(self):
        for size in self.ships_type:
            self.shipprint(size)

    # The function takes on the input the size of the ship, randomly selects coordinates on the field
    # and adds an object Ship ().
    # After that, it calls a function that adds the coordinates of the # aureole.

    def shipprint(self, size):
        status_tmp = True
        ship_tmp = []
        while status_tmp == True:
            # Take random coordinates in [0, 9]
            i = random.randint(0, 9 - size)
            j = random.randint(0, 9)
            for s in range(size):
                # print("s is %s" % (s))
                if [i + s, j] not in ship_tmp and [i + s, j] not in self.aureole:
                    # print("i is %s, j is %s" % (i+s, j))
                    ship_tmp.append([i + s, j])
                else:
                    ship_tmp = []
                    break
            if len(ship_tmp) == size:
                status_tmp = False
        # Create object Ship
        self.ships.append(Ship(size, ship_tmp))
        # Add aureole in list
        for k in ship_tmp:
            # self.cells[k[0]][k[1]].status = 's'
            # print((k[0], k[1]))
            self.set_aureole([k[0], k[1]])

    # The function adds the areola elements to the list self.aureole = []
    def set_aureole(self, cell):
        # print("cell is %s" % (cell))
        delta_comb = [(1, 1), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
        # add the cell to the list self.aureole = []
        if cell not in self.aureole:
            self.aureole.append(cell)

        for delta in delta_comb:
            ads = self.adds(cell, delta)
            # print("ads is %s" % (ads))
            if ads != 0 and ads not in self.aureole and ads[0] in range(0, 9) and ads[1] in range(0, 9):
                self.aureole.append(ads)
        # for f in self.aureole:
        # print("areol is %s" % (f))

    # The function takes the Ship to the input and returns a list of areola points for this ship
    def get_aureole(self, ship):
        areole = []
        delta_comb = [(1, 1), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
        for delta in delta_comb:
            for cell in ship.cells:
                ads = self.adds(cell, delta)
                if ads not in ship.cells and ads[0] in range(0, 9) and ads[1] in range(0, 9):
                    # print("ads[0] is %s, ads[1] is %s" % (ads[0], ads[1]))
                    areole.append(ads)
        return areole

    # Functions are transmitted coordinates of the "shot."
    # If the corresponding ship's coordinate is located, then the hit is displayed.
    # In addition, it is checked whether the ship is sunk.
    # In this case, an areola is placed around the ship.
    def shot(self, x, y):
        for ship in self.ships:
            if [x, y] in ship.cells:
                self.cells[x][y].status = 'd'
                ship.get_shot("shot")
                break
            else:
                self.cells[x][y].status = '*'
        if ship.get_state() == 'Sunk':
            areole = self.get_aureole(ship)
            for a in areole:
                # print("a is %s" % (a))
                self.cells[a[0]][a[1]].status = '*'

    # The function checks whether all ships are "sunk"
    def allsunk(self):
        countsunk = 0
        for ship in self.ships:
            if ship.get_state() == 'Sunk':
                countsunk += 1
                # print(countsunk)
        if countsunk == len(self.ships_type):
            return True
        else:
            return False

    # Function print own player ships
    def show_ships_cells(self):
        all_ships_cells = []
        for ship in self.ships:
            all_ships_cells.append(ship.get_cells())
        # return all_ships_cells
        # result = lambda all_ships_cells: [item for sublist in all_ships_cells for item in sublist]
        all_cells = [val for sublist in all_ships_cells for val in sublist]
        return all_cells

    def show_ships(self):
        for ship in self.ships:
            print(ship.get_state())

    # Auxiliary function.

    # Summarizes the elements of two lists of the same dimension element by element.
    def adds(self, cord, delta):
        sum_list = []
        for i in range(len(cord)):
            sum_list.append(cord[i] + delta[i])
        return sum_list


field1 = Field()
field2 = Field()

# field1.show_ships()
# print(field1.show_ships_cells())


player1 = Human(field1, field2)
# player1 = Computer(field1)
player2 = Computer(field2, field1)

# player1.isfreecell()
# player1.step()

game = Game(player1, player2)

game.start()