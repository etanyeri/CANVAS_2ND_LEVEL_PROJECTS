"""This code that will check if a user guessed the secret number and 
tell the user if their guess was high or low.."""



# This function draws a checkmark sign in the middle of the canvas   
def draw_checkmark():   
    pensize(10)
    color('green')
    left(60)
    forward(90)
    backward(90)
    left(75)
    forward(40)
    backward(40)
 
 
def draw_up_arrow():
    pensize(10)
    color('green')
    left(90)
    forward(120)
    left(130)
    forward(40)
    backward(40)
    left(90)
    forward(40)
    left(50)
    clear()
    
def draw_down_arrow():
    pensize(10)
    color('green')
    left(90)
    forward(120)
    backward(120)
    left(50)
    forward(40)
    backward(40)
    right(90)
    forward(40)
    right(50)
    clear()
  
   
    


number = 6
while True:
    guess = int(input('Enter a number between 1-10: '))
    if guess < number:
        draw_up_arrow()
    elif guess > number:
        draw_down_arrow()
    else:
        draw_checkmark()
        break
        
        
        