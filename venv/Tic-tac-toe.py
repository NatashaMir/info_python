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
    def __init__(self, field, mark):
        self.field = field
        self.mark = mark

    def isfreecell(self):
         return self.field.isfreecell()

    def step(self):
        x, y = self.getstepcoord()
        self.field.cellwrite(x, y, self.mark)
        self.field.show()

    def iswin(self):
        return self.field.isline(self.mark)

    def getstepcoord(self):
        pass

class Human(Player):
    def __init__(self, field, mark):
        Player.__init__(self, field, mark)

    def getstepcoord(self):
        x = int(input('Enter x'))
        y = int(input('Enter y'))
        #x, y in [0,2]
        return x, y


class Computer(Player):
    def __init__(self, field, mark):
        Player.__init__(self, field, mark)

    def getstepcoord(self):
        x, y = self.field.getfreecell()
        return x, y

class Cell():
    def __init__(self):
        self.status = "p"

class Field:
    def __init__(self):
        self.cells = []
        for i in range(0,3):
            tmp = []
            for j in range(0,3):
                tmp.append(Cell())
            self.cells.append(tmp)


    def isfreecell(self):
         for i in range(0,3):
             for j in range(0,3):
                 if self.cells[i][j].status == 'p':
                     return True
         return False


    def cellwrite(self, x, y, mark):
        self.cells[x][y].status = mark


    def show(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.cells[i][j].status + " ", end = '')
            print()


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
        for i in range(0,3):
            for j in range(0,3):
                if self.cells[i][j].status == 'p':
                    return i,j

field = Field()

player1 = Human(field, 'x')
player2 = Computer(field, 'y')

game = Game(player1, player2)

game.start()