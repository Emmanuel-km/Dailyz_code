#have a text to count the words
My_text="this is my daily code I passionatly write code everyday to enhance my coding skils walk with me in this path"
#using split() method
#split function saves the values in a list so for loop will be used
sentence=My_text.split(" ")
#declaring a count variable to count words in the text
count=0
for i in sentence:
    count+=1
#printing the outcome
print(f"The number of words present in text are {count}")


 

