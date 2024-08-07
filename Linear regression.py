#!/usr/bin/env pyhton3
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle


data = pd.read_csv("student-mat.csv", sep=";")


data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]


predict = "G3"


X = np.array(data.drop([predict], axis=1))
y = np.array(data[predict])


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)


linear = linear_model.LinearRegression()

# Train the model
linear.fit(x_train, y_train)

# Evaluate the model
acc = linear.score(x_test, y_test)
print(f"Accuracy: {acc}")

# Print the coefficients and intercept
print('Coefficient:', linear.coef_)
print('Intercept:', linear.intercept_)

# Make predictions
predictions = linear.predict(x_test)

# Display the predictions along with the input and actual values
for i in range(len(predictions)):
    print(f"Prediction: {predictions[i]}, Features: {x_test[i]}, Actual: {y_test[i]}")
