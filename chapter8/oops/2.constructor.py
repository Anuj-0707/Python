#__init__Function
class Student:
    #default constructor
    def __init__(self):
        pass
    # parameterised constructor
    def __init__(self,name,marks): # constructor take self as first parameter
        self.name=name
        self.marks=marks
        print("Adding new student in database..")
s1=Student("Anuj",97)
print(s1.name, s1.marks,sep="\n")