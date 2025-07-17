class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        count=0
        for el in self.marks:
            sum+=el
            count+=1
        avg=sum/count
        print(f"{avg:.2f}")
s1=Student("Anuj",[98,99,95])
s1.get_avg()
