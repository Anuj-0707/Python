# Those method which do not use self parameter(work at class level)
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("Hello")
    def get_avg(self):
        sum=0
        count=0
        for el in self.marks:
            sum+=el
            count+=1
        avg=sum/count
        print(f"hello {self.name} your avg is :{avg:.2f}")
s1=Student("Anuj",[98,99,95])
s1.get_avg()
s1.hello()

