# salariedemployee.py
"""SalariedEmployee concrete subclass of Employee."""
from decimal import Decimal
from employee import Employee

class SalariedEmployee(Employee):
    """Class representing an employee who gets paid a weekly salary."""

    def __init__(self, first_name, last_name, ssn, weekly_salary):
        """Initialize SalariedEmployee attributes."""
        super().__init__(first_name, last_name, ssn) 
        self.weekly_salary = weekly_salary

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, salary):
        """Set weekly_salary or raise ValueError if invalid."""
        if salary < Decimal('0.0'):
            raise ValueError('salary worked must be >= 0.0')
        
        self._weekly_salary = salary
        
    def earnings(self):
        """Calculate earnings."""
        return self.weekly_salary

    def __repr__(self):
        """Return string representation for repr()."""
        return ('SalariedEmployee: ' + super().__repr__() + 
                f'\nweekly salary: {self.weekly_salary:.2f}')




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
