# Section 5.9 snippets
# 5.9 Searching Sequences

# List Method index
numbers = [3, 7, 1, 4, 2, 8, 5, 6]

numbers.index(5)

# Specifying the Starting Index of a Search
numbers *= 2

numbers

numbers.index(5, 7)

# Specifying the Starting and Ending Indices of a Search
numbers.index(7, 0, 4)

# Operators in and not in
1000 in numbers

5 in numbers

1000 not in numbers

5 not in numbers

# Using Operator in to Prevent a ValueError
key = 1000

if key in numbers:
    print(f'found {key} at index {numbers.index(search_key)}')
else:
    print(f'{key} not found')
    

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
