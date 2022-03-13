"""This program lets you know if you can have a key or not, 
based on your role at the school."""

your_role=input('What is your role at school?: ')
student='student'
teacher='teacher'
administrator='administrator'

if your_role==teacher or your_role==administrator:
    print('Administrators and teachers get keys!')
elif your_role==student:
    print('Students do not get keys!')
else:
    print('You can only be an administrator, teacher, or student!')