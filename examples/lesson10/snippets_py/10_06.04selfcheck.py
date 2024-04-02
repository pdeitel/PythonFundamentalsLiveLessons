# Section 10.6.4 Self Check snippets

# Exercise 3
deck_of_cards.shuffle()

figure, axes_list = plt.subplots(nrows=2, ncols=5)

for axes in axes_list.ravel():
     axes.get_xaxis().set_visible(False)
     axes.get_yaxis().set_visible(False)
     image_name = deck_of_cards.deal_card().image_name
     img = mpimg.imread(str(path.joinpath(image_name).resolve()))
     axes.imshow(img)

figure.tight_layout()
        


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
