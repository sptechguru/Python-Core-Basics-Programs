class Person:
    def __init__(self,first_name, last_name, age):
        # print("Init Method is Called")
        self.name= first_name
        self.last = last_name
        self.age = age

    # That is class method is created by instances variables

    def full_name(self):
        return f"{self.name } {self.last }"

p2 = Person('Raj','pal',23)
print(p2.full_name())

# class method is called

p1 = Person('santosh','pal',24)
print(p1.name)





