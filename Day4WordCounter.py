#have a text to count the words
#My_text="this is my daily code I passionatly write code everyday to enhance my coding skils walk with me in this path"
#using the strip method from user input
#the try block is for exception handling
#the function.strip removes white space at the ends
def user_input():
    try:
        My_text=input("enter text to be counted").strip()
        if len(My_text)<1:
            raise ValueError
        return My_text
    except ZeroDivisionError:
         user_input()
    except ValueError:
        print("you entered unnecessary and unrecognizable text\n please enter again")
        import logging
        logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        filename="basic.log")
        logging.error("the user has left blank space")
        user_input()
My_text=user_input()
#using split() method

#split function saves the values in a list so for loop will be used
try:
    sentence=My_text.split(" ")
except AttributeError:
    import logging
    logging.basicConfig(
    level=logging.CRITICAL,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    filename="basic.log")
    logging.critical("the user hasnt entered any thing")
    My_text=user_input()
#declaring a count variable to count words in the text
count=0
for i in sentence:
    count+=1
#printing the outcome
print(f"The number of words present in text are {count}")