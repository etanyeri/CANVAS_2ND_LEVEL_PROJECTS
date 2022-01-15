


""" This program is to draw a smiley face"""

# After making yellow circle, define a function to make a mouth
def makemouth():
    left(180)
    forward(35)
    right(90)
    forward(60)
    right(180)
    pendown()
    color('black')
    pensize(5)
    circle(40,180)

# define a function to make eyes
def makeeye():
    penup()
    forward(35)
    left(90)
    forward(15)
    pendown()
    color('black')
    begin_fill()
    circle(3)
    end_fill()
    penup()
    forward(45)
    pendown()
    color('black')
    begin_fill()
    circle(3)
    end_fill()
    
    
# Ask the user to enter “Yes” if they are happy. 
happy= input('Are you happy? : ')

if happy=='yes':
    color('yellow')
    begin_fill()
    circle(70)
    end_fill()
    makemouth()
    makeeye()
    penup()
    forward(60)