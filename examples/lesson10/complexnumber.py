# complexnumber.py
"""Complex class with overloaded operators."""

class Complex:
    """Complex class that represents a complex number 
    with real and imaginary parts."""

    def __init__(self, real, imaginary):
        """Initialize Complex class's attributes."""
        self.real = real
        self.imaginary = imaginary

    def __add__(self, right):
        """Overrides the + operator."""
        return Complex(self.real + right.real, 
                       self.imaginary + right.imaginary)

    def __iadd__(self, right):
        """Overrides the += operator."""
        self.real += right.real
        self.imaginary += right.imaginary
        return self

    def __repr__(self):
        """Return string representation for repr()."""
        return (f'({self.real}' + 
                (' + ' if self.imaginary >= 0 else ' - ') +
                f'{abs(self.imaginary)}i)')


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
