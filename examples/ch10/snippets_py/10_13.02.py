# Section 10.13.2 snippets

from carddataclass import Card
from carddataclass import Card

c1 = Card(Card.FACES[0], Card.SUITS[3])

c1

print(c1)

c1.face

c1.suit

c1.image_name

c2 = Card(Card.FACES[0], Card.SUITS[3])

c2

c3 = Card(Card.FACES[0], Card.SUITS[0])

c3

c1 == c2

c1 == c3

c1 != c3

from deck2 import DeckOfCards  # uses Card data class

deck_of_cards = DeckOfCards()

print(deck_of_cards)



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
