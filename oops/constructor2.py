import time
class Person:
    def __init__(self,first_name,last_name,age):
        print("instance method is called")
        self.name = first_name
        self.last = last_name
        self.age = age

pr = Person ('santosh','pal',25)
pr2 = Person ('Sani','Kumar',55)

print(pr.name)
print(pr.last)
print(pr.age)

time.sleep(2)
print("instance method is called Second times @@@@......")

print()

print(pr2.name)
print(pr2.last)
print(pr2.age)