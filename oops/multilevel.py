import time
class Dad:
    basketball = 6
    guitar = 10
    def isdance(self):
        return f"No I Michel Jackson {self.dance} No of Times"

class Son(Dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes I Dance {self.dance} No of Times"

class Grandson(Son):
    dance = 6
    basketball = 9
    guitar = 1
    def isdance(self):
        return f"Yes I Michel Jackson {self.dance} No of Times"


darry = Dad()
larry = Son()
harry = Grandson()

print(darry.guitar)
time.sleep(2)
print(darry.basketball)


# electronic device
# pocket gadget
# phone