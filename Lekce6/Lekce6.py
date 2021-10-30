# 1.NORMÁLNÍ ROZDĚLENÍ
import numpy
from scipy.stats import norm
import matplotlib.pyplot as plt

# mu = 100
# sigma = 15
#
# data = norm.rvs(loc=mu, scale=sigma, size=100_000)
# print(data)
#plt.hist(data, 100, density=True)
#count, bins, ignored = plt.hist(data, bins=100, density=True)
#plt.show()
# mensi_nez_178 = norm.cdf(178, 180, 8)
# mensi_nez_186 = norm.cdf(186, 180, 8)
# rozdil = mensi_nez_186 - mensi_nez_178
# print(rozdil)

# 2.exponenciální ROZDĚLENÍ
from scipy.stats import expon

# scale = 2
#
# data = expon.rvs(scale=scale, size=100_000)
# count, bins, ignored = plt.hist(data, 40, density=True)
# plt.plot(bins, expon.pdf(bins, scale=scale), linewidth=1, color='r')
# plt.show()

# 3.CELOČÍSELNÉ ROZDĚLENÍ
# import pandas
# from scipy.stats import binom
#
# n = 20
# p = 0.25
#
# points = list(range(0, 21))
# data = binom.cdf(points, n, p)
# data = pandas.DataFrame(data)
# data["Color"] = numpy.where(data.index > 10, "green", "red")
# data[0].plot(kind="bar", color=data["Color"])
# plt.show()

# # 4. TESTOVÁNÍ HYPOTÉZ
# from scipy.stats import binom
#
# #kouzelník a hodi mincí
# print(binom.pmf(2, 2, 0.5))

import pandas
import matplotlib.pyplot as plt
#
# p = 0.5
# n = list(range(1, 10))
#
# y = binom.pmf(k=n, n=n, p=p)
# data = pandas.DataFrame(y)
# data["Color"] = numpy.where(data[0] > 0.05, "blue", "red")
# data[0].plot(kind="bar", color=data["Color"])
# plt.show()
#
# #dopočítání pravdepodobnosti
# print(binom.pmf(k=9, n=10, p=0.5))
#
# print(binom.pmf(k=9, n=10, p=0.5) + binom.pmf(k=10, n=10, p=0.5))
#
# #oboustranny test - kouzelník neví na kterou stranu bude padat
# print(binom.pmf(k=0, n=5, p=0.5) + binom.pmf(k=5, n=5, p=0.5))

#příklady testů
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/student-mat.csv")
open("student-mat.csv", "wb").write(r.content)

import pandas

data = pandas.read_csv("student-mat.csv")
print(data.head())

from scipy.stats import mannwhitneyu

x = data[data["school"] == "GP"]["G1"]
y = data[data["school"] == "MS"]["G1"]
print(x.shape)
print(y.shape)
mannwhitneyu(x, y)