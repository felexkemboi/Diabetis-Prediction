import csv
import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer

from sklearn import metrics

from sklearn.impute import SimpleImputer


from sklearn.linear_model import LogisticRegression

import pickle


df = pd.read_excel('diabetes_dataset.xlsx')
print(df.head(3))

from sklearn.model_selection import train_test_split
feature_col_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
predicted_class_names = ['Outcome']

X = df[feature_col_names].values # these are factors for the prediction
y = df[predicted_class_names].values # this is what we want to predict

split_test_size = 0.3




X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = split_test_size,random_state=42)



#imputing missing values with the mean
from sklearn.preprocessing import Imputer
# For all readings == 0, impute with mean
fill_0 = Imputer(missing_values=0,strategy="mean",axis=0)
X_train= fill_0.fit_transform(X_train)
X_test = fill_0.fit_transform(X_test)


#fitting the regression model
lr_model=LogisticRegression(C=0.7,random_state=42)



lr_model.fit(X_train,y_train.ravel())

pickle.dump(lr_model, open('model.pkl','wb'))


lr_predict_test = lr_model.predict(X_test)






model = pickle.load(open('model.pkl','rb'))


"""


print(X_test)
print() 
print("Accuracy: {0:.4f}%".format(metrics.accuracy_score(y_test,lr_predict_test)*100))
"""




"""
print()
print("Confusion Matrix")
print(metrics.confusion_matrix(y_test,lr_predict_test))
print()
print("Classification Report")
print(metrics.classification_report(y_test,lr_predict_test))

# Loading model to compare the results

model = pickle.load(open('model.pkl','rb')) """

