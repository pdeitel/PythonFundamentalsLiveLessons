# Section 5.16 Self Check snippets

# Exercise 4
t = [[10, 7, 3], [20, 4, 17]]

total = 0

items = 0

for row in t:
    for item in row:
        total += item
        items += 1     

total / items

total = 0

items = 0

for row in t:
    total += sum(row)
    items += len(row)

total / items



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
