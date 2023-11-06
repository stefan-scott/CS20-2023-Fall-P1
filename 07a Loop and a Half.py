# Loop and a Half Demo
# Mr. Scott
# Nov 6, 2023
# "Forever Loops" + break and continue

while True:  # a conditional loop, but the condition is fixed to True
    choice = input("would you like to stop? [yes/no]: ") #YES Yes yes
    if choice.lower() == "yes":
        confirm = input("you sure? [yes/no]: ")
        if confirm.upper() == "YES":
            break  
        else:  #if no confirmation, just restart the loop
            continue
    print("let's try this again...")
    