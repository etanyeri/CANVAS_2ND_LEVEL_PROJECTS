

"""This program will draw 7 shapes"""


radius=20


penup()
setposition(0,-150)
pendown()

i=0
radius=20  #start with a radius of 20 circle
for i in range(7):
    pendown()
    circle(radius,360,i)
    penup
    setposition(0,-150)
    radius=radius+20 #increase in radius by 20 pixels each time
    i=i+1   # at the end of each loop, number of points will increment