# Section 4.15 snippets

# Built-In Function id and Object Identities 
x = 7

id(x)

# Passing an Object to a Function 
def cube(number):
    print('id(number):', id(number))
    return number ** 3

cube(x)

# Testing Object Identities with the is Operator 
def cube(number):
    print('number is x:', number is x)  # x is a global variable
    return number ** 3

cube(x)

# Immutable Objects as Arguments
def cube(number):
    print('id(number) before modifying number:', id(number))
    number **= 3
    print('id(number) after modifying number:', id(number))
    return number

cube(x)

print(f'x = {x}; id(x) = {id(x)}')

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
