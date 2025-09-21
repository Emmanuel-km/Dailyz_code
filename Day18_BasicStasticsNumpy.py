import numpy as np
def Aggrigates():
    #sum
    #Syntax: numpy.sum(arr, axis, dtype, out): 
    #the axis value 1 sums up the row
    #the axis value 0 sums up the column(initial)
    x=np.array([[1,2,3],[3,2,5]])
    y=np.array([[2,2,1],[1,2,4]])
    a=np.array([2,4,1,3,4,6,1,2,4,5])

    #summing up the row 
    z=np.sum((x,y),axis=0)
    print(f"\n\n\nthe sum of\n{x} \nand\n {y} \nalong axis 0 is {z}\n\n\n")

    #summing up in a column
    z=np.sum((x,y),axis=1)
    print(f"the sum of\n{x} \nand \n{y} \nalong axis 1 is {z}\n\n\n")
    #summing up
    z=np.sum(a)
    print(f"the sum of{(a)} is {z}\n\n")
    #finding average

    z=np.average((x,y),axis=0)
    print(f"the average of \n{x} \nand\n{y}\n in the axis 0 is {z} \n\n\n")
    #print(z)

    #along the axis 1
    z=np.average((x,y),axis=1)
    print(f"the average of \n{x} \nand\n{y}\n in the axis 1 is {z} \n\n\n")

    #in a 1-d array

    z=np.average(a)
    print(f"the average of {a} is {z}\n\n\n")
    
    
    #finding median
    z=np.median((x,y),axis=0)
    print(f"the median of\n{x}\nand\n{y}\n along axis 0 is \n{z}\n\n\n")
    
    #along axis 1
    z=np.median((x,y),axis=1)
    print(f"the median of\n{x}\nand\n{y}\n along axis 1 is \n{z}\n\n\n")

    z=np.median(a)
    print(f"The median of \n{a}\n is {z} \n\n\n")

Aggrigates()