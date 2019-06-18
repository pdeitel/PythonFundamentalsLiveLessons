# Section 7.14.2 snippets

# Creating a DataFrame from a Dictionary
import pandas as pd

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90],
               'Sam': [94, 77, 90], 'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
               
grades = pd.DataFrame(grades_dict)

grades

# Customizing a DataFrame’s Indices with the index Attribute 
grades.index = ['Test1', 'Test2', 'Test3']

grades

# Accessing a DataFrame’s Columns 
grades['Eva']

grades.Sam

# Selecting Rows via the loc and iloc Attributes
grades.loc['Test1']

grades.iloc[1]

# Selecting Rows via Slices and Lists with the loc and iloc Attributes
grades.loc['Test1':'Test3']

grades.iloc[0:2]

grades.loc[['Test1', 'Test3']]

grades.iloc[[0, 2]]

# Selecting Subsets of the Rows and Columns 
grades.loc['Test1':'Test2', ['Eva', 'Katie']]

grades.iloc[[0, 2], 0:3]

# Boolean Indexing
grades[grades >= 90]

grades[(grades >= 80) & (grades < 90)]

# Accessing a Specific DataFrame Cell by Row and Column
grades.at['Test2', 'Eva']

grades.iat[2, 0]

grades.at['Test2', 'Eva'] = 100

grades.at['Test2', 'Eva']

grades.iat[1, 2] = 87

grades.iat[1, 2]

# Descriptive Statistics
grades.describe()

pd.set_option('precision', 2)

grades.describe()

grades.mean()

# Transposing the DataFrame with the T Attribute
grades.T

grades.T.describe()

grades.T.mean()

# Sorting By Rows by Their Indices
grades.sort_index(ascending=False)

# Sorting By Column Indices
grades.sort_index(axis=1)

# Sorting By Column Values
grades.sort_values(by='Test1', axis=1, ascending=False)

grades.T.sort_values(by='Test1', ascending=False)

grades.loc['Test1'].sort_values(ascending=False)


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
