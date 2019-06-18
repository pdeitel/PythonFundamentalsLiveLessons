# Section 7.5 snippets

# Creating Integer Ranges with arange 
import numpy as np

np.arange(5)

np.arange(5, 10)

np.arange(10, 1, -2)

# Creating Floating-Point Ranges with linspace
np.linspace(0.0, 1.0, num=5)

# Reshaping an array
np.arange(1, 21).reshape(4, 5)

# Displaying Large arrays 
np.arange(1, 100001).reshape(4, 25000)

np.arange(1, 100001).reshape(100, 1000)


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
