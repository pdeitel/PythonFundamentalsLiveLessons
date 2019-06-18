# Section 6.2.9 snippets
months = {'January': 1, 'February': 2, 'March': 3}

months2 = {number: name for name, number in months.items()}

months2

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}

grades2 = {k: sum(v) / len(v) for k, v in grades.items()}

grades2



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
