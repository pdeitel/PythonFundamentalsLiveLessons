# Section 10.6.4 snippets

from deck import DeckOfCards

deck_of_cards = DeckOfCards()

# Enable Matplotlib in IPython
%matplotlib

# Create the Base `Path` for Each Image
from pathlib import Path

path = Path('.').joinpath('card_images')

# Import the Matplotlib Features
import matplotlib.pyplot as plt

import matplotlib.image as mpimg

# Create the `Figure` and `Axes` Objects
figure, axes_list = plt.subplots(nrows=4, ncols=13)

# Configure the `Axes` Objects and Display the Images
for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

# Maximize the Image Sizes
figure.tight_layout()

### Shuffle and Re-Deal the Deck
deck_of_cards.shuffle()

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)



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
