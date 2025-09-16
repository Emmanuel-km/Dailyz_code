#using some variables declared on Day15_...
#so we will import
import Day15_NumpyWorking as d
#we are working with numpy
import numpy as np
#indexing is used to locate a specific value(s) from arrays
arr1=d.arr4
def indexing():
    #accesing a value from the second row second column
    #printing the result of the sum of the first and second value 
    # in the first row  
    # handling a three d array  
    print(f"The addition of {arr1[0,0,0]} and {arr1[0,0,1]} is {arr1[0,0,0]+arr1[0,0,1]}")
    #changing a row in the array
    arr1[0,2]=[2,3,4,5]
    print(arr1)
indexing()

