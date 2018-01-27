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
    def __init__(self, field):
        self.field = field

    def isfreecell(self):
        return self.field.isfreecell()

    def step(self):
        nest_step = True
        while nest_step == True:
            x, y = self.getstepcoord()
            nest_step = self.field.shot(x, y)
            self.field.show()

    def iswin(self):
        return self.field.allsunk()

    def getstepcoord(self):
        pass


class Human(Player):
    def __init__(self, field):
        Player.__init__(self, field)

    def getstepcoord(self):
        while True:
            x = int(input('Enter x in [0,9]'))
            y = int(input('Enter y in [0,9]'))
            if x in list(range(9)) and y in list(range(9)):
                return x, y
                break
            else:
                print("Coordinates in the wrong range")


class Computer(Player):
    def __init__(self, field):
        Player.__init__(self, field)

    def getstepcoord(self):
        x, y = self.field.getfreecell()
        print(x)
        print(y)
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
        self.ships_type = [4, 3, 3]
        self.ships = []
        self.aureole = []
        self.shipscreate()

    def getfreecell(self):
        step = True
        while step == True:
            for i in range(0, 10):
                for j in range(0, 10):
                    if self.cells[i][j].status == 'p':
                        return i, j
                        step = False

    def isfreecell(self):
        for i in range(0, 10):
            for j in range(0, 10):
                if self.cells[i][j].status == 'p':
                    return True
        return False

    def shipscreate(self):
        for ship in self.ships_type:
            self.shipprint(ship)

    def shipprint(self, size):
        status_tmp = True
        ship_tmp = []
        while status_tmp == True:
            i = random.randint(0, 9 - size)
            j = random.randint(0, 9)
            for s in range(size):
                if self.cells[i + s][j].status == 'p' and [i + s, j] not in self.aureole:
                    ship_tmp.append([i + s, j])
                    status_tmp = False
                else:
                    break
        self.ships.append(Ship(size, ship_tmp))
        for k in ship_tmp:
            print((k[0], k[1]))
            self.set_aureole((k[0], k[1]))

    def adds(self, cord, delta):
        sum_list = []
        for i in range(len(cord)):
            sum_list.append(cord[i] + delta[i])
        return sum_list

    def set_aureole(self, cell):
        delta_comb = [(1, 1), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
        for delta in delta_comb:
            ads = self.adds(cell, delta)
            if ads != 0 and ads not in self.aureole and ads != cell:
                self.aureole.append(ads)
                self.aureole.append(cell)

    def show(self):
        for i in range(0, 10):
            for j in range(0, 10):
                print(self.cells[i][j].status + " ", end='')
            print()


    def shot(self, x, y):
        for ship in self.ships:
            if [x, y] in ship.cells:
                self.cells[x][y].status = 'd'
                ship.get_shot("shot")
                return True
            else:
                self.cells[x][y].status = '*'
                return False

    def allsunk(self):
        countsunk = 0
        for ship in self.ships:
            if ship.get_state() == 'Sunk':
                countsunk += 1
        print(countsunk)
        if countsunk == len(self.ships_type):
            return True
        else:
            return False




field1 = Field()
field2 = Field()

player1 = Human(field1)
player2 = Computer(field2)

game = Game(player1, player2)

game.start()