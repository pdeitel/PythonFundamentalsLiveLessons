# Section 7.3 snippets
import numpy as np

integers = np.array([[1, 2, 3], [4, 5, 6]])

integers

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

floats

# Determining an array’s Element Type
integers.dtype

floats.dtype

# Determining an array’s Dimensions
integers.ndim

floats.ndim

integers.shape

floats.shape

# Determining an array’s Number of Elements and Element Size
integers.size

integers.itemsize

floats.size

floats.itemsize

# Iterating through a Multidimensional array’s Elements
for row in integers:
    for column in row:
        print(column, end='  ')
    print()

for i in integers.flat:
    print(i, end='  ')
    


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
