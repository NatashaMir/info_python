class Component(object):
    def __init__(self):
        pass

    def operation(self):
        pass


class Leaf(Component):
    def __init__(self):
        Component.__init__(self)

    def operation(self):
        pass

    def get_elements(self):
        print("some function")


class Composite(Component):
    def __init__(self):
        Component.__init__(self)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def operation(self):
        map(lambda x: x.operation(), self.children)

    def get_elements(self):
        for i in self.children:
            i.get_elements()

c = Composite()
c1 = Composite()
l = Leaf()
l_two = Leaf()
c.add_child(l)
c1.add_child(l_two)
c1.add_child(c)
c1.operation()
print(c1.children)
c1.get_elements()