import time
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f" Name is:- {self.name}. Salary is:- {self.salary} and role is:- {self.role}"
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f" Name is:- {self.name}. Salary is:- {self.salary} and role is:- {self.role}"

print('EMPLOYEE FIRST CLASS MAIN CLASS')

emp1 =Employee("Harry", 345000, "Programmer")
emp2 =Employee("Rohan", 5500, "WEB Designer")

print(str(emp1))
time.sleep(2)
print()
print('EMPLOYEE SECOND CLASS CHILD CLASS')

print(str(emp2))
