print("Hello World")
print(print) #(Case-senstive)
age="20"
age2=20
Address="Matwari, Hazaribagh"
name="Aman Gurnani"
print(name,age,Address)
print(type(age), type(name), type(Address))
a=5; b=6; c=8 
# a=5
# b=6
# c=8
# a = 5 
# b = 6
# c = 8   #(right. Wrong a=5 b=6 c=8) 

sum=a+b+c
print(a+b+c)
print(sum)

a=5; b=6
# sum = a + b; product = a * b; diff = a - b, quotient = a / b; modulo = a % b, power = a ** b
print(a+b, a-b, a*b, a**b, a/b, a%b)
print(a==b, a>=b, a<=b, a!=b,)
# conversion: conversion of type1 variable to type2 variable. 
# two types of conversion: type conversion (automatic), and type casting (manual)
# float is superior than int, as more info is stored in float. 


a=5.12 #float
b=4 #int (auto converted into float)
#type conversion
sum=a+b
print(sum) #float

#typecasting 
a1= int(a)
sum2=b+a1 #(float manually converted into int)
print(sum2)

#user input mei humesha string datatype store hota hai 
val=input("Enter some value: ") 
print(type(val), val)

val=float(input("Enter some value: ")) #(str typecasted into float)
print(type(val), val)

#Question1: WAP to input two numbers and print their sum
val1=float(input("Enter the first number: "))
val2=float(input("Enter the second number: "))
print(val+val2)

#Question2: WAP to input side of a square and print its area. 
side=float(input("Enter the side: "))
print("area =", side*side)

#Question3: WAP to input two floating numbers and print their average. 
num1=float(input("Enter first number: "))
num2=float(input("Enter the second number: "))
sum=num1+num2
average=sum/2
print(average)
print("average=", (num1+num2)/2)

print("Hello, Aman!")
print ("How are you?"); print ("I am fine here") ; print ('can a line be written in python using single codes?') #each print starts a new line.

print ("I a learning python.",'Its really awesome') #in the same line.
print ("I am learning python.", end=" ") 
print ('Its really awesome')  #in the same line using 'end'.

#python variable should only contain alpha numeric number (A-Z, a-z, 0-9) and underscores. 

x,y,z = 5,6,7 
print (x,y,z) 
x = y = z = 6
print (x,y,z)
print (x+y+z)
a = "Hello World!" 
b = "My name is"
c = "Aman Gurnani" 
print (a,b,c) 
#by using '+' to combine variables, we have to manually create spaces. but on using comma ',', we get spaces by default. 

#to make a variable global, we have to declare it global before #initialiazing. 


x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview

x = 5 + 6j 
#y = int(x) #complex number can not be casted into another number.
print (y, type(x))
print 

x = 5.56 
y = complex(x) 
print (y,type(x), type(y))

# MyName = "Aman Gurnani" 
#y = float (MyName) 
#print (type(y))
#so, such type of string can not be converted into int or float.
MyNum = "45" 
y = float (MyNum) 
z= complex (MyNum)
print (y,z,type(y), type(z))











