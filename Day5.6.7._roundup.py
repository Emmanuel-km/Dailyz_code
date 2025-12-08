#all week turn aroundup
#we will talk about the week
#MOnday we talked about naming rules,assignment,type checking
#Tuesday we talked about conditionals if elif else
def Tuesday_even_odd():
    try:
        number=int(input("enter a number to check if it's odd or even:  "))
        print("accepted")
        if number % 2== 0 :
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")
    except ValueError:
        import logging
        logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        filename="basic.log")
        logging.error("the user has not entered a number")
        print("enter a number please")
        Tuesday_even_odd()
Tuesday_even_odd()
#a good adjustment on the loging block 
