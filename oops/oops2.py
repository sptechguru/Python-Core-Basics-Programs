class Laptop:
    def __init__(self,name,model_name,Price):
        self.brand = name
        self.name = model_name
        self.laptop_name = name + ' ' + model_name
        self.rs =  Price

    # Laptop Discont offers apply_discont function are used

    def apply_discont(self,num):
        off_price = (num/100)*self.rs
        return self.rs - off_price



sp2 = Laptop('Dell','DSel44', 53000)
print(sp2.apply_discont(10))

sp = Laptop('lenovo','aut300', 3000)
print(sp.apply_discont(10))

print(sp.laptop_name)
# print(sp.rs)



