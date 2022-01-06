

"""This code is a program that has Tracy draw 
a square in each corner of the canvas."""


def asquare():
 for i in range(4):
    square_length= int(input('what length should the line be:' ))
    pendown()
    forward(square_length)
    left(90)
    
    
speed(9)    
penup()
setposition(-200,-200)
square_length= int(input('what length should the line be:' ))
asquare()



penup()
setposition(150,-200)
square_length= int(input('what length should the line be:' ))
asquare()

penup()
setposition(150,150)
square_length= int(input('what length should the line be:' ))
asquare()

penup()
setposition(-200,150)
square_length= int(input('what length should the line be:' ))
asquare()