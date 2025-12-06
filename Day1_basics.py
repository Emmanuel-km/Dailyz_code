#this is a simple calculator that combines string concantenation 
# import math custom module
import math_operations.py as k
print("Hello there this a calculator")
print("Enter the operation needed:\n 1-multiplication \n2-addition \n 3-division \n4-subtraction \n5.- end")
try:
    choice=int(input("select a number:   "))
    list1=[1,2,3,4]
    while choice not in list1:
        #raise TypeError
        choice=int(input("select a number:   "))
    if choice==5:
        break
    else:
        x=int(input("enter first number: "))
        y=int(input("enter second number:  "))
    if choice==1:
        result=k.multiplication(x,y)
    if choice==2:
        result=k.addition(x,y)
    if choice==3:
        result=k.division(x,y)
    if choice==4:
        result=k.subtraction(x,y)
except ValueError:
    choice=0
    breakpoint
except TypeError:
    choice=0
except Exception as e:
    print(f"failed to catch {e}")

print("excuted SUCCEFFULLY")

