# code for visualizing the Digits dataset in 3D
from sklearn.datasets import load_digits

digits = load_digits()

from sklearn.manifold import TSNE

tsne3 = TSNE(n_components=3, random_state=11)

reduced_data3 = tsne3.fit_transform(digits.data) 

import matplotlib.pyplot as plt

figure = plt.figure(figsize=(7, 5))

import mpl_toolkits.mplot3d.axes3d as axes3d

axes = figure.add_subplot(projection='3d')

dots = axes.scatter(reduced_data3[:, 0], reduced_data3[:, 1], reduced_data3[:, 2], 
    c=digits.target, cmap=plt.cm.get_cmap('nipy_spectral_r', 10))
    
colorbar = plt.colorbar(dots)

plt.show()
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