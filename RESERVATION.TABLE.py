""" This program asks the user for their name using input.
Have another string variable that represents the name on a particular
table reservation in a restaurant"""

user_name=input('What is your name?: ')
reservation_name='Mary'
print('Name: '+ user_name)

if user_name==reservation_name:
    print('Right this way!')
else:
    print("Sorry, we don't have a reservation under that name.")