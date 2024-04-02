# Section 7.13 snippets

# reshape vs. resize
import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90]])

grades

grades.reshape(1, 6)

grades

grades.resize(1, 6)

grades

# flatten vs. ravel
grades = np.array([[87, 96, 70], [100, 87, 90]])

grades

flattened = grades.flatten()

flattened

grades

flattened[0] = 100

flattened

grades

raveled = grades.ravel()

raveled

grades

raveled[0] = 100

raveled

grades

# Transposing Rows and Columns

grades.T

grades

# Horizontal and Vertical Stacking
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

np.hstack((grades, grades2))

np.vstack((grades, grades2))



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
