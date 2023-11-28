#Exercise 1
# Create a function Create a function called coin_flip() that randomly
# returns “heads” or “tails”. Call the function 100 times, and track
# how many times the function returns “tails”. Display this amount. 


import random   #random.randint()   random.uniform()   random.choice()
NUM_FLIPS = 2000  #Constant.  word-number substitution

def coin_flip():
    # uses random probability to return either "heads" or "tails"
    chance = random.randint(1,2)  #1 or a 2
    if chance == 1:
        return "heads"
    else:
        return "tails"
    
def coin_flip_b():
    # using random selection from a list, return either "heads" or "tails"
    sides = ["heads", "tails"]
    return random.choice(sides)
    
# Run an experiment. Flip a coin NUM_FLIPS times and report the results
num_tails = 0
for i in range(NUM_FLIPS):  #repeat NUM_FLIPS
    if coin_flip() == "tails":
        num_tails += 1
print(f"On {NUM_FLIPS} rolls, we got tails {num_tails} times.")





    
    