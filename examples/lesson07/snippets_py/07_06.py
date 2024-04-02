# Section 7.6 snippets

# Timing the Creation of a List Containing Results of 6,000,000 Die Rolls 
import random

%timeit rolls_list = \
   [random.randrange(1, 7) for i in range(0, 6_000_000)]

# Timing the Creation of an array Containing Results of 6,000,000 Die Rolls  
import numpy as np

%timeit rolls_array = np.random.randint(1, 7, 6_000_000)

# 60,000,000 and 600,000,000 Die Rolls  
%timeit rolls_array = np.random.randint(1, 7, 60_000_000)

%timeit rolls_array = np.random.randint(1, 7, 600_000_000)

# Customizing the %timeit Iterations  
%timeit -n3 -r2 rolls_array = np.random.randint(1, 7, 6_000_000)

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
