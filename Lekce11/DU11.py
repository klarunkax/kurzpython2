# B-2
# C-1
#D-3
#A-4

from sklearn.datasets import load_digits
import pandas
import requests

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, silhouette_samples

digits = load_digits()
X = digits.data

print(X)
scaler = StandardScaler()
X = scaler.fit_transform(X)
X.shape
print(X)

tsne = TSNE(
    init="pca",
    n_components=2,
    perplexity=10,
    learning_rate="auto",
    random_state=0,
)
X = tsne.fit_transform(X)
print(X.shape)


plt.scatter(X[:, 0], X[:, 1], s=15)
plt.show()

model = KMeans(n_clusters=10, random_state=0)
labels = model.fit_predict(X)

print(silhouette_score(X, labels))