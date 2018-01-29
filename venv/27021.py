class Container_interface:
    def clone(self):
        pass

    def add(self, element):
        pass

    def contance(self, element):
        pass

    def size(self):
        pass

    def get(self, index):
        pass


class Set():
    def __init__(self, container):
        self.container = container

    def union(self, other_set):
        result_set = Set(self.container.clone())
        for i in range(0, other_set.container.size()):
            set_element = other_set.container.get(i)
            if not result_set.container.contance(set_element):
                result_set.container.add(set_element)
        return result_set


class List_container(Container_interface):
    def __init__(self):
        self.lis = []

    def clone(self):
        list_container = List_container()
        list_container.lis = self.lis[::]
        return list_container

    def add(self, element):
        self.lis.append(element)

    def contance(self, element):
        return element in self.lis

    def size(self):
        return len(self.lis)

    def get(self, index):
        return self.lis[index]

container = List_container()

container.add(1)
container.add(2)
container.add(3)
container.add(4)

set = Set(container)

container1 = List_container()

container1.add(1)
container1.add(2)
container1.add(6)
container1.add(7)

set1 = Set(container1)

new_set = set.union(set1)

for i in range(0, new_set.container.size()):
    print(new_set.container.get(i))