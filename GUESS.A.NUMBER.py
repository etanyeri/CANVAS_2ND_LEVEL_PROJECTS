
"""This code that will check if a user guessed the secret number."""


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
    

#  When they guess the secret number, a checkmark will appear 
# and the user will stop being asked to guess.


secret_number= 'n'
while True:
    user_number=input('Enter a guess number 1-10: ')
    if user_number == secret_number:
        draw_checkmark()
        pass