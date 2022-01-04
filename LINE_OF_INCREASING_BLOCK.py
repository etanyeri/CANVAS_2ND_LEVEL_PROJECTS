

""" This code will draw a line of 5 blocks that increase in size."""

speed(8)
def makesquare(): #codes of making a square
    for i in range(4):
        pendown()
        forward(square_side)
        left(90)
        penup()

penup()
setposition(-150,0)
square_side=10  #The first block should have sides of length 10

"""space between each block that is as long as the block’s length before it"""

for i in range(5): 
    makesquare()
    forward(square_side*2)    
    square_side=square_side+10 #Each consecutive block should have its side length increase by 10