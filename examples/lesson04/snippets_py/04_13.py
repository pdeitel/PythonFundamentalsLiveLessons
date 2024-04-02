# Section 4.13 snippets

# Accessing a Global Variable from a Function 
x = 7

def access_global():
    print('x printed from access_global:', x)
    
access_global()

def try_to_modify_global():
    x = 3.5
    print('x printed from try_to_modify_global:', x)
    
try_to_modify_global()

x

def modify_global():
    global x;
    x = 'hello'
    print('x printed from modify_global:', x)
    
modify_global()

x

# Shadowing Functions
sum = 10 + 5

sum

sum([10, 5])

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
