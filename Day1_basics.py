#this is a simple calculator that combines string concantenation 
# import math custom module
import math_operations.py as k
print("Hello there this a calculator")
print("Enter the operation needed:\n 1-multiplication \n2-addition \n 3-division \n4-subtraction \nany character to end")
try:
    choice=int(input("select a number:   "))
    list1=[1,2,3,4]
    while choice not in list1:
        #raise TypeError
        choice=int(input("select a number:   "))
    if choice==4:
        break
    else:
        x=int(input("enter first number: "))
        y=int(input("enter second number:  "))
    if choice==1:
        result=k.multiplication(x,y)
except ValueError:
    choice=0
    breakpoint
except TypeError:
    choice=0
except Exception as e:
    print(f"failed to catch {e}")

print("excuted SUCCEFFULLY")

