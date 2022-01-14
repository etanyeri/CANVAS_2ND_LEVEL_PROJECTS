


""" This code is to draw a representation of your
phone signal using the value of i!"""


for i in range(10,51,10): # Has 5 bars that are each 10 pixels wide
#Increases each bar’s height by 10 pixels, with the tallest bar being 50
    forward(10) # Makes the first bar 10 pixels tall
    left(90)
    forward(i)
    left(90)
    forward(10)
    left(90)
    forward(i)
    left(90)
    penup()
    forward(25)
    pendown()