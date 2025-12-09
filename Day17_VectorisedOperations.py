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
    '''
    Arithmetic Ufuncs:
1. np.add: 
2. np.subtract
3. np.multiply
4. np.divide
5. np.floor_divide
6. np.power
7. np.mod
8. np.abs: Element-wise absolute value.
9. np.negative: Element-wise negation.

Mathematical Ufuncs:
1. np.sqrt: Square root of each element.
2. np.exp: Exponential function (e^x) for each element.
3. np.log, np.log10, np.log2: Natural logarithm, base-10 logarithm, and base-2 logarithm, respectively.
4. np.sin, np.cos, np.tan: Trigonometric functions.
5. np.arcsin, np.arccos, np.arctan: Inverse trigonometric functions.
6. np.sinh, np.cosh, np.tanh: Hyperbolic trigonometric functions.
7. np.arcsinh, np.arccosh, np.arctanh: Inverse hyperbolic trigonometric functions.

Comparative Ufuncs:
1. np.greater, np.greater_equal: Element-wise comparison for greater than and greater than or equal to.
2. np.less, np.less_equal: Element-wise comparison for less than and less than or equal to.
3. np.equal, np.not_equal: Element-wise comparison for equality and inequality.

Logical Ufuncs:
1. np.logical_and, np.logical_or, np.logical_xor: Element-wise logical operations.
2. np.logical_not: Element-wise logical NOT operation.

Bitwise Ufuncs:
1. np.bitwise_and, np.bitwise_or, np.bitwise_xor: Element-wise bitwise operations.
2. np.invert: Element-wise bitwise NOT operation (bitwise inversion).

Rounding and Truncation Ufuncs:
1. np.round: Round elements to the nearest integer or specified number of decimals.
2. np.floor: Round elements down to the nearest integer.
3. np.ceil: Round elements up to the nearest integer.
4. np.trunc: Truncate decimal values, keeping only the integer part.

Statistical Ufuncs:
1. np.mean, np.median: Compute the mean and median of array elements.
2. np.min, np.max: Finds the minimum and maximum values present in an array.
3. np.std, np.var: Calculate the standard deviation and variance of elements.

Special Ufuncs:
1. np.isnan: Check for NaN (Not-a-Number) values in an array.
2. np.isinf: Check for infinity values in an array.
3. np.isfinite: Check for finite values in an array.
4. np.unique: Find unique elements in an array.

Trigonometric and Hyperbolic Ufuncs:
1. np.deg2rad, np.rad2deg: Convert between degrees and radians.
2. np.hypot: Calculate the hypotenuse of right triangles.
    '''
#universalFunctions()

def vectorising():
    #vectorising in numpy is performing calculations in
    #  the entire array without
    #loops
    #using vectorision methods you can peform addition,
    # subtractiion ...etc on arrays
    #even logical operations 

    #example
    x=np.array([2,3,4,9])
    y=(x%2==0)
    #print(y)

    #matrix operation using vectorisation
    np.divide(a,b)
    np.abs(a,b)
    #example
    a=np.array([[2,3],[3,1]])
    b=np.array([[4,1],[2,1]])
    #matrix opration by the keyword dot
    #dotting a vector
    #a⋅b= a1b1 + a2b2
    #this will be in 2*2 shape in a form of ([2][3][3][1])*([4][1] [2][1])
    results=np.dot(a,b)
    print(results)

vectorising()
#order of arrays