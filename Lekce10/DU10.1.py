import requests

r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-2-rot.csv"
)
open("soybean-2-rot.csv", "wb").write(r.content)

r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/auto.csv"
)
open("auto.csv", "wb").write(r.content)

import pandas

from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

data = pandas.read_csv("soybean-2-rot.csv")
print(data)


X = data.drop(columns=["class"])
y = data["class"]

oh_encoder = OneHotEncoder()
X = oh_encoder.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)

clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f1_score(y_test, y_pred, average="weighted"))

#které vstupní proměnné model použil pro rozhodování.
print(oh_encoder.feature_names_in_)
importances = clf.feature_importances_
print(importances)

for feat, importance in zip(oh_encoder.feature_names_in_, clf.feature_importances_):
    print (f'feature: {feat}, importance: {importance}')