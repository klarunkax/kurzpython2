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
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kosatce.csv")
open("kosatce.csv", "wb").write(r.content)

data = pandas.read_csv("kosatce.csv")
print(data.shape)
print(data.head())
print(data.isna().sum())
#data = data.dropna()
#print(data.shape)
print(data["target"].value_counts(normalize=True))

#Načti si data do proměnných X a y
X = data.drop(columns=["target"])
y = data["target"]

#Rozděl data na trénovací a testovací (velikost testovacích dat nastav na 30% a nezapomeň nastavit proměnnou random_state, aby tvoje výsledky byly reprodukovatelné)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
#Pokud použijeme stejný algoritmus jako v prvním úkolu, tj. KNeighborsClassifier, je možné předpovědět typ kosatce na základě těchto dat tak, aby metrika f1_score dosáhla alespoň 85%?
#trenování modelu a vyhodnocení modelu ????
# ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
# f1_scores = []
#
# for k in ks:
#     clf = KNeighborsClassifier(n_neighbors=k)
#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)
#     f1_scores.append(f1_score(y_test, y_pred))
# plt.plot(ks, f1_scores)
# plt.show()

#trenování modelu
clf = KNeighborsClassifier(n_neighbors=17)
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
print(f1_score(y_test, y_pred))
