# Looping by item vs Looping by index

transport = ["airplane", "bus", "car", "dogsled", "elevator"]
#                0         1      2        3         4
#                                -3        -2         -1
# len(transport) → 5   range()  [0,1,2,3,4]

# LOOP BY ITEM.  Easy to code, but we don't have any info
# about *where* the item resides in the list.
for method in transport:
    print(f"You can travel by: {method}")

# LOOP BY INDEX.  A little longer to code, but we can still
# access each item, and we also know their list positions
for index in range(len(transport)):
    item = transport[index]
    print(f"The item at {index}: {item}")

# Exercise: Write a method to convert a string to aLtErNaTiNg case
def alt_case(str):
    # given a string of text, return the same text where
    # the case alternatives from lower to higher and so on,
    # changing at each character.    .upper()  .lower()
    # Even Char Pos:  lower   Odd Char Pos: upper
    # n % 2 == 1 For all odd numbers     n%2==0  for all even numbers 
    result = ""   #accumulator pattern
    for index in range(len(str)):
        letter = str[index]
        if index % 2 == 0:  #EVEN index
            result += letter.lower()
        else: #ODD index
            result += letter.upper()
    return result

print(alt_case("Here is some TEXT TO TRY"))
    
    
    
    
