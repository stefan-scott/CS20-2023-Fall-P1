# Try Except Demo
# Mr. Scott
# Nov 6, 2023
# Gracefully handling exceptions...no more crashing!


#          0    1   2
my_list = [88, 44, "Twenty Two"]  # NOTHING CAN CAUSE A CRASH...
while True:
    try:
        index = int(input("enter an index: "))  #STR→INT Conversion..if str is not a num
                                                #ValueError
        chosen_number = my_list[index]  # Accessing data from a list:
                                        #IndexError  (if index is invalid)
        print("choice: " + chosen_number)  #Strings can only be joined to strings
        break                               #TypeError
    except ValueError:
        print("Value Error")
    except IndexError:
        print("Index Error")
    except TypeError:
        print("Type Error")

# except: #what happens if we run into an error
#     print("That was some sort of exception!")

print("But the program can continue...")




