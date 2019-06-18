# Section 7.9 snippets
import numpy as np

numbers = np.array([1, 4, 9, 16, 25, 36])

np.sqrt(numbers)

numbers2 = np.arange(1, 7) * 10

numbers2

np.add(numbers, numbers2)

# Broadcasting with Universal Functions
np.multiply(numbers2, 5)

numbers3 = numbers2.reshape(2, 3)

numbers3

numbers4 = np.array([2, 4, 6])

np.multiply(numbers3, numbers4)



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
