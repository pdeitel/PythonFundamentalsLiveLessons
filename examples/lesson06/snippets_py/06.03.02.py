# Section 6.3.2 snippets

# Union 
{1, 3, 5} | {2, 3, 4}

{1, 3, 5}.union([20, 20, 3, 40, 40])

# Intersection 
{1, 3, 5} & {2, 3, 4}

{1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4])

# Difference 
{1, 3, 5} - {2, 3, 4}

{1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4])

# Symmetric Difference 
{1, 3, 5} ^ {2, 3, 4}

{1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4])

# Disjoint
{1, 3, 5}.isdisjoint({2, 4, 6})

{1, 3, 5}.isdisjoint({4, 6, 1})




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
