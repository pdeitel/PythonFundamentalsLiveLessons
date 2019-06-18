# Section 8.12.2 snippets

# Function sub—Replacing Patterns 
import re

re.sub(r'\t', ', ', '1\t2\t3\t4')

re.sub(r'\t', ', ', '1\t2\t3\t4', count=2)

# Function split 
re.split(r',\s*', '1,  2,  3,4,    5,6,7,8')

re.split(r',\s*', '1,  2,  3,4,    5,6,7,8', maxsplit=3)



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
