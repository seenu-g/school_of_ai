#What should be the value of rng, such that print(sum(nums)) prints 48?

def quiz4(input) :
    rng = input
    nums = list(range(rng))     # range is a built-in function that creates a list of integers
    print(nums)               # Prints "[0, 1, 2, 3, 4]"
    print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
    print(nums[2:])           # Get a slice from index 2 to the end; prints "[2, 3, 4]"
    print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
    print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
    print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
    nums[2:4] = [8, 9]        # Assign a new sublist to a slice
    print(nums)               # Prints "[0, 1, 8, 9, 4]"
    print(sum(nums))

def main():
    quiz4(9)
    
# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()