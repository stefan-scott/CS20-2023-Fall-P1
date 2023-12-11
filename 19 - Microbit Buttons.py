# Microbit Button and Images
# Mr. Scott
# Dec 11, 2023
# How to read button presses + using built-in images
import microbit, time  #cs20-microbitio

# Microbit Slideshow: 3 images, 1 second each
microbit.display.show(microbit.Image.XMAS)
time.sleep(1)

microbit.display.show(microbit.Image.ROLLERSKATE)
time.sleep(1)

microbit.display.show(microbit.Image.DUCK)
time.sleep(1)

# Image Animation
clock_images = [microbit.Image.CLOCK1,
                microbit.Image.CLOCK2,
                microbit.Image.CLOCK3,
                microbit.Image.CLOCK4,
                microbit.Image.CLOCK5,
                microbit.Image.CLOCK6,
                microbit.Image.CLOCK7,
                microbit.Image.CLOCK8,
                microbit.Image.CLOCK9,
                microbit.Image.CLOCK10,
                microbit.Image.CLOCK11,
                microbit.Image.CLOCK12]

current_index = 0 #the index of image to show
delay_amount = 0.2 #seconds to wait b/w each frame

while True:
    microbit.display.show(clock_images[current_index])
    current_index += 1
    #0 1 2 3 4 5 6 7 8 9 10 11 no no no
    if current_index > 11:
        current_index = 0
    
    time.sleep(delay_amount)

# TO-DO:
#
# Re-attempt the functions practice quiz
#
# Add button presses to increase/decrease
# the animation playback speed (modify the delay)




# USING THE BUTTONS

# button_a_count = 0
# button_b_count = 0 
# # Button Usage
# 
# while True:
#     print(f"a: {button_a_count} \t b: {button_b_count}")
#     if microbit.button_a.is_pressed():  #if button is held...
#         button_a_count += 1  # button_a_count = button_a_count + 1
#     if microbit.button_b.was_pressed(): #was it pressed since last check
#         button_b_count += 1
#     
    
        
    
    
    
    