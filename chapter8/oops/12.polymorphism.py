#print(1+2) #OPERATION
#print("Anuj"+"Pandey") #concatenation
#print([1,2,3,4]+[5,6,7,8]) #MERGING
#DUNDER FUNCTIONS
#a+b   a.__add__(b)
#a-b   a.__sub__(b)
#a*b   a.__mul____(b)
#a/b   a.__truediv____(b)
#a%b   a.__mod____(b)


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show_number(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
num1=Complex(3,4)
num1.show_number()
num2=Complex(5,6)
num2.show_number()
num3=num1-num2
num3.show_number()
