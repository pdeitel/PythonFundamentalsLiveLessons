# Section 5.17 snippets

# 5.17.1 Sample Graphs for 600, 60,000 and 6,000,000 Die Rolls

# 5.17.2 Visualizing Die-Roll Frequencies and Percentages

# Launching IPython for Interactive Matplotlib Development


# Importing the Libraries
import matplotlib.pyplot as plt

import numpy as np

import random

import seaborn as sns

# Rolling the Die and Calculating Die Frequencies
rolls = [random.randrange(1, 7) for i in range(600)]

values, frequencies = np.unique(rolls, return_counts=True)

# Creating the Initial Bar Plot
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'

sns.set_style('whitegrid')

axes = sns.barplot(x=values, y=frequencies, palette='bright')

# Setting the Window Title and Labeling the x- and y-Axes
axes.set_title(title)

axes.set(xlabel='Die Value', ylabel='Frequency')  

# Finalizing the Bar Plot
axes.set_ylim(top=max(frequencies) * 1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height() 
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')
              
# Rolling Again and Updating the Bar Plot—Introducing IPython Magics
plt.cla()

%recall 5

rolls = [random.randrange(1, 7) for i in range(600)]

rolls = [random.randrange(1, 7) for i in range(60000)]

%recall 6-13

values, frequencies = np.unique(rolls, return_counts=True)
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')  
axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height() 
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')
              
# Saving Snippets to a File with the %save Magic 
%save RollDie.py 1-13





   

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
