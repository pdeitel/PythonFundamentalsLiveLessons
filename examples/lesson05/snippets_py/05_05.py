# Section 5.5 snippets

# Specifying a Slice with Starting and Ending Indices
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

numbers[2:6]

# Specifying a Slice with Only an Ending Index
numbers[:6]

numbers[0:6]

# Specifying a Slice with Only a Starting Index
numbers[6:]

numbers[6:len(numbers)]

# Specifying a Slice with No Indices
numbers[:]

# Slicing with Steps
numbers[::2]

# Slicing with Negative Indices and Steps
numbers[::-1]

numbers[-1:-9:-1]

# Modifying Lists Via Slices
numbers[0:3] = ['two', 'three', 'five']

numbers

numbers[0:3] = []

numbers

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

numbers[::2] = [100, 100, 100, 100]

numbers

id(numbers)

numbers[:] = []

numbers

id(numbers)

numbers = []

numbers

id(numbers)



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
