# 14.6 Case Study: Unsupervised Machine Learning, Part 1—Dimensionality Reduction

# Loading the Digits Dataset
from sklearn.datasets import load_digits

digits = load_digits()

# Creating a TSNE Estimator for Dimensionality Reduction
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=11)

# Transforming the Digits Dataset’s Features into Two Dimensions
reduced_data = tsne.fit_transform(digits.data)

reduced_data.shape

# Visualizing the Reduced Data
import matplotlib.pyplot as plt

dots = plt.scatter(reduced_data[:, 0], reduced_data[:, 1],
                    c='black')

# Visualizing the Reduced Data with Different Colors for Each Digit
dots = plt.scatter(reduced_data[:, 0], reduced_data[:, 1],
     c=digits.target, cmap=plt.cm.get_cmap('nipy_spectral_r', 10))

colorbar = plt.colorbar(dots)

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
