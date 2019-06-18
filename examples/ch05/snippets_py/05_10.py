# Section 5.10 snippets

color_names = ['orange', 'yellow', 'green']

# Inserting an Element at a Specific List Index
color_names.insert(0, 'red')

color_names

# Adding an Element to the End of a List
color_names.append('blue')

color_names

# Adding All the Elements of a Sequence to the End of a List
color_names.extend(['indigo', 'violet'])

color_names

sample_list = []

s = 'abc'

sample_list.extend(s)

sample_list

t = (1, 2, 3)

sample_list.extend(t)

sample_list

sample_list.extend((4, 5, 6))  # note the extra parentheses

sample_list

# Removing the First Occurrence of an Element in a List 
color_names.remove('green')

color_names


# Emptying a List
color_names.clear()

color_names

# Counting the Number of Occurrences of an Item
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 
             1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

for i in range(1, 6):
    print(f'{i} appears {responses.count(i)} times in responses')
    
# Reversing a List’s Elements
color_names = ['red', 'orange', 'yellow', 'green', 'blue']

color_names.reverse()

color_names

# Copying a List
copied_list = color_names.copy()

copied_list




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
