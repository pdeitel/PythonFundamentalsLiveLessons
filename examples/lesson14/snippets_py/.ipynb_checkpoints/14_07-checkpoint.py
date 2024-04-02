# 14.7 Case Study: Unsupervised Machine Learning, Part 2—k-Means Clustering
# Iris Dataset

# 14.7.1 Loading the Iris Dataset
from sklearn.datasets import load_iris

iris = load_iris()

print(iris.DESCR)

# Checking the Numbers of Samples, Features and Targets
iris.data.shape

iris.target.shape

iris.target_names

iris.feature_names

# 14.7.2 Exploring the Iris Dataset: Descriptive Statistics with Pandas
import pandas as pd

pd.set_option('max_columns', 5)

pd.set_option('display.width', None)

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

iris_df['species'] = [iris.target_names[i] for i in iris.target]

iris_df.head()

pd.set_option('precision', 2)

iris_df.describe()

iris_df['species'].describe()

# 14.7.3 Visualizing the Dataset with a Seaborn pairplot
import seaborn as sns

sns.set(font_scale=1.1)

sns.set_style('whitegrid')

grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4],
     hue='species')

# Displaying the pairplot in One Color
grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4])

# 14.7.4 Using a KMeans Estimator

# Creating the Estimator
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=11)

# Fitting the Model
kmeans.fit(iris.data)

# Comparing the Computer Cluster Labels to the Iris Dataset’s Target Values
print(kmeans.labels_[0:50])

print(kmeans.labels_[50:100])

print(kmeans.labels_[100:150])

# 14.7.5 Dimensionality Reduction with Principal Component Analysis
# Creating the PCA Object
from sklearn.decomposition import PCA

pca = PCA(n_components=2, random_state=11)

# Transforming the Iris Dataset’s Features into Two Dimensions
pca.fit(iris.data)

iris_pca = pca.transform(iris.data)

iris_pca.shape

# Visualizing the Reduced Data
iris_pca_df = pd.DataFrame(iris_pca, 
                            columns=['Component1', 'Component2'])

iris_pca_df['species'] = iris_df.species

axes = sns.scatterplot(data=iris_pca_df, x='Component1', 
     y='Component2', hue='species', legend='brief', 
     palette='cool')

iris_centers = pca.transform(kmeans.cluster_centers_)

import matplotlib.pyplot as plt

dots = plt.scatter(iris_centers[:,0], iris_centers[:,1], 
                    s=100, c='k')

# 14.7.6 Choosing the Best Clustering Estimator
from sklearn.cluster import DBSCAN, MeanShift,\
     SpectralClustering, AgglomerativeClustering

estimators = {
    'KMeans': kmeans,
    'DBSCAN': DBSCAN(),
    'MeanShift': MeanShift(),
    'SpectralClustering': SpectralClustering(n_clusters=3),
    'AgglomerativeClustering': 
        AgglomerativeClustering(n_clusters=3)
}

import numpy as np

for name, estimator in estimators.items():
     estimator.fit(iris.data)
     print(f'\n{name}:')
     for i in range(0, 101, 50):
         labels, counts = np.unique(
             estimator.labels_[i:i+50], return_counts=True)
         print(f'{i}-{i+50}:')
         for label, count in zip(labels, counts):
             print(f'   label={label}, count={count}')
             
            
# Code for visualizing in 3D
tsne3 = TSNE(n_components=3, random_state=11)
reduced_data3 = tsne3.fit_transform(digits.data) 
figure = plt.figure(figsize=(7, 5))
import mpl_toolkits.mplot3d.axes3d as axes3d
axes = fig.add_subplot(projection='3d')
dots = axes.scatter(reduced_data3[:, 0], reduced_data3[:, 1], reduced_data3[:, 2], 
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
