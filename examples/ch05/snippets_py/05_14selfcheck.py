# Section 5.14 Self Check snippets

# Exercise 3
numbers = list(range(1, 16))

numbers

list(filter(lambda x: x % 2 == 0, numbers))

list(map(lambda x: x ** 2, numbers))

list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# Exercise 4
fahrenheit = [41, 32, 212]

list(map(lambda x: (x, (x - 32) * 5 / 9), fahrenheit)) 



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
