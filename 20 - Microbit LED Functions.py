# Microbit LED Functions
# Mr. Scott
# Dec 13, 2023
# Some new helper methods for working with LED matrix

import microbit, time, random

# list to represent the 5x5 grid on the micro:bit
grid = [ [5, 0, 0, 0, 0],
         [0, 5, 0, 0, 0],
         [0, 0, 5, 0, 0],
         [0, 0, 0, 5, 0],
         [0, 0, 0, 0, 5] ]

def show_grid():
    # convert our 2D list into a properly
    # formatted string (to be an Image)
    result = ""
    for row in grid:
        for pixel in row:
            result += str(pixel)
        result += ":"
    result = result[0:-1] #remove trailing :
    print(result) #may want to comment out
    microbit.display.show(microbit.Image(result))

def set_pixel(x,y,intensity):
    #set a pixel at (x,y) to brightness: intensity(0-9)
    grid[y][x] = intensity
    show_grid()
    
def queue_pixel(x,y,intensity):
    # queue a change for a particular x,y pixel
    grid[y][x] = intensity

def plot(x,y):
    #turn on pixel at (x,y) to full brightness
    set_pixel(x,y,9)

def unplot(x,y):
    #turn off a pixel at (x,y)
    set_pixel(x,y,0)
    
def print_grid():
    #print out grid in an easy-to-read format
    for row in grid:
        print(row)
        
# Main Code Starts Here

def set_all(intensity):
    # fill all pixels to level "intensity"
    for x in range(5):  #x → 0, 1, 2, 3, 4
        for y in range(5): #y → 0, 1, 2, 3, 4
            queue_pixel(x,y,intensity)
    show_grid()

# Fading Effect - Animation
for cycles in range(3):
    for brightness in range(10):  #0-9
        set_all(brightness)
        time.sleep(0.05)

    for brightness in range(8,0,-1):   #8-1
        set_all(brightness)
        time.sleep(0.05)
        
# Game Mechanics - driving a player around
set_all(0) #clear the screen
player_x = 2
player_y = 4

plot(player_x, player_y)

while True:
    if microbit.button_a.was_pressed():
        if player_x > 0:  #if there's room to move
            unplot(player_x, player_y)
            player_x = player_x - 1
            plot(player_x, player_y)
            
    if microbit.button_b.was_pressed():
        if player_x < 4: #if there's room to move
            unplot(player_x, player_y)
            player_x += 1
            plot(player_x, player_y)
    
# Recap: Built-in vs Custom
# microbit.display.show(microbit.Image.HAPPY)   #BUILT-IN
# 
# test_image = microbit.Image("00000:11111:22222:33333:44444")
# microbit.display.show(test_image)