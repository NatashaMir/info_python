class ControlledClass:
    def __init__(self):
        self.value = 0
        self.control_classes = []

    def add_control_class(self, obj):
        self.control_classes.append(obj)

    def set_value(self, new_value):
        for control_obj in self.control_classes:
            control_obj.notify(self.value, new_value)
        self.value = new_value

class ControlClass:
    def notify(self, old_value, new_value):
        print("Parameter change from %s to %s" % (old_value, new_value))

obj_controlled = ControlledClass()
obj_controll = ControlClass()
obj_controlled.add_control_class(obj_controll)
obj_controlled.set_value(100)