

""" This code is to draw a dartboard and color in each circle 
of the dartboard with a different color"""

def drawcircles():
    radius=25        #Has the center circle in the middle of the canvas with a radius of 25
    circle(radius)   # total number of circles will be 4.
    for i in range(3):
            penup()
            right(90)
            forward(25)
            left(90)
            pendown()
            radius = radius+25
            circle(radius)
        
speed(3) 

drawcircles()     
        
circle_radius=100 # each will decrease in radius by 25 pixels

for i in range(4):
    color_choice=input('What color is the circle should be?:' )
    color(color_choice)
    begin_fill()
    circle(circle_radius)
    end_fill()
    circle_radius=circle_radius-25 
    left(90)
    forward(25)
    right(90)