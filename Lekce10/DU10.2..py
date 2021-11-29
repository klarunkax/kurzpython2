import requests

r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/auto.csv"
)
open("auto.csv", "wb").write(r.content)

import pandas

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import LinearSVC

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = pandas.read_csv("auto.csv", na_values=["?"])
data = data.dropna()
print(data.shape)
print(data.head())
print(data.isna().sum())
print(data)

data_grouped = data.groupby(["year"]).agg({"mpg":["mean"]})
# data_grouped = pandas.DataFrame(data_grouped)
print(data_grouped)

data_grouped.plot(
title="průměřná spotřeba"
)
plt.show()

# X = data.drop(columns=["origin", "name"])
# y = data["origin"]
#
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.3, stratify=y, random_state=0
# )
#
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)
#
# model = DecisionTreeClassifier(random_state=0)
#
# params={'max_depth': [1,2,3,4,5], 'min_samples_leaf': [1,2,3,4,5]}
#
#
# clf = GridSearchCV(model, params, scoring="f1_weighted")
# clf.fit(X_train, y_train)
#
# print(clf.best_params_)
# print(clf.best_score_)
#
# y_pred = clf.predict(X_test)
# print(round(f1_score(y_test, y_pred, average="weighted"), 3))
#
# model_2 = DecisionTreeClassifier(random_state=0,max_depth=5,min_samples_leaf=1)
# clf_2 = model_2.fit(X_train, y_train)
# clf_2.fit(X_train, y_train)
# y_pred_2 = clf_2.predict(X_test)
# print(round(f1_score(y_test, y_pred_2, average="weighted"), 3))