

"""This program will draw some symbols based on the user's rate 
between 1-10"""

# Write all functions to draw for a croos,a line and a checkmark

def draw_cross():
    pensize(10)
    color('red')
    left(45)
    for i in range(4):
        forward(50)
        backward(50)
        left(90)

def draw_minus():
    pensize(10)
    color('yellow')
    forward(50)
    backward(100)
    forward(50)
    
def draw_checkmark():   
    pensize(10)
    color('green')
    left(60)
    forward(90)
    backward(90)
    left(75)
    forward(40)
    backward(40)
    
## The user is asked to give a number. 
rating=int(input('Enter your rate from 1-10: '))

if 1<=rating<=4:
    draw_cross()
elif 5<=rating<=7:
    draw_minus()
else:
    draw_checkmark()