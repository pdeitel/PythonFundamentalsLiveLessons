# Section 5.2 snippets

# Creating a List
c = [-45, 6, 0, 72, 1543]

c

# Accessing Elements of a List
c[0]

c[4]

# Determining a List’s Length 
len(c)

# Accessing Elements from the End of the List with Negative Indices
c[-1]

c[-5]

# Indices Must Be Integers or Integer Expressions
a = 1

b = 2

c[a + b]

# Lists Are Mutable
c[4] = 17

c

# Some Sequences Are Immutable
s = 'hello'

s[0]

s[0] = 'H'

# Attempting to Access a Nonexistent Element
c[100]

# Using List Elements in Expressions
c[0] + c[1] + c[2]

# Appending to a List with +=
a_list = []

for number in range(1, 6):
    a_list += [number]
    
a_list

letters = []

letters += 'Python'

letters

# Concatenating Lists with +
list1 = [10, 20, 30]

list2 = [40, 50]

concatenated_list = list1 + list2

concatenated_list

# Using for and range to Access List Indices and Values
for i in range(len(concatenated_list)):  
    print(f'{i}: {concatenated_list[i]}')

# Comparison Operators
a = [1, 2, 3]

b = [1, 2, 3]

c = [1, 2, 3, 4]

a == b

a == c

a < c

c >= b


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
