"""This program reports whether or not someone is eligible
to run for president in the U.S.

You are eligible to run for president! if they have the following credentials:
They are at least 35 years old
They were born in the U.S.
They have been a resident for at least 14 years"""


age=int(input('What is your age?: '))

born_Us=input('Were you born in US? (YES/NO): ')

year_residency=int(input('How long have you been resident?: '))

YES='yes'
NO='no'

if age>35 and born_Us==YES and year_residency>=14:
    print('You are eligible to run for president!')
    
else:
    print('You are not eligible to run for president.')