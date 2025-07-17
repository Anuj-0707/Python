class Student:
    college_name = "Niet" # class attribute
    def __init__(self,name,marks):
        self.name=name # obj attribute
        self.marks=marks
s1=Student("Anuj",97)
print(s1.name,s1.marks,Student.college_name)
s2=Student("Akash",95)
print(s2.name,s2.marks,Student.college_name)