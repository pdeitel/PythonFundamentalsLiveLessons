# Section 11.3.2 snippets
# NOTE: This section's self check snippets are included in this file 
# because the interactive session continues into the self check.

# Loading the Text
from pathlib import Path

text = Path('RomeoAndJuliet.txt').read_text()

# Loading the Mask Image that Specifies the Word Cloud’s Shape
import imageio

mask_image = imageio.imread('mask_heart.png')

# Configuring the WordCloud Object
from wordcloud import WordCloud   

wordcloud = WordCloud(width=1000, height=1000, 
    colormap='prism', mask=mask_image, background_color='white')
   

# Generating the Word Cloud
wordcloud = wordcloud.generate(text)

# Saving the Word Cloud as an Image File
wordcloud = wordcloud.to_file('RomeoAndJulietHeart.png')

%matplotlib

import matplotlib.pyplot as plt

plt.imshow(wordcloud)




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
