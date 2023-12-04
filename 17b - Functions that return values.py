# Functions that return Values (fruitful functions)
# Mr. Scott
# Dec 4, 2023

# Some built-in functions that return values
import math

print(abs(5))   #absolute value
print(abs(-5))

print(math.pow(2,3)) # 2^3  (2x2x2)   2**3
print(math.pow(7,2)) # 7^2  (7x7)

print(max(7,11))  #returns the largest value
print(max(4, 1, 17, 2))

# Write a function to calculate the SQUARE of an object
def custom_square(base):
    result = base * base
    return result #BETTER DESIGN -> allows me to use the data in multiple ways

#3 things we would use a returned value for:
#1. Store in a variable
square_of_five = custom_square(5)

#2. print it out
print(custom_square(10))

#3. Use return value as an INPUT for another method
print(max(custom_square(10), custom_square(5)))
    
    
    
    
    