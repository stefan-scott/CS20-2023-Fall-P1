# user input
h_3pt = int(input("Huskies 3 pointers? "))
h_2pt = int(input("Huskies 2 pointers? "))
h_1pt = int(input("Huskies 1 pointers? "))
huskies_score = h_3pt*3 + h_2pt*2 + h_1pt*1

c_3pt = int(input("Cougars 3 pointers? "))
c_2pt = int(input("Cougars 2 pointers? "))
c_1pt = int(input("Cougars 1 pointers? "))
cougars_score = c_3pt*3 + c_2pt*2 + c_1pt*1

# Determine the Winner - 3 CASES
if huskies_score > cougars_score:
    print(f"Huskies win {huskies_score} to {cougars_score}")
elif cougars_score > huskies_score:
    print(f"Cougars win {cougars_score} to {huskies_score}")
else:
    print(f"Tie Game! {huskies_score} to {cougars_score}")
    
# Determining if it's a high or low scoring game
if huskies_score > 70 and cougars_score > 70:
    print("HIGH SCORING GAME")
else:
    print("LOW SCORING GAME")
