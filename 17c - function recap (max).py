# Functions Review (parameters + return)
# Mr. Scott
# Dec 5, 2023

def my_max(a, b, c):
    # given 3 numbers (a,b,c)
    # return the value of the largest
    if a > b:  # largest must be a or c
        if a > c:
            return a
        else:
            return c
    else:      # largest must be b or c
        if b > c:
            return b
        else:
            return c
    
print (my_max(10, 100, 5))   

#print( min(10, 100, 1000) )
