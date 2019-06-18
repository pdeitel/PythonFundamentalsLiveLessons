# Section 6.2.3 snippets

# 6.2.3 Basic Dictionary Operations
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

roman_numerals

# Accessing the Value Associated with a Key
roman_numerals['V']

# Updating the Value of an Existing Key–Value Pair
roman_numerals['X'] = 10

roman_numerals

# Adding a New Key–Value Pair
roman_numerals['L'] = 50

roman_numerals

# Removing a Key–Value Pair
del roman_numerals['III']

roman_numerals

roman_numerals.pop('X')

roman_numerals

# Attempting to Access a Nonexistent Key
roman_numerals['III']

roman_numerals.get('III')

roman_numerals.get('III', 'III not in dictionary')

roman_numerals.get('V')

# Testing Whether a Dictionary Contains a Specified Key
'V' in roman_numerals

'III' in roman_numerals

'III' not in roman_numerals



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
