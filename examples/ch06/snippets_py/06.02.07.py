# Section 6.2.7 snippets
# Python Standard Library Module ‘collections‘
from collections import Counter

text = ('this is sample text with several words '
        'this is more sample text with some different words')

counter = Counter(text.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')
    
print('Number of unique keys:', len(counter.keys()))




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
