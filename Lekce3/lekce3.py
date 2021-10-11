import requests
from matplotlib import pyplot as plt

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/dopravni-urazy.csv")
open("dopravni-urazy.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kraje.csv")
open("kraje.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/sportoviste.json")
open("sportoviste.json", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/adopce-zvirat.csv")
open("adopce-zvirat.csv", "wb").write(r.content)

#Cyklus přes řádky tabulky: iterrows a itertuples vs merge, groupby
import math
import pandas
import matplotlib.pyplot as plt
#
# urazy = pandas.read_csv("dopravni-urazy.csv")
# print(urazy.head())
# kraje = pandas.read_csv("kraje.csv")
# print(kraje)
##PRVNÍ METODA
# urazy_prumer = pandas.DataFrame(columns=["nazev_kraje", "hodnota"])
# for idx, kraj in kraje.iterrows():
#     kod_kraje = kraj["kod_polozky"]
#     nazev_kraje = kraj["nazev_polozky"]
#     prumerna_hodnota =  urazy[urazy["kraj"] == kod_kraje]["hodnota"].mean()
#     urazy_prumer = urazy_prumer.append({"nazev_kraje": nazev_kraje, "hodnota": prumerna_hodnota}, ignore_index=True)
#
# urazy_prumer = urazy_prumer.dropna()
# print(urazy_prumer.head())
#
#
# urazy_prumer.sort_values(by="hodnota").plot.bar(
#     x="nazev_kraje", y="hodnota", title="Pocet dopravnich urazu na 100,000 obyvatel (prumer za roky 1995-2017)"
# )
# plt.show()

#DRUHA METODA
# urazy_prumer = pandas.DataFrame(columns=["nazev_kraje", "hodnota"])
#
# for kraj in kraje.itertuples():
#     kod_kraje = kraj.kod_polozky
#     nazev_kraje = kraj.nazev_polozky
#     prumerna_hodnota = urazy[urazy["kraj"] == kod_kraje]["hodnota"].mean()
#     urazy_prumer = urazy_prumer.append({"nazev_kraje": nazev_kraje, "hodnota": prumerna_hodnota}, ignore_index=True)
#
# urazy_prumer.sort_values(by="hodnota").plot.bar(
#     x="nazev_kraje", y="hodnota", title="Pocet dopravnich urazu na 100,000 obyvatel (prumer za roky 1995-2017)"
# )
# plt.show()
#
# ##třetí METODA
# urazy_s_kraji = urazy.merge(kraje, left_on="kraj", right_on="kod_polozky")
# print(urazy_s_kraji.head())

# sportoviste = pandas.read_json("sportoviste.json")
# print(sportoviste.head())
# sportoviste = sportoviste.dropna(how="all", axis="columns")
# sportoviste = sportoviste.set_index("OBJECTID")
# sportoviste.info()
#
# sportoviste = sportoviste.rename(columns={"POINT_Y": "zemepisna_sirka", "POINT_X": "zemepisna_delka"})
# print(sportoviste.head())
#
# poloha_nadrazi_opava = [49.9345092, 17.9085369]
#
#
# def vzdalenost_od_bodu(radek, bod):
#     # Vypocet vzdalenosti mezi dvema body (Eukleidovska vzdalenost)
#     vzdalenost = math.sqrt((bod[0] - radek.zemepisna_sirka) ** 2 + (bod[1] - radek.zemepisna_delka) ** 2)
#     # Prevod na vzdalenost v kilometrech a zaokrouhleni
#     vzdalenost_km = vzdalenost * (2.0 * 6371 * math.pi / 360.0)
#     vzdalenost_km = round(vzdalenost_km, 2)
#     return vzdalenost_km
#
# sportoviste["vzdalenost_od_nadrazi"] = sportoviste.apply(vzdalenost_od_bodu, axis=1, args=(poloha_nadrazi_opava,))
# print(sportoviste.head())
#
# sportoviste_sorted = sportoviste.sort_values(by="vzdalenost_od_nadrazi")[[ "sportoviste_nazev", "vzdalenost_od_nadrazi"]].head()
#
# print(sportoviste_sorted)

# CVIČENÍ
adopce = pandas.read_csv("adopce-zvirat.csv", sep=";")
print(adopce.head())

adopce = adopce.dropna(how='all', axis='columns')
adopce = adopce.dropna(how='all', axis='rows')
import pandas as pd

#adopce.info()

#print(adopce[["nazev_en", "cena","k_prohlidce"]].head())

# adopce_vyber = pandas.DataFrame(columns=["nazev_en", "cena","k_prohlidce"])
# for idx, nazev_en in adopce.iterrows():
#     kod_kraje = nazev_en["kod_polozky"]
#     nazev_kraje = nazev_en["nazev_polozky"]
#     prumerna_hodnota =  urazy[urazy["kraj"] == kod_kraje]["hodnota"].mean()
#     urazy_prumer = urazy_prumer.append({"nazev_kraje": nazev_kraje, "hodnota": prumerna_hodnota}, ignore_index=True)

# metoda A
# adopce_vyber = adopce[
#     (adopce["nazev_en"].str.contains("blue", case=False)) & (adopce["k_prohlidce"] == 1) & (
#                 adopce["cena"] <= 2500)]
# print(adopce_vyber[["nazev_en", "k_prohlidce", "cena"]])

# metoda B
# vybrana_zvirata = pandas.DataFrame()
# for index, radek in adopce.iterrows():
#    if 'blue' in radek["nazev_en"].lower():
#       if radek["cena"] <= 2500:
#          if radek["k_prohlidce"]:
#             vybrana_zvirata = vybrana_zvirata.append(radek, ignore_index=True)
# print(vybrana_zvirata[["nazev_en", "k_prohlidce", "cena"]])


# metoda c

vybrana_zvirata = pandas.DataFrame()
for radek in adopce.itertuples():
    if 'blue' in radek.nazev_en.lower():
        if radek.cena <= 2500:
            if radek.k_prohlidce:
                vybrana_zvirata = vybrana_zvirata.append({"nazev": radek.nazev_en, "cena": radek.cena}, ignore_index=True)
print(vybrana_zvirata)