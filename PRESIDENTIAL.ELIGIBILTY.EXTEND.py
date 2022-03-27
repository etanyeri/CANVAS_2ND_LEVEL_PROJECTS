"""Presidential eligibility program to include a notice to the user
that describes why they are not eligible to run."""


age=int(input('What is your age?: '))
print('Age:' + str(age))

born_Us=input('Were you born in US? (YES/NO): ')
print('Born in the U.S.? (Yes/No):' + born_Us)

year_residency=int(input('How long have you been resident?: '))
print('Years of Residency: ' + str(year_residency))

YES='yes'
NO='no'

if age<35 and born_Us==NO and year_residency<14:
    print("You are not eligible to run for president.")
    print('You are too young. You must be at least 35 years old.')
    print('You must be born in the U.S. to run for president')
    print('You have not been a resident for long enough.')
    
elif age<35 and born_Us==NO and year_residency>14:
    print("You are not eligible to run for president.")
    print('You are too young. You must be at least 35 years old.')
    print('You must be born in the U.S. to run for president')

elif age<35 and born_Us==YES and year_residency<14:
    print("You are not eligible to run for president.")
    print('You are too young. You must be at least 35 years old.')
    print('You have not been a resident for long enough.')
    
elif age<35 and born_Us==YES and year_residency>14:    
    print("You are not eligible to run for president.")
    print('You are too young. You must be at least 35 years old.')
    
elif age>35 and born_Us==NO and year_residency<14:
      print("You are not eligible to run for president.")
      print('You must be born in the U.S. to run for president')
      print('You have not been a resident for long enough.')
      
elif age>35 and born_Us==NO and year_residency>14:
     print("You are not eligible to run for president.")
     print('You must be born in the U.S. to run for president')
     
elif age>35 and born_Us==YES and year_residency<14:
     print("You are not eligible to run for president.")
     print('You have not been a resident for long enough.')
     
else:
     print('You are eligible to run for president!')