# Section 5.15 snippets

# Finding the Minimum and Maximum Values Using a Key Function
'Red' < 'orange'

ord('R')

ord('o')

colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']

min(colors, key=lambda s: s.lower())

max(colors, key=lambda s: s.lower())

# Iterating Backwards Through a Sequence
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

reversed_numbers = [item ** 2 for item in reversed(numbers)]

reversed_numbers

# Combining Iterables into Tuples of Corresponding Elements
names = ['Bob', 'Sue', 'Amanda']

grade_point_averages = [3.5, 4.0, 3.75] 

for name, gpa in zip(names, grade_point_averages):
    print(f'Name={name}; GPA={gpa}')


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
