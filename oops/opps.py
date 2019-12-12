class Person:
    def __init__(self,first_name, last_name, age):
        print("Init Method")
        self.name= first_name
        self.last = last_name
        self.age = age

p1 = Person('santosh','pal',24)
print(p1.name)
print(p1.last)
print(p1.age)





