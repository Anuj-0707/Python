# methods are functions that belong to objects
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("Hello",self.name)
    def get_marks(self):
        return self.marks
s1=Student("Anuj",98)
s1.welcome()
print(s1.get_marks())
