# Section 8.12.1 Self Check snippets

# Exercise 4
import re

street = r'\d+ [A-Z][a-z]* [A-Z][a-z]*'

'Match' if re.fullmatch(street, '123 Main Street') else 'No match'

'Match' if re.fullmatch(street, 'Main Street') else 'No match'


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
