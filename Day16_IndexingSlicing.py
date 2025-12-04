#using some variables declared on Day15_...
#so we will import
import Day15_NumpyWorking as d
#we are working with numpy
import numpy as np
#indexing is used to locate a specific value(s) from arrays
arr1=d.arr4
arrK=d.arr10
def indexing():
    #accesing a value from the second row second column
    #printing the result of the sum of the first and second value 
    # in the first row  
    # handling a three d array  
    print(f"The addition of {arr1[0,0,0]} and {arr1[0,0,1]} is {arr1[0,0,0]+arr1[0,0,1]}")
    #changing a row in the array
    arr1[0,2]=[2,3,4,5]
    print(arr1)
#indexing()
def negativeIndexing():
    print(arr1)
    #accessing the second row in the first column
    print(arr1[-2,1])
    #acccessing it purely negative indexing
    print(arr1[-2,-2])
#negativeIndexing()
def columnExtraction():
    #to extract a column we use [:,]
    print(arr1[:,2])
#columnExtraction()

#slicing

#slicing ranges
def slice():
    #slicing 3-d list
    #so making arr2 with the two middle values of the first
    #first array in arr1
    arr2=(arr1[0][0][1:3])
    print(arr2)
    arr2=np.arange(0,9)
    #one d
    arr3=arr2[3:]
    #print(arr3)
    #two d
#slice()

#Array broadcasting
def broadcasting():
    #declaring the variable
    arr4=np.array([2,4,9,1])
    arr4+=10
    print(arr4)
#broadcasting()

#Fancy indexing
def FancyIndexing():
    #boolean indexing
    #using mask to meet requirement
    mask=((arrK<0))
    arrK[mask]=0
    print(arrK)
FancyIndexing()
