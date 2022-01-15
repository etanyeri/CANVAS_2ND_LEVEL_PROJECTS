

"""This program is to draw a line of black and white squares."""


def asquare():
 for i in range(4):
    forward(20)
    left(90)
    
penup()
setposition(-150,0)
pendown()

# Draw 6 squares in a line in the middle of the canvas
# every other square filled in based on i value even or odd
i=0
for i in range(6):
  if i % 2 == 0:
      color('black')
      begin_fill()
      asquare()
      end_fill()
      i=i+1
  asquare()
  penup()
  forward(50)
  pendown()