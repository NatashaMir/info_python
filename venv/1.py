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
        x, y = self.getstepcoord()
        self.field.shot(x, y)
        #self.field.cellwrite(x, y)
        self.field.show()

    def iswin(self):
        return self.field.allsunk()

    def getstepcoord(self):
        pass


class Human(Player):
    def __init__(self, field):
        Player.__init__(self, field)

    def getstepcoord(self):
        x = int(input('Enter x'))
        y = int(input('Enter y'))
        # x, y in [0,10]
        return x, y


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
    
    def get_cells(self):
      for cell in self.cells:
        print(cell)
        
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
        self.ships = []
        self.aureole = []
        self.shipscreate()

    def shipscreate(self):
        ships_type = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for ship in ships_type:
            self.shipprint(ship)
   
    def show_ship_cells(self):
      for ship in self.ships:
        ship.get_cells()



    def shipprint(self, size):
        status_tmp = True
        ship_tmp = []
        while status_tmp == True:
            i = random.randint(0, 9 - size)
            j = random.randint(0, 9)
            #print(i)
            #print(j)
            for s in range(size):
                if self.cells[i + s][j].status == 'p' and [i + s, j] not in self.aureole:
                    #print(i + s)
                    ship_tmp.append([i + s, j])
                    status_tmp = False
                else:
                    break
        self.ships.append(Ship(size, ship_tmp))          
        for k in ship_tmp:
            #self.cells[k[0]][k[1]].status = 's'
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
        #for f in self.aureole:
            #print(f)

    def show(self):
        for i in range(0, 10):
            for j in range(0, 10):
                print(self.cells[i][j].status + " ", end='')
            print()

    def show_ships(self):
        for ship in self.ships:
            print(ship.get_state())

    def isfreecell(self):
        for i in range(0, 10):
            for j in range(0, 10):
                if self.cells[i][j].status == 'p':
                    return True
        return False

    #def cellwrite(self, x, y):
    #    self.cells[x][y].status = '*'

    def shot(self, x, y):
        #if self.cells[x][y].status == "s":
          #self.cells[x][y].status = 'd'
        for ship in self.ships:
          if [x, y] in ship.cells:
            self.cells[x][y].status = 'd'
            ship.get_shot("shot")
            break
          else:
            self.cells[x][y].status = '*'

    def allsunk(self):
        countsunk = 0
        for ship in self.ships:
          if ship.get_state() == 'Sunk':
            countsunk += 1 
        print(countsunk)    
        if countsunk == 10:
            return True
        else:
            return False


    def getfreecell(self):
      step = True
      while step == True:
        for i in range(0, 10):
            for j in range(0, 10):
                if self.cells[i][j].status == 'p':
                  return i, j
                  step =  False




field1 = Field()
field2 = Field()

#field1.show_ships()
#field1.show_ship_cells()


player1 = Human(field1)
player2 = Computer(field2)

#player1.isfreecell()
#player1.step()

game = Game(player1, player2)

game.start()
