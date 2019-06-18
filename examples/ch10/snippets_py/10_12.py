# Section 10.12 snippets

from collections import namedtuple

Card = namedtuple('Card', ['face', 'suit'])

card = Card(face='Ace', suit='Spades')

card.face

card.suit

card

# Other Named Tuple Features
values = ['Queen', 'Hearts']

card = Card._make(values)

card

card._asdict()



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
