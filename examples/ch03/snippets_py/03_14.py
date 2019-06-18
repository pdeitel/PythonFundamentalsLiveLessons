# Section 3.14 snippets
amount = 112.31

print(amount)

print(f'{amount:.20f}')

# Importing Type Decimal from the decimal Module 
from decimal import Decimal

# Creating Decimals
principal = Decimal('1000.00')
principal

rate = Decimal('0.05')
rate

# Decimal Arithmetic 
x = Decimal('10.5')
y = Decimal('2')
x + y
x // y
x += y
x

# Calculating Compound Interest
for year in range(1, 11):
    amount = principal * (1 + rate) ** year 
    print(f'{year:>2}{amount:>10.2f}')



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
