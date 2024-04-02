# 14.5 Case Study: Multiple Linear Regression with the California Housing Dataset

# 14.5.1 Loading the Dataset
# Loading the Data
from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()

# Displaying the Dataset’s Description
print(california.DESCR)

california.data.shape

california.target.shape

california.feature_names

# 14.5.2 Exploring the Data with Pandas
import pandas as pd

pd.set_option('precision', 4)

pd.set_option('max_columns', 9)

pd.set_option('display.width', None)

california_df = pd.DataFrame(california.data, 
                              columns=california.feature_names)
 
california_df['MedHouseValue'] = pd.Series(california.target)

california_df.head()

california_df.describe()

# 14.5.3 Visualizing the Features
sample_df = california_df.sample(frac=0.1, random_state=17)

import matplotlib.pyplot as plt

import seaborn as sns

sns.set(font_scale=2)

sns.set_style('whitegrid')                                    

for feature in california.feature_names:
     plt.figure(figsize=(16, 9))
     sns.scatterplot(data=sample_df, x=feature, 
                     y='MedHouseValue', hue='MedHouseValue', 
                     palette='cool', legend=False)

# 14.5.4 Splitting the Data for Training and Testing
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
     california.data, california.target, random_state=11)

X_train.shape

X_test.shape

# 14.5.5 Training the Model
from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()

linear_regression.fit(X=X_train, y=y_train)

for i, name in enumerate(california.feature_names):
     print(f'{name:>10}: {linear_regression.coef_[i]}')

linear_regression.intercept_

# 14.5.6 Testing the Model
predicted = linear_regression.predict(X_test)

expected = y_test

predicted[:5]

expected[:5]

# 14.5.7 Visualizing the Expected vs. Predicted Prices
df = pd.DataFrame()

df['Expected'] = pd.Series(expected)

df['Predicted'] = pd.Series(predicted)

figure = plt.figure(figsize=(9, 9))

axes = sns.scatterplot(data=df, x='Expected', y='Predicted', 
     hue='Predicted', palette='cool', legend=False)

start = min(expected.min(), predicted.min())

end = max(expected.max(), predicted.max())

axes.set_xlim(start, end)

axes.set_ylim(start, end)

line = plt.plot([start, end], [start, end], 'k--')

# 14.5.8 Regression Model Metrics
from sklearn import metrics

metrics.r2_score(expected, predicted)

metrics.mean_squared_error(expected, predicted)

# 14.5.9 Choosing the Best Model
from sklearn.linear_model import ElasticNet, Lasso, Ridge

estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}

from sklearn.model_selection import KFold, cross_val_score

for estimator_name, estimator_object in estimators.items():
     kfold = KFold(n_splits=10, random_state=11, shuffle=True)
     scores = cross_val_score(estimator=estimator_object, 
         X=california.data, y=california.target, cv=kfold,
         scoring='r2')
     print(f'{estimator_name:>16}: ' + 
           f'mean of r2 scores={scores.mean():.3f}')

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
