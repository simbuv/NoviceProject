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