class Manager:
    def __init__(self, builder):
        self.builder = builder

    def build(self):
        self.builder.build.fundament()
        self.builder.build.walls()
        self.builder.build.roof()

class Cottage:
    def __init__(self):
        self.fundament = None
        self.walls = None
        self.roof = None

class Cottage_builder:
    def __init__(self):
        self.house = Cottage()

    def fundament(self):
        self.house.fundament = 'fundament'

    def walls(self):
        self.house.walls = 'walls'

    def roof(self):
        self.house.roof = 'roof'

    def get_house(self):
        return self.house

builder = Cottage_builder()
manager = Manager(builder)
manager.build()
cottage = builder.get_house()