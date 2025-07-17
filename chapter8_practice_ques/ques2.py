class Account:
    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc_no=acc_no
    #debit method
    def debit(self,amount):
        if(amount<=self.bal):
            self.bal-=amount
            print("Rs.",amount,"is debited")
            print("Total balance = ",self.bal)
        else:
            print("Not Enough balance")
    #credit method
    def credit(self,amount):
        self.bal+=amount
        print("Rs.",amount,"is credited")
        print("Total balance = ",self.bal)
acc1 = Account(10000, 102341563890)
mode=input("Enter D for debit or C for credit : ")
print(acc1.bal)
print(acc1.acc_no)
if (mode=="C" or mode=="c"):
    amount=float(input("Enter amount to credit : "))
    acc1.credit(amount)
if (mode=="D" or mode=="d"):
    amount=float(input("Enter amount to debit : "))
    acc1.debit(amount)