# Section 8.12.1 snippets

import re

# Matching Literal Characters
pattern = '02215'

'Match' if re.fullmatch(pattern, '02215') else 'No match'

'Match' if re.fullmatch(pattern, '51220') else 'No match'

# Metacharacters, Character Classes and Quantifiers
'Valid' if re.fullmatch(r'\d{5}', '02215') else 'Invalid'

'Valid' if re.fullmatch(r'\d{5}', '9876') else 'Invalid'

# Other Predefined Character Classes

# Custom Character Classes
'Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Invalid'

'Valid' if re.fullmatch('[A-Z][a-z]*', 'eva') else 'Invalid'

'Match' if re.fullmatch('[^a-z]', 'A') else 'No match'

'Match' if re.fullmatch('[^a-z]', 'a') else 'No match'

'Match' if re.fullmatch('[*+$]', '*') else 'No match'

'Match' if re.fullmatch('[*+$]', '!') else 'No match'

# * vs. + Quantifier
'Valid' if re.fullmatch('[A-Z][a-z]+', 'Wally') else 'Invalid'

'Valid' if re.fullmatch('[A-Z][a-z]+', 'E') else 'Invalid'

# Other Quantifiers
'Match' if re.fullmatch('labell?ed', 'labelled') else 'No match'

'Match' if re.fullmatch('labell?ed', 'labeled') else 'No match'

'Match' if re.fullmatch('labell?ed', 'labellled') else 'No match'

'Match' if re.fullmatch(r'\d{3,}', '123') else 'No match'

'Match' if re.fullmatch(r'\d{3,}', '1234567890') else 'No match'

'Match' if re.fullmatch(r'\d{3,}', '12') else 'No match'

'Match' if re.fullmatch(r'\d{3,6}', '123') else 'No match'

'Match' if re.fullmatch(r'\d{3,6}', '123456') else 'No match'

'Match' if re.fullmatch(r'\d{3,6}', '1234567') else 'No match'

'Match' if re.fullmatch(r'\d{3,6}', '12') else 'No match'


##########################
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
##########################
