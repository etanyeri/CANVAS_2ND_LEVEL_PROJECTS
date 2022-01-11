
""" This code is to draw a dartboard using the value of i 
instead of an outside variable."""


speed(10)

radius=25  # Has the center circle placed
           # in the middle of the canvas with a radius of 25

for i in range(radius,120,25):
    circle(i)
    right(90)
    penup()
    forward(25)
    left(90)
    radius=radius+25 #  that each increase in radius by 25 pixels
    pendown()