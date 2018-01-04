class Circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius

    def square(self):
        return 3.14*self.radius*self.radius


circle=Circle(10,20,300)
circle1=Circle(40,50,600)
int_res=circle.square()
print(int_res)