class Person:
    name="Anonymous"
#   def change_name(self,name): instead of it
#        self.name=name
    @classmethod
    def change_name(cls,name):
        cls.name=name
s1=Person()
s1.change_name("Anuj")
print(s1.name)
print(Person.name)