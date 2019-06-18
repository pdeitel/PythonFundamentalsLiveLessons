# Section 4.14 snippets

# Importing Multiple Identifiers from a Module
from math import ceil, floor

ceil(10.3)

floor(10.7)

# Caution: Avoid Wildcard Imports 
e = 'hello'

from math import *

e

# Binding Names for Modules and Module Identifiers
import statistics as stats

grades = [85, 93, 45, 87, 93]

stats.mean(grades)



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
