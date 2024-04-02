# Section 7.10 snippets

# Indexing with Two-Dimensional arrays
import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])
                   
grades

grades[0, 1]  # row 0, column 1

# Selecting a Subset of a Two-Dimensional array’s Rows
grades[1]

grades[0:2]

grades[[1, 3]]

# Selecting a Subset of a Two-Dimensional array’s Columns
grades[:, 0]

grades[:, 1:3]

grades[:, [0, 2]]

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
