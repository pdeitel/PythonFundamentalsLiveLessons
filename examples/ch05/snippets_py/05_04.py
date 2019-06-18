# Section 5.4 snippets
student_tuple = ('Amanda', [98, 85, 87])

first_name, grades = student_tuple

first_name

grades

first, second = 'hi'

print(f'{first}  {second}')

number1, number2, number3 = [2, 3, 5]

print(f'{number1}  {number2}  {number3}')

number1, number2, number3 = range(10, 40, 10)

print(f'{number1}  {number2}  {number3}')

# Swapping Values Via Packing and Unpacking
number1 = 99

number2 = 22

number1, number2 = (number2, number1)

print(f'number1 = {number1}; number2 = {number2}')

# Accessing Indices and Values Safely with Built-in Function enumerate
colors = ['red', 'orange', 'yellow']

list(enumerate(colors))

tuple(enumerate(colors))

for index, value in enumerate(colors):
    print(f'{index}: {value}')
    








##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
