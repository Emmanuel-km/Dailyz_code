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
ElementWiseOperations()