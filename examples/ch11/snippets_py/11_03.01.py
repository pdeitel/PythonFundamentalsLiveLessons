# Section 11.3.1 snippets

# Loading the Data
from pathlib import Path

from textblob import TextBlob

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())

from nltk.corpus import stopwords

stop_words = stopwords.words('english')

# Getting the Word Frequencies
items = blob.word_counts.items()

# Eliminating the Stop Words
items = [item for item in items if item[0] not in stop_words]

# Sorting the Words by Frequency
from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)

# Getting the Top 20 Words
top20 = sorted_items[1:21]

# Convert top20 to a DataFrame 
import pandas as pd

df = pd.DataFrame(top20, columns=['word', 'count'])  

df

# Visualizing the DataFrame 
axes = df.plot.bar(x='word', y='count', legend=False)

import matplotlib.pyplot as plt

plt.gcf().tight_layout()


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
