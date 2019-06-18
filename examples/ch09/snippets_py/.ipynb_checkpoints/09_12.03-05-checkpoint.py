# NOTE: This file contains all the snippets for Sections 9.12.3-9.12.5,
# including the 9.12.5 Self Check

# Section 9.12.3 snippets

# Loading the Titanic Dataset via a URL
import pandas as pd

titanic = pd.read_csv('https://vincentarelbundock.github.io/' +
    'Rdatasets/csv/carData/TitanicSurvival.csv')
                      
# Viewing Some of the Rows in the Titanic Dataset
pd.set_option('precision', 2)  # format for floating-point values

titanic.head()

titanic.tail()

# Customizing the Column Names
titanic.columns = ['name', 'survived', 'sex', 'age', 'class']

titanic.head()

# Section 9.12.4 snippets
titanic.describe()

(titanic.survived == 'yes').describe()

# Section 9.12.5 snippets
%matplotlib

histogram = titanic.hist()

# Section 9.12.5 Self Check snippets

# Exercise 2
pd.read_csv('grades.csv', names=['ID', 'Name', 'Grade'])




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
