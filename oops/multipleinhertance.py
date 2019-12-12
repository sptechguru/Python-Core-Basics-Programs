import time
class phone:

    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price


    def full_name(self):
        return f"{self.brand}{self.model_name} {self.price}"


#  multiple inheritance  in class phone is Dervive Class & Main Class
# smartphone is child Class


class Smartphone(phone):

    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram =ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def last_name(self):
        return f"{self.brand}{self.model_name} {self.price} {self.ram}{self.internal_memory} {self.rear_camera}"


phone = phone(' Nokia ','110',1000)
smartphone = Smartphone(' oneplus :','5+ :','30000 :' ,'6Gb :','64GB :','20Mp')
print(phone.full_name())
print()

time.sleep(2)
print(smartphone.last_name())



# print(smartphone.full_name()+ f" And Price is  {smartphone.price}{smartphone.ram} "
# f"{smartphone.internal_memory}{smartphone.rear_camera}")


