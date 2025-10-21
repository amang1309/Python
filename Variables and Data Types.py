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






