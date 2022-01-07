
"""This program is to draw a snowman colored with gray."""


def makesnowman(sm_radius):
 for i in range(3): # Is made of three gray circles
    color('grey')
    begin_fill()
    circle(sm_radius) #The first one has a radius of 100
    end_fill()
    left(90)
    forward(2*sm_radius)
    right(90)
    sm_radius=sm_radius/2 # The middle has a radius of 50
    
sm_radius=int(input('What should be the sm radius? (0-160): '))

penup()
setposition(0,-200)
pendown()
makesnowman(sm_radius)