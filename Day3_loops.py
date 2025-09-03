def for_Loops():
    try:
        #for loops with ranges
        for i in range(5):
            print(i)
            print(i+1)
        #for loops with lists
        list_even=[2,4,6,8,10]
        for i in list_even:
            print(i**2)
        #nested for loops
        list1=[1,2,3]
        list3=["b","c","d"]
        for i in list1:
            print(i)
            for j in list3:
                print(j)

        #loop control continue
        #this for loop will jump 4 hence not print it
        for i in list_even:
            if i==4:
                continue 
            else:
                print(i)
    except:
        ("error has been catched")
    
for_Loops()
def while_loops():
    #with conter and loop control ..
    #..break,continue,pass
    #conter can count up or down
    #depending on the situation 
    password="password"
    user_try=input("enter the password ")
    user_NumberOfTries=1
    while user_try!=password:
        user_try=input(f"input the password you have  tries remaining")
        user_NumberOfTries+=1
        if user_NumberOfTries==4:
            print("maximum tries reached")
            break
#while_loops()
