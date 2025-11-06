import logging
def conditionals():
    #if condition
    age=20
    if age>=18:
        print("The respondent is an adult")
    #if else condition
    age=13
    if age>=18:
        print("The respondent is an adult")
    else:
        print("The respondent is a child")
    #nested if elifs
    #grade calculator
    #five subjects
    all_subjects=[71,64,91,84,100]
    Sum=Average=0
    for i in all_subjects:Sum+=i
    Average=Sum/5
    #now the statements
    if Average>94:
        print("grade scored is A")
    elif Average>88:
        print("grade scored is B")
    elif Average>84:
        print("grade scored is C")
    else:
        print("grade is D failed ")
#conditionals()

def exceptionsHandling():
    #try and except block is great at cashing errors
    #before it crashes the process
    #catching zero division error
    #so this code calls its function
    #when it finds any error without crashing
    try:
        x=int(input("enter first number: "))
        y=int(input("enter second number: "))
        division=x/y
        print(f"The division ➗ of {x} and {y} is {division}")
    except ZeroDivisionError:
        print("you entered a zero value so it can be worked on try again")
        import logging
        logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        filename="basic.log")
        logging.error("zerodivision has occured")
        exceptionsHandling()
    except:
        exceptionsHandling()
exceptionsHandling()


