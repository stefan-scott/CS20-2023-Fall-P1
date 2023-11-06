#Step One
name = input("name? ")

# Step Two...same, but then
# convert to a number...
amountCad = input("amount CAD? ")
amountCad = float(amountCad)

# Step Three
amountYen = amountCad * 110

# Step Four. Print out a summary
print("Hello, " + name + ". If you exchange " + str(amountCad) + " CAD")
print("you would receive " + str(amountYen) + " YEN.")

