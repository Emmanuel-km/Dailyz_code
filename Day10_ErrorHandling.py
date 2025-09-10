#error handling is one core objectives in writing code 
#in a block so that it can catch errors(exceptions) while running
#main importance is to prevent the program crashing unexpected
#example:
#user=int(input("enter a number between 1 and 10: "))
#so what happens when a user doesn't enter a number
#the program crashes
#so we have to fix two issues here a user has to enter only a number between 1 and 10
#here is the code
def EnterNumber():
    #starting the try block
    try:
        number=int(input("enter number between 1 and 10: "))
        is_numberless=number<1
        is_numbergreater=number>10
        if is_numbergreater or is_numberless:
            print("not in the range")
            print("enter number again")
            EnterNumber()
    except ValueError:
        print("you entered a wrong data type please enter again")
        EnterNumber()
EnterNumber()