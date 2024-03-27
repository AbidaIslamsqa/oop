#Count Discount price using oop
mobile=["i-phone",100000]
class product:
    def __init__(self , name , price):
        self.name1 = name
        self.price1 = price
    def pricediscount(self,discount):
        self.price1-=discount
mobile=product("i-phone", 100000)
print(mobile.name1, "Price is", mobile.price1) 
mobile.pricediscount(2000)
print(mobile.name1, "Discount Price is", mobile.price1)

