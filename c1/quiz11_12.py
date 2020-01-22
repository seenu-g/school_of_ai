# What is the value of the square-root of sum of the dot product between y and the square-root of x?
import numpy as np
def quiz11() :

    x = np.array([[1,2],[3,4]])
    y = np.array([[5,6],[7,8]])

    v = np.array([9,10])
    w = np.array([11, 12])

    # Inner product of vectors; both produce 219
    print(v.dot(w)) # answer is scalar # as it is inner product of vectors
    print(np.dot(v, w)) #same as above.

    # Matrix / vector product; both produce the rank 1 array [29 67]
    #print(x.dot(v))
    #print(np.dot(x, v))

    # Matrix / matrix product; both produce the rank 2 array
    print(x.dot(y))
    print(np.dot(x, y))
    
    print(np.sqrt([1,4,8]))
    
    print(np.sqrt(np.sum(y.dot(np.sqrt(x)))))

# What is the sum of all the elements of x and square-root of 
#                    (dot-product of 
 #                   (sum of each coloumn of x and sum of each row of x? 
def quiz12() :

    x = np.array([[1,2],[3,4]])
    print(x)
    print(np.sum(x))  # Compute sum of all elements; prints "10"
    print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
    print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"
    
    result1 =  np.sum(x) 
    result2 =  np.sqrt(np.dot(np.sum(x, axis=0),np.sum(x, axis=1)))
    print (result1 + result2)

def main():
    #quiz11()
    quiz12()
    
# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()