class Coffee:
    def __init__(self, type, price):
        self.type = type
        self.price = price

class Box:
    def __init__(self, coffee, weight):
        self.coffee=coffee
        self.weight=weight

    def cost(self):
        return self.coffee.price*self.weight

class Lorry:
    def __init__(self):
        self.boxes=[]

    def add(self,box):
        self.boxes.append(box)

    def total_cost(self):
        total=0
        for box in self.boxes:
            total+=box.cost()
        return total

arabica=Coffee("arabica",100)
rabusta=Coffee("rabusta",200)

box1=Box(arabica,10)
box2=Box(rabusta,40)
box3=Box(arabica,90)

lorry=Lorry()
lorry.add(box1)
lorry.add(box2)
lorry.add(box3)
print(lorry.total_cost())