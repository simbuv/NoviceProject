class listoperations:
    def __init__(myObj, name, age):
        myObj.name = name
        myObj.age = age

    def myName(obj):
        print("Hello "+obj.name)


p1 = listoperations("Simbu",36)

print(p1.name)
print(p1.age)
print(p1.myName())

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname,self.firstname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome",self.firstname,self.lastname, "to the class of",self.graduationyear)

x = Student("Simbu", "San", 2019)
x.welcome()