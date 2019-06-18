# Section 7.14.2 Self Check snippets

# Exercise 1
import pandas as pd

temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82],
         'Thu': [75, 97], 'Fri': [62, 79]}
         
temperatures = pd.DataFrame(temps, index=['Low', 'High'])  # (a)

temperatures  # (a)

temperatures.loc[:, 'Mon':'Wed']  # (b)

temperatures.loc['Low']  # (c)

pd.set_option('precision', 2)  # (d)

temperatures.mean()  # (d)

temperatures.mean(axis=1)  # (e)


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
