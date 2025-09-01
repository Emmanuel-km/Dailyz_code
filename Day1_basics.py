#this is a simple calculator that combines string concantenation 
print("Hello there this a calculator")
print("Enter the operation needed:/n 1-multiplication 2-addition 3-division 4-subtraction")
choice=input("select a number")
list1=[1,2,3,4]
while choice not in list1:
  choice=input("select a number")
x=input("enter first number")
y=input("enter second number")
def multiplication(x,y):
 print(multiple=x*y)
def addition(x,y):
 print(addition=x+y)
def division(x,y):
 print(division=x/y)
def subtraction(x,y):
 print(multiple=x-y)
if choice==1:
 mulitplication(x,y)
elif choice==2:
 addition(x,y)
elif choice==3
 division(x,y)
else
 subtraction(x,y)
