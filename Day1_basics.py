#this is a simple calculator that combines string concantenation 
print("Hello there this a calculator")
print("Enter the operation needed:\n 1-multiplication \n2-addition \n 3-division \n4-subtraction \nany character to end")
try:
    choice=int(input("select a number:   "))
    list1=[1,2,3,4]
    if choice not in list1:
        raise TypeError
    x=int(input("enter first number: "))
    y=int(input("enter second number:  "))
except ValueError:
    choice=0
    breakpoint
except TypeError:
    choice=0
def multiplication(x,y):
    return x*y
def addition(x,y):
    return x+y
def division(x,y):
    return x/y
def subtraction(x,y):
    return x-y
if choice==1:
    results=multiplication(x,y)
    print(f"The results of the multiplication of {x} and {y} is {results} ")
elif choice==2:
    results=addition(x,y)
    print(f"The results of addition of {x} and {y} is {results} ")
elif choice==3:
    results=division(x,y)
    print(f"The results of the division of {x} and {y} is {results}")
elif choice==4:
    results=subtraction(x,y)
    print(f"The subtraction between {x} and {y} is {results}")
else:
    print("excuted SUCCEFFULLY")
