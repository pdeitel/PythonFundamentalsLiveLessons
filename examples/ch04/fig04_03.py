# fig04_03.py
"""Function-call stack demonstration script."""

def main():
    result = square(7)  # square's stack frame pushed onto stack here
    print('square(7):', result)  
    # main's stack frame is popped here

def square(number):
    return number ** 2  # square's stack frame is popped here

main()  # execution begins here
# when main returns, the script terminates here

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
