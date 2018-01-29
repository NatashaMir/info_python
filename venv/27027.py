class My_metaclassA(type):
    def __new__(cls, name, base, dirs):
        return type.__new__(cls, name, base, dirs)

class My_metaclassB(type):
    def __new__(cls, name, base, dirs):
        return type.__new__(cls, name, base, dirs)

class My_metaclassC(My_metaclassA, My_metaclassB):
    pass

class My_classA(metaclass=My_metaclassA):
    pass

class My_classB(metaclass=My_metaclassB):
    pass

class My_classC(My_classA, My_classB, metaclass=My_metaclassC):
    pass