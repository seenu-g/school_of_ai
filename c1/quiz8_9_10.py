

import numpy as np
#What should a[0] be set equal to such that print(sum(sum(a)*sum(b))) prints 420?

def quiz8(input) :
    a = np.array([1, 2, 3])   # Create a rank 1 array
    print(type(a))            # Prints "<class 'numpy.ndarray'>"
    print(a.shape)            # Prints "(3,)"
    print(a[0], a[1], a[2])   # Prints "1 2 3"
    a[0] = input                # Change an element of the array
    print(a)                  # Prints "[5, 2, 3]"
    
    b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
    print(b.shape)                     # Prints "(2, 3)"
    print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
    print(sum(a))
    print(sum(b))
    print(sum(sum(a)*sum(b)))

#Is it guaranteed that print(np.prod(e)) will always be less than 1
    #Return random floats in the half-open interval [0.0, 1.0).
    #[0,1) means greater than or equal to 0 and less than 1.
    # multiply 2 floats in half-open interval [0.0, 1.0).
def quiz9() :
    a = np.zeros((2,2))   # Create an array of all zeros
    print(a)              # Prints "[[ 0.  0.]
                          #          [ 0.  0.]]"

    b = np.ones((1,2))    # Create an array of all ones
    print(b)              # Prints "[[ 1.  1.]]"

    c = np.full((2,2), 7)  # Create a constant array
    print(c)               # Prints "[[ 7.  7.]
                           #          [ 7.  7.]]"

    d = np.eye(2)         # Create a 2x2 identity matrix
    print(d)              # Prints "[[ 1.  0.]
                          #          [ 0.  1.]]"

    e = np.random.random((2,2))  # Create an array filled with random values
    print(e)                     # Might print "[[ 0.91940167  0.08143941]
                                 #               [ 0.68744134  0.87236687]]"
    print(np.prod(e))
    #Return the product of array elements over a given axis.

#At which index of a, 99 values is stored? See quiz for options.
def quiz10() :
    a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
    a[0, 0] = 4
    print(a)
    
    b = a[:2, 1:3]
    print (b)
    print(a[0, 1])   # Prints "2"
    b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
    print(a[0, 1])   # Prints "77"
    print(a)
    
    c = a[:1, 2:4]
    print(c)
    c[0, 0] = 99
    print (a)
    print(a[0,2]) # prints 99

def main():
    #quiz8(15)
    #quiz9()
    quiz10()
# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()