class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
#    def cal_percent(self):
#       self.percent=(self.phy+self.math+self.chem)/3 instead of it
#        print(f"{self.percent:.2f}%")
    @property
    def percent(self):
        return f"{((self.phy+self.math+self.chem)/3):.2f}%"
st1 = Student(99,98,97)
print(st1.percent)
st1.phy=86
print(st1.percent)