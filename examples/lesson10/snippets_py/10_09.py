# Section 10.9 snippets

class WellPaidDuck:
    def __repr__(self):
        return 'I am a well-paid duck'
    def earnings(self):
        return Decimal('1_000_000.00')
    
from decimal import Decimal

from commissionemployee import CommissionEmployee

from salariedcommissionemployee import SalariedCommissionEmployee

c = CommissionEmployee('Sue', 'Jones', '333-33-3333',
                       Decimal('10000.00'), Decimal('0.06'))
                       
s = SalariedCommissionEmployee('Bob', 'Lewis', '444-44-4444',
    Decimal('5000.00'), Decimal('0.04'), Decimal('300.00'))
    
d = WellPaidDuck()

employees = [c, s, d]

for employee in employees:
    print(employee)
    print(f'{employee.earnings():,.2f}\n')

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
