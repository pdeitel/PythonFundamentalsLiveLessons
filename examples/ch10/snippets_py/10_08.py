# Section 10.8.1 snippets

# 10.8.1 Base Class CommissionEmployee

# Testing Class CommissionEmployee
from commissionemployee import CommissionEmployee

from decimal import Decimal

c = CommissionEmployee('Sue', 'Jones', '333-33-3333', 
    Decimal('10000.00'), Decimal('0.06'))

c

print(f'{c.earnings():,.2f}')

c.gross_sales = Decimal('20000.00')

c.commission_rate = Decimal('0.1')

print(f'{c.earnings():,.2f}')

# 10.8.2 Subclass SalariedCommissionEmployee 

# Testing Class SalariedCommissionEmployee

from salariedcommissionemployee import SalariedCommissionEmployee

s = SalariedCommissionEmployee('Bob', 'Lewis', '444-44-4444',
         Decimal('5000.00'), Decimal('0.04'), Decimal('300.00'))
         
print(s.first_name, s.last_name, s.ssn, s.gross_sales, 
       s.commission_rate, s.base_salary)

print(f'{s.earnings():,.2f}')

s.gross_sales = Decimal('10000.00')

s.commission_rate = Decimal('0.05')

s.base_salary = Decimal('1000.00')

print(s)

print(f'{s.earnings():,.2f}')

# Testing the "is a" Relationship 
issubclass(SalariedCommissionEmployee, CommissionEmployee)

isinstance(s, CommissionEmployee)

isinstance(s, SalariedCommissionEmployee)

# Processing CommissionEmployees and SalariedCommissionEmployees Polymorphically
employees = [c, s]

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
