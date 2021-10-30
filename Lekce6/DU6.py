import requests
import pandas
from scipy.stats import mannwhitneyu
# #1.PŠENICE
# with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
#   open("psenice.csv", 'w', encoding="utf-8").write(r.text)
#
# psenice = pandas.read_csv("psenice.csv")
# print(psenice.head())
#
# # Hypotézy budou následující:
# # H0: průměry délky zrna jsou si rovné.
# # H1: průměry délky zrna jsou různé (nejsou si rovné).
#
# x = psenice["Rosa"]
# y = psenice["Canadian"]
# print(x.shape)
# print(y.shape)
# print(mannwhitneyu(x, y))
#
# # Výsledek: p-value 3,52% < 5% = Nulovou hypotezu zamítame

#2.JEMNÉ ČÁSTICE 2
import requests

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

air_polution_ukol = pandas.read_csv("air_polution_ukol.csv")
air_polution_ukol["date"] = pandas.to_datetime(air_polution_ukol["date"])
air_polution_ukol["year"] = air_polution_ukol["date"].dt.year
air_polution_ukol["month"] = air_polution_ukol["date"].dt.month
#print(air_polution_ukol)

# a.)Z dat vyber data za leden roku 2019 a 2020.
air_polution_vyber = air_polution_ukol[air_polution_ukol["month"] == 1]
air_polution_vyber_2019 = pandas.DataFrame()
air_polution_vyber_2020 = pandas.DataFrame()
air_polution_vyber_2019 = air_polution_vyber[air_polution_vyber["year"] == 2019]
air_polution_vyber_2020 = air_polution_vyber[air_polution_vyber["year"] == 2020]
print(air_polution_vyber_2019)
print(air_polution_vyber_2020)

# b.)Porovnej průměrné množství jemných částic ve vzduchu v těchto dvou měsících pomocí Mann–Whitney U testu. Formuluj hypotézy pro oboustranný test (nulovou i alternativní) a napiš je do komentářů v programu
# # Hypotézy budou následující:
# # H0: průměrné množství jemných částic ve vzduchu v těchto dvou měsících je si rovné.
# # H1: průměrné množství jemných částic ve vzduchu v těchto dvou měsících je různé (není si rovné).
#
x = air_polution_vyber_2019[air_polution_vyber_2019["year"] == 2019]["pm25"]
y = air_polution_vyber_2020[air_polution_vyber_2020["year"] == 2020]["pm25"]
print(x.shape)
print(y.shape)
vysledek = mannwhitneyu(x, y)
vysledek = vysledek.pvalue

if vysledek < 0.05:
  print("Nulovou hypotezu zamítame")
else:
  print("Nulovou hypotezu nezamítame")


#Měl(a) bys dospět k výsledku, že p-hodnota testu je 1.1 %. Rozhodni, zda bys na hladině významnosti 5 % zamítla nulovou hypotézu. Své rozhodnutí napiš do programu
#
# # Výsledek: p-value 1.1% < 5% = Nulovou hypotezu zamítame