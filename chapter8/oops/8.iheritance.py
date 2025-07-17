# When one class (child/derived) derives the property & method of another class (parent/base).
class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
s1 = ToyotaCar("Fortuner")
print(s1.start())