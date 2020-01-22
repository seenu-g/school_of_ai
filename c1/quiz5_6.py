#What should be the value of rng2, such that the code block above prints 91?
def sum_squares(input) :
    rng2 = input
    nums = range(rng2)
    squares = []
    for x in nums:
        squares.append(x ** 2)
    print(sum(squares))

#What is the sum of the two values to which rng3 can be set such that the output above is 364?
def sum_even_squares(input) :
    rng3 = input
    nums = range(rng3)
    even_squares = [x ** 2 for x in nums if x % 2 == 0]
    print(sum(even_squares))

def main():
    sum_squares(7)
    sum_even_squares(13)
    
# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()