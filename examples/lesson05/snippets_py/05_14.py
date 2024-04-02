# Section 5.14 snippets

# Filtering a Sequence’s Values with the Built-In filter Function
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def is_odd(x):
    """Returns True only if x is odd."""
    return x % 2 != 0

list(filter(is_odd, numbers))

[item for item in numbers if is_odd(item)]

# Using a lambda Rather than a Function 
list(filter(lambda x: x % 2 != 0, numbers))

# Mapping a Sequence’s Values to New Values
numbers

list(map(lambda x: x ** 2, numbers))

[item ** 2 for item in numbers]

# Combining filter and map
list(map(lambda x: x ** 2, 
         filter(lambda x: x % 2 != 0, numbers)))

[x ** 2 for x in numbers if x % 2 != 0]




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
