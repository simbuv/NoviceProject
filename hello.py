"""
my_name = 'Simbu'
print("Hello and welcome "+my_name+"!")

x,y,z="Orange","Banana","Apple"
print(x)
print(y)
print(z)

fruits=["Apple", "Banana", "Cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)
"""
#Create a variable outside of a function, and use it inside the function
x="awesome"

def myFunc():
    print(x+" Simbu")

myFunc()  

a= "Hello, World! "
#print(a[1])
#print(a[5:11])
#print(a[2:])
#print(len(a))
print(a[-11:-2])
print(a.upper())
#strip() method removes any whitespace
print(a.strip())
print(a.split(","))
#for x in "Banana":
    #print(x)

#format of strings
age = 36
txt = "my name is Simbu {}"
print(txt.format(age))
print(txt.capitalize())
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))

theList= ["Orange","Apple","Cherry"]
"""
print(theList[:2])
if "Apple" in theList:
    print("Yes,'apple' is in the fruits list")
else:
    print("Yes,'apple' is not in the fruits list")

theList[1]="BlackCurrent"
theList[1:3] = ["Fig","ButterFruit"]
"""
theList.insert(2,"WaterMelon")
theList.append("Tangerine")

#To append elements from another list to the current list
tropical = ["mango", "pineapple", "papaya"]
theList.extend(tropical)

#tuple

theList.remove("mango")
print(theList)
theList.pop(1)
#to remove last item
theList.pop()
print(theList)
del theList[0]
print(theList)
thetuple =("Kiwi","Grapes")
theList.extend(thetuple)
print(theList)

#Loop Through a List
thisList=["Apple","Banana","Cherry"]
#for x in theList:
#    print(x)

#Loop Through the Index Numbers
#Use the range() and len() functions to create a suitable iterable

for i in range(len(thisList)):
  print(thisList[i])