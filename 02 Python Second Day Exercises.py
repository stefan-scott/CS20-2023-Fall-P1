# I/O Exercises
# Mr. Scott
# October 30, 2023
# input(),  print(),  type conversions

# Output - printing to the screen [Simple]
print("Hello")   
text = "CS20"    
print(text)

# Output - printing multiple things
print("Hello," + text)  # + can join two strings (no formatting)
print("Hello," , text , "!" )  #, in print() joins with spaces between

# Output - joining strings and numbers
num = 45
print("best number:" , num) # , can mix types easily
print("best number: " + str(num)) # ERROR. Can't use '+' for STR and INT


# Input - reading in values and storing in variables
number_one = input("Enter a number: ") #input always gives STRING
number_two = input("Enter a second number: ")

# If needed, convert to a numeric data type
number_one = int(number_one)
number_two = int(number_two)
# INT        INT        INT
result = number_one + number_two

#          STR           INT   
print("The sum is: " + str(result))



