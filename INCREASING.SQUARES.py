
"""This program will fill the canvas with squares centered 
around the middle of the screen. """



speed(5)
#The smallest square closest to the center 
#should have a length of 50 pixels.

length=50

#The largest square should have a length of 350 pixels.

while length<360:
    
    for i in range(4):
            forward(length)
            left(90)
    right(180)
    penup()
    forward(25)
    left(90)
    forward(25)
    left(90)
    pendown()
    
    #The squares should increase in length by 50 pixels with every iteration.
    length=length+50