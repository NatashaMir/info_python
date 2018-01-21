class Employee:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

class Crew:
    def __init__(self):
        self.stuff = []

    def add(self,employee):
        self.stuff.append(employee)


class Plane:
    def __init__(self, place, fuel):
        self.place = place
        self.flue = flue

class Ticket:
    def __init__(self, number):
        self.id = number

class Flue:
    def __init__(self, price):
        self.price = price

class Flight
    def __init__(self, plane, price, crew):
        self.plane = plane
        self.price = price
        self.crew = crew

    def price_total(self):
        total = 0
        for employee in self.crew:
            total += box.cost()

