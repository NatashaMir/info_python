class Employee:
  def __init__(self, position, rate):
    self.position = position
    self.rate = rate #salary in one hour
    
class Crew:
  def __init__(self):
    self.employees = []
    
  def add_employee(self, employee):
    self.employees.append(employee)  
    
class Plane:
  def __init__(self, model, seat, fuel_expense):
    self.model = model
    self.seat = seat
    self.fuel_expense = fuel_expense
    

class Flight:
   
  tickets = 0
  
  def __init__(self, number, plane, distance, crew, ticket_cost):
    self.number = number
    self.plane = plane
    self.distance = distance
    self.crew = crew
    self.ticket_cost = ticket_cost
  

  def sale_ticket(self, n):
    if n <= self.plane.seat:
      Flight.tickets += n
    else:
        print("Number of seats exceeded")
        
  def total_cost(self):
    total=0
    for employee in self.crew.employees:
      total+=employee.rate
      print(employee.rate)
    total = total + self.plane.fuel_expense * self.distance + Flight.tickets * self.ticket_cost   
    return total   
        
    

Anna = Employee('stewardess', 100)
Mari = Employee('stewardess', 100)
Bob = Employee('pilot', 500)
Jack = Employee('pilot', 400)

crew = Crew()
crew.add_employee(Anna)
crew.add_employee(Bob)
crew.add_employee(Jack)

plane = Plane('Boing 134', 10, 3)

fligh = Flight('RT76H', plane, 100, crew, 50)

fligh.sale_ticket(10)

print(fligh.total_cost())

  
