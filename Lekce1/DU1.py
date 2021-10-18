import requests
import pandas
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

# 1.TITANIC
# titanic = pandas.read_csv("titanic.csv")
#
# print(titanic.head())
# titanic.info()
#
# titanic_pivot = pandas.pivot_table(titanic, index="Pclass",columns="Sex", values="Survived",aggfunc=numpy.sum)
# print(titanic_pivot)

#2.PUJČOVÁNÍ KOL
london_merged = pandas.read_csv("london_merged.csv")

london_merged["timestamp"] = pandas.to_datetime(london_merged["timestamp"])
london_merged["year"] = london_merged["timestamp"].dt.year

print(london_merged.head())
london_merged.info()

london_merged_pivot = pandas.pivot_table(london_merged, index="weather_code",columns="year", values="weather_code")
print(london_merged_pivot)
