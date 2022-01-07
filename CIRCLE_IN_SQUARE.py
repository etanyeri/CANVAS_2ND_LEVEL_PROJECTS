
""" This code is that asks a user for a radius value and 
then draws a blue circle inside a red square
in the center of the canvas."""


radius=int(input('What radius should the circle be?:')) 


def makesquare():
    color('red')
    begin_fill()
    for i in range(4):
        forward(2*radius)
        left(90)
    end_fill()
    
penup()
backward(radius)
pendown()

makesquare()

pendown()
forward(radius) # make a circle inside a square
penup()
color('blue')
begin_fill()
circle(radius)
end_fill()