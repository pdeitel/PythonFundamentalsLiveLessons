# Section 5.16 snippets

# Creating a Two-Dimensional List
a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

# Illustrating a Two-Dimensional List

# Identifying the Elements in a Two-Dimensional List
for row in a:
    for item in row:
        print(item, end=' ')
    print()

# How the Nested Loops Execute
for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}]={item} ', end=' ')
    print()







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
