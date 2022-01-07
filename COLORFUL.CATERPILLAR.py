

""" This code is to draw a colorful caterpillar"""

def circles(color_choise):
    pendown()
    color(color_choise)
    begin_fill()
    circle(20)
    end_fill()
    penup()
    forward(40)
    pendown()
   
    
    
penup()
setposition(-150,0)

for i in range(2):
    # Caterpillar have 8 body circles.
    
    color_choise= 'blue'. # Have circles that alternate between 4 different colors
    circles(color_choise)
    
    color_choise='green'
    circles(color_choise)
    
    color_choise='yellow'
    circles(color_choise)
    
    color_choise='red'
    circles(color_choise)