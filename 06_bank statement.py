# create account class with two attributes -balance & account no. create methods for debit , credit & printing the balance
class Account:
    def __init__(self,bal,acc):
       self.balance =bal
       self.account_no=acc
    # debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs;",amount,"was debited ")
        print("total balance:",self.balance)   
        # credit method
    def credit(self,amount):
        self.balance+=amount
        print("Rs:",amount,"was credited")
        print("total balance:",self.balance)   
    def get_bal(self):
        return self.balance
acc1=Account(2000,2535701)
acc1.debit(200)
acc1.credit(500)
acc1.get_bal()
