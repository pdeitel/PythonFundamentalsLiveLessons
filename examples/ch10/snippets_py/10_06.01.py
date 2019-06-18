# Section 10.6.1 snippets

# Creating, Shuffling and Dealing the Cards 
from deck import DeckOfCards

deck_of_cards = DeckOfCards()

print(deck_of_cards)

deck_of_cards.shuffle()

print(deck_of_cards)

# Dealing Cards
deck_of_cards.deal_card()

# Class Card’s Other Features
card = deck_of_cards.deal_card()

str(card)

card.image_name



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
