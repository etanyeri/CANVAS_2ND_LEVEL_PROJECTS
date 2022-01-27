

""" Write a program that draws a happy or sad face based
on the users mood."""


# After making yellow circle, define a function to make a happy mouth

def make_happy_mouth():
    left(90)
    forward(15)
    left(90)
    forward(40)
    right(90)
    forward(60)
    right(180)
    pendown()
    color('black')
    pensize(5)
    circle(40,180)
    
# After making yellow circle, define a function to make a sad mouth
def make_sad_mouth():
    left(90)
    forward(45)
    right(90)
    forward(40)
    left(90)
    color('black')
    pensize(6)
    circle(40,180)

def make_happy_eye():
    penup()
    forward(30)
    left(90)
    forward(15)
    pendown()
    color('black')
    begin_fill()
    circle(4)
    end_fill()
    penup()
    forward(45)
    pendown()
    color('black')
    begin_fill()
    circle(4)
    end_fill()
    
def make_sad_eye():
    penup()
    right(180)
    forward(60)
    right(90)
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


# use a variable called happy to save user input.

happy= input('Are you happy? : ')

if happy=='yes':
    color('yellow')
    begin_fill()
    circle(70)
    end_fill()
    make_happy_mouth()
    make_happy_eye()
    penup()
    forward(60)
else:
    color('yellow')
    begin_fill()
    circle(70)
    end_fill()
    make_sad_mouth()
    make_sad_eye()
    
    