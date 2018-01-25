import random
from itertools import permutations as comb

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
    def __init__(self, field_self, field_opponent):
        self.field_self = field_self
        self.field_opponent = field_opponent

    def isfreecell(self):
         return self.field_opponent.isfreecell()

    def step(self):
        x, y = self.getstepcoord()
        self.field_opponent.cellwrite(x, y)
        self.field_opponent.show()

    def iswin(self):
        return self.field.isline(self.mark)

    def getstepcoord(self):
        pass

class Human(Player):
    def __init__(self, field_self, field_opponent):
        Player.__init__(self, field_self, field_opponent)

    def getstepcoord(self):
        x = int(input('Enter x'))
        y = int(input('Enter y'))
        #x, y in [0,10]
        return x, y


class Computer(Player):
    def __init__(self, field_self, field_opponent):
        Player.__init__(self, field_self, field_opponent)

    def getstepcoord(self):
        x, y = self.field_opponent.getfreecell()
        return x, y

class Cell():
    def __init__(self):
        self.status = "p"
        
class Ship:
    def __init__(self, ship_type, cells):
        self.ship_type = ship_type
        self.cell = []
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


class Field:
    def __init__(self):
        self.cells = []
        for i in range(0,10):
            tmp = []
            for j in range(0,10):
                tmp.append(Cell())
            self.cells.append(tmp)
        self.ships = []   
        self.aureole = []
            

    def shipscreate(self):
      ships_type = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
      for ship in ships_type:
        self.shipprint(ship)

    def shipprint(self, size):
        status_tmp = True
        ship_tmp = []
        while status_tmp == True:
          i = random.randint(0, 9-size)
          j = random.randint(0, 9)
          print(i)
          print(j)
          for s in range(size):
            if self.cells[i+s][j].status == 'p' and [i+s, j] not in self.aureole:
              print(i+s)
              ship_tmp.append([i+s,j])
              status_tmp = False
            else:
              break
        for k in ship_tmp:
            self.cells[k[0]][k[1]].status = 's'
            self.set_aureole((k[0], k[1]))
        self.ships.append(Ship(size, ship_tmp))    
          
    def adds(self, cord, delta):
     	sum_list = []
     	for i in range(len(cord)):
     		  sum_list.append(cord[i] + delta[i])
     	return sum_list  

    def set_aureole(self, cell):
      delta_comb = list(comb(range(-1, 2), 2))
      delta_comb += [(1, 1), (-1, -1)]
      for delta in delta_comb:
          ads = self.adds(cell, delta)
          if ads != 0 and ads not in self.aureole and ads != cell:
            self.aureole.append(ads)
      for f in self.aureole:
        print(f)
    

    def show(self):
        for i in range(0,10):
            for j in range(0,10):
                print(self.cells[i][j].status + " ", end = '')
            print() 
            
    def show_ships(self):
      for ship in self.ships:
        print(ship.get_state())
        
    def isfreecell(self):
         for i in range(0,10):
             for j in range(0,10):
                 if self.cells[i][j].status == 'p':
                     return True
         return False


    def cellwrite(self, x, y):
        self.cells[x][y].status = '*'


    def isline(self, mark):
        for i in range(0,3):
            if self.cells[i][0].status == mark and self.cells[i][1].status == mark and self.cells[i][2].status == mark:
                return True
        for i in range(0,3):
            if self.cells[0][i].status == mark and self.cells[1][i].status == mark and self.cells[2][i].status == mark:
                return True
        if self.cells[0][0].status == mark and self.cells[1][1].status == mark and self.cells[2][2].status == mark:
            return True
        if self.cells[0][2].status == mark and self.cells[1][1].status == mark and self.cells[2][0].status == mark:
            return True
        return False

    def getfreecell(self):
        for i in range(0,10):
            for j in range(0,10):
                if self.cells[i][j].status == 'p':
                    return i,j        
          
field = Field()

field.show()

field.shipscreate()

field.show()

field.show_ships()

