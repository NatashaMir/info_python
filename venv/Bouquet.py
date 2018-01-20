class Flower:
  def __init__(self, name, color, price):
    self.name = name
    self.color = color
    self.price = price
    
    
class Accessory:
  def __init__(self, color, price):
    self.color = color
    self.price = price
    
class Bouquet:
  def __init__(self):
        self.units=[]
      
  def add(self, unit, count = 1):
    for i in range(count):
      self.units.append(unit)
    
  def total_cost(self):
        total=0
        for unit in self.units:
            total+=unit.price
        return total  
      
      
rose = Flower('rose', 'red', 30)   
chamomile = Flower('chamomile', 'white', 10)

ribbon = Accessory('green', 20)
bow = Accessory('red', 25)

bouquet = Bouquet()

bouquet.add(rose, 3)
bouquet.add(chamomile, 4)
bouquet.add(ribbon)
bouquet.add(bow)

print(bouquet.total_cost())
