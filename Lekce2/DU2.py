import requests

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
  open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

import pandas
import numpy

president_elections = pandas.read_csv("1976-2020-president.csv")
president_elections["Rank"] = president_elections.groupby(["state","year"])["candidatevotes"].rank(method="min", ascending=False)
president_elections_winners = president_elections[president_elections["Rank"] == 1]

print(president_elections_winners.head())
president_elections_winners = president_elections_winners.sort_values(["state", "year"])
president_elections_winners["party_following_year"] = president_elections_winners.groupby(["state"])["party_simplified"].shift()
president_elections_winners = president_elections_winners[["party_simplified","party_following_year","state","year"]]
president_elections_winners = president_elections_winners.dropna()
print(president_elections_winners.head(n=20))

president_elections_winners["change"] = numpy.where(president_elections_winners["party_simplified"] == president_elections_winners["party_following_year"], 0, 1)
president_elections_winners_change = pandas.DataFrame(president_elections_winners.groupby("state")["change"].sum())
print(president_elections_winners_change)
president_elections_winners_change_sorted = president_elections_winners_change.sort_values(["change"])
print(president_elections_winners_change_sorted)


