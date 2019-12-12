class Person:
    def __init__(self,person_name, person_last_name):
        self.name = person_name
        self.last = person_last_name

        print(Person.last)

    def about(self):
        return self.name +  ' ' + self.last

men =[]

for i in range(5):
    one = input(("Enter Person :"))
    one = one.split()

    men.append(person(one[0],one[1]))


 for i in range men:
     print(i.about(i))
