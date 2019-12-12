class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def calc_circumference(self):
        return 2* Circle.pi*self.radius

C1 = Circle(4)
c2 = Circle(2)

print(C1.calc_circumference())