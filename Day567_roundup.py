#all week turn aroundup
#we will talk about the week
#MOnday we talked about naming rules,assignment,type checking
#Tuesday we talked about conditionals if elif else
def Tuesday_even_odd():
    try:
        number=int(input("enter a number to check if it's odd or even:  "))
        print("accepted")
    except:
        print(f"an error has occured please enter a number")
        Tuesday_even_odd()
    #if number % 2== 0 :
            #print(f"{number} is an even number")
    #else:
            #print(f"{number} is an odd number")

Tuesday_even_odd()
