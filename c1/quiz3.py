#What should be the value of "location" such that print(hw6[location]) prints 6?

hello = 'hello'    # String literals can use single quotes
world = "world"    # or double quotes; it does not matter.
print(hello)       # Prints "hello"
print(len(hello))  # String length; prints "5"
hw = hello + ' ' + world  # String concatenation
print(hw)  # prints "hello world"
hw6 = '%s %s %d' % (hello, world, 6)  # sprintf style string formatting
print(hw6)  # prints "hello world 6"

location = 0
print(hw6[location])