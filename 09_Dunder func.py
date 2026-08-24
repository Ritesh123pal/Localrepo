# create a class called order which stores item and its price.use dunder function__gt__()to convey that:order1>order2 if price of order1 > price of order2
class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2): #dunder fun
        return (self.price>ord2.price)
        
ord1=order("chips",20)
ord2=order("biscuit",10)        
print(ord1>ord2) #true
