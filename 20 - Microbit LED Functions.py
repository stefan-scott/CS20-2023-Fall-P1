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
    
    
    
# Recap: Built-in vs Custom
# microbit.display.show(microbit.Image.HAPPY)   #BUILT-IN
# 
# test_image = microbit.Image("00000:11111:22222:33333:44444")
# microbit.display.show(test_image)