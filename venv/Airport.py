class Employee:
  def __init__(self, position, rate):
    self.position = position
    self.rate = rate #salary in one hour
    
class Crew:
  def __init__(self):
    self.employees = []
    
class Plane:
  def __init__(self, model, seat, fuel_expense):
    self.model = model
    self.seat = seat
    self.fuel_expense = fuel_expense
    
class Fuel:
  def __init__(self, prise):
    self.prise = prise
    
class Flight:
  def __init__(self, number, plane, distance, crew):
    self.number = number
    self.distance = distance
    self.crew = crew
  
  def fuel_expense(self):
    return plane.fuel_expense * distance
    
    
    
class Ticket:
  def __init__(self, flight, seat_number, prise):
    self.flight = flight
    self.seat_number = seat_number
    self.prise = prise
    
class Airline:
  def __init__(self, crew)
