class Account:
    def __init__(self,acc_no,pswrd):
        self.acc_no=acc_no
        self.__pswrd=pswrd
    def reset_paswrd(self):
        print(self.__pswrd)
acc1=Account(12145,"towqr")
print(acc1.acc_no)
print(acc1.reset_paswrd())