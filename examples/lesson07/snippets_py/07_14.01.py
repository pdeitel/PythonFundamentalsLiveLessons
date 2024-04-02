# Section 7.14.1 snippets

# Creating a Series with Default Indices
import pandas as pd

grades = pd.Series([87, 100, 94])

# Displaying a Series
grades

# Creating a Series with All Elements Having the Same Value
pd.Series(98.6, range(3))

# Accessing a Series’ Elements
grades[0]

# Producing Descriptive Statistics for a Series
grades.count()

grades.mean()

grades.min()

grades.max()

grades.std()

grades.describe()

# Creating a Series with Custom Indices
grades = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])

grades

# Dictionary Initializers
grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})

grades

# Accessing a Series’ Elements Via Custom Indices
grades['Eva']

grades.Wally

grades.dtype

grades.values

# Creating a Series of Strings 
hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

hardware

hardware.str.contains('a')

hardware.str.upper()


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
