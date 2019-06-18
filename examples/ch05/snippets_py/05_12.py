# Section 5.12 snippets

list1 = []

for item in range(1, 6):
    list1.append(item)
    
list1

# Using a List Comprehension to Create a List of Integers
list2 = [item for item in range(1, 6)]

list2

# Mapping: Performing Operations in a List Comprehension’s Expression
list3 = [item ** 3 for item in range(1, 6)]

list3

# Filtering: List Comprehensions with if Clauses 
list4 = [item for item in range(1, 11) if item % 2 == 0]

list4


# List Comprehension That Processes Another List’s Elements 
colors = ['red', 'orange', 'yellow', 'green', 'blue']

colors2 = [item.upper() for item in colors]

colors2

colors


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
