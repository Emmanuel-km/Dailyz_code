#fuctions in python
#a function is a group code that can be repeated many times as long it is called
#lets  acccept name input from the user
name=input("type y your name to be displayed: ")
#also age
# handling error by try except block
#handling error in a fuction so it repeats it until correct value is entered
def enter_age():
    try:
        age=int(input("enter your age: "))
        #making it a global variable
        return age
    except:
        #calling the function if error is found
        return enter_age()
        #enter_age()
#age is a local scope of the function enter_age
#so to make it global we use the return stateent plus redeclaring it into the code
#making age a gobal variable so that the function my_fuction may use it
age=enter_age()
#1.initializing the fuction block
def my_fuction(name,age):
    print(f"hello {name} you will be turning {(age+1)} soon")
my_fuction(name,age)