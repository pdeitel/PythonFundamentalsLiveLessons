# Section 5.7 snippets

# Passing an Entire List to a Function
def modify_elements(items):
    """"Multiplies all element values in items by 2."""
    for i in range(len(items)):
        items[i] *= 2

numbers = [10, 3, 7, 1, 9]

modify_elements(numbers)

numbers

# Passing a Tuple to a Function
numbers_tuple = (10, 20, 30)

numbers_tuple

modify_elements(numbers_tuple)


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
