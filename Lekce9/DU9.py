import pandas
import requests
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    ConfusionMatrixDisplay,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/water-potability.csv")
open("water-potability.csv", 'wb').write(r.content)

data = pandas.read_csv("water-potability.csv")
print(data.shape)
print(data.head())
print(data.isna().sum())
data = data.dropna()
print(data.shape)
print(data["Potability"].value_counts(normalize=True))

#Rozdělíme si vstupní proměnné a cílovou hodnotu:
X = data.drop(columns=["Potability"])
y = data["Potability"]

#rozdělíme na trénovací a testovací sadu: ???
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print(X_train)

#Data normalizujeme metodou z-scores
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#trenování modelu a vyhodnocení modelu ????
# ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
# scores = []
#
# for k in ks:
#     clf = KNeighborsClassifier(n_neighbors=k)
#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)
#     scores.append(precision_score(y_test, y_pred))
# plt.plot(ks, scores)
# plt.show()

#trenování modelu
clf = KNeighborsClassifier(n_neighbors=15)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(y_pred)

ConfusionMatrixDisplay.from_estimator(
    clf,
    X_test,
    y_test,
    display_labels=clf.classes_,
    cmap=plt.cm.Blues,
)
plt.show()
#
print(precision_score(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
