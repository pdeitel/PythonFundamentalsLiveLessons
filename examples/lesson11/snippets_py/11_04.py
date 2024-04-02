# Section 11.4 snippets
# NOTE: This section's self check snippets are included in this file 
# because the interactive session continues into the self check.

# Calculating Statistics and Readability Scores
from pathlib import Path

text = Path('RomeoAndJuliet.txt').read_text()

from textatistic import Textatistic

readability = Textatistic(text)

%precision 3

readability.dict()





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
