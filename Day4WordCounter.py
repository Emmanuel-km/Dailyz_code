#have a text to count the words
#My_text="this is my daily code I passionatly write code everyday to enhance my coding skils walk with me in this path"
#using the strip method from user input
#the try block is for exception handling
#the function.strip removes white space at the ends
def user_input():
    try:
        My_text=input("enter text to be counted).strip()
     except:
         user_input()
user_input()
#using split() method

#split function saves the values in a list so for loop will be used
sentence=My_text.split(" ")
#declaring a count variable to count words in the text
count=0
for i in sentence:
    count+=1
#printing the outcome
print(f"The number of words present in text are {count}")


 

