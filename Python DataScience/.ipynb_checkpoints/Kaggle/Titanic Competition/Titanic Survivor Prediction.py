# Titanic Survival Predictor
"""
Created on Wed Dec 11 12:13:25 2019

@author: donal
"""


#importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Importing the dataset
#saved to my working folder and then pressed F5
dataset= pd.read_csv('train_1.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
laberencoder_X = LabelEncoder()
laberencoder_X.fit_transform(X[:,2])

df=pd.Categorical()
# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 2] = labelencoder_X.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [2])
X = onehotencoder.fit_transform(X).toarray()

#avoiding the dummy variable trap
X=X[:,1:]

#taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

from sklearn.preprocessing import Imputer
imputer = Imputer()
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])