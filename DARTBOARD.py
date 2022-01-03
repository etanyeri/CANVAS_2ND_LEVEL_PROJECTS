

""" Write a program that draws a dartboard"""


# circle(radius)
# circle(circle_radius)   
# instead of giving an integer value to radius,
# assigned a variable to circle() as a radius value



def manycircles():
    circle_radius=25      # Has the center circle placed in the middle  
    circle(circle_radius)    #of the canvas with a radius of 25


    for i in range(4): # Consists of 4 concentric circles
        penup()
        right(90)
        forward(25)
        left(90)
        pendown()
        circle_radius=circle_radius+25
        circle(circle_radius)
        
manycircles()