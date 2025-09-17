import numpy as np
def ElementWiseOperations():
    #we can perform arthimetic operations on arrays
    #consider two arrays
    a=np.array([26,32,12,17])
    b=np.array([3,4,2,3])
    #performing various operations on them

    #addition
    print(f"the addition of {a} and {b} is \n{(np.add(a,b))}\n")

    #subtraction
    print(f"The subtraction of {a} and {b} is\n {(np.subtract(a,b))}\n")

    #multiplication
    print(f"The multiplication of {a} anf {b} is \n{(np.multiply(a,b))}\n")

    #division
    print(f"The division of {a} and {b} is \n{(np.divide(a,b))}\n")

    #exponatio(power)
    print(f"{a} raised to power {b} is\n {(np.power(a,b))}\n")

    #modulus
    print(f"the modulus of {a} and {b} is \n{(np.mod(a,b))}\n")
#ElementWiseOperations()

def universalFunctions():
    #we will use universal function with the keyword
    #frompyfunc()

    #vectorising is another way of using the function
    #by the numpy array

    #numpy summations
    #1.cummulative summation
    arr3=np.array([2,5,18,32])
    arr4=np.cumsum(arr3)
    print(arr4)
universalFunctions()
