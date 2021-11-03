import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/ceny_domu.csv")
with open("ceny_domu.csv", "wb") as f:
  f.write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/insurance.csv")
with open("insurance.csv", "wb") as f:
  f.write(r.content)

#REGRESE
import pandas
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import seaborn

# ceny_domu = pandas.read_csv("ceny_domu.csv")
# print(ceny_domu.head())
#
# #lineárni regrese - OLS - metoda nejmenších čtverců

#
# mod = smf.ols(formula="prodejni_cena_mil ~ obytna_plocha_m2", data=ceny_domu)
# res = mod.fit()
# res.summary()
#
# pred_ols = res.get_prediction()
#
# fig, ax = plt.subplots(figsize=(8, 6))
#
# import matplotlib.pyplot as plt
# plt.plot(ceny_domu["obytna_plocha_m2"], ceny_domu["prodejni_cena_mil"], "b.")
# plt.plot(ceny_domu["obytna_plocha_m2"], res.fittedvalues, "r")
# #plt.show()
#
# ceny_domu.isna().sum()
# ceny_domu["plocha_pozemku_pred_domem_m2"] = ceny_domu["plocha_pozemku_pred_domem_m2"].fillna(0)
#
# #korelační matice - korelace mezi proměnnými
# # import seaborn
# # seaborn.heatmap(ceny_domu.corr(), annot=True, cmap="Blues")
# # plt.show()
#
# # drop nepotřebné sloupce
# ceny_domu = ceny_domu.drop("pocet_aut_v_garazi", axis=1)
# ceny_domu = ceny_domu.drop("plocha_pozemku_pred_domem_m2", axis=1)
# ceny_domu = ceny_domu.drop("plocha_pozemku_m2", axis=1)
# ceny_domu = ceny_domu.drop("pocet_koupelen", axis=1)
#
# #model s více proměnnými
# mod = smf.ols(formula="prodejni_cena_mil ~ obytna_plocha_m2 + celkova_kvalita + rok_vystavby + rok_rekonstrukce "
#                       " + plocha_garaze_m2", data=ceny_domu)
# res = mod.fit()
# res.summary()
#
# #predikce ceny
#
# data = pandas.DataFrame({"obytna_plocha_m2": [200],
#                          "celkova_kvalita": [8],
#                          "rok_vystavby": [1980],
#                          "rok_rekonstrukce": [2010],
#                          "plocha_garaze_m2": [60]})
# res.predict(data)
#
# #neciselne_hodnoty
# ceny_domu["sousedstvi"].unique()
# #pocet sousedství
# ceny_domu["sousedstvi"].unique().shape
# #průměrná cena za sousedství
#
# #zařazení ceny sousedství jako proměnou
# prumery = ceny_domu.groupby('sousedstvi')['prodejni_cena_mil'].mean().sort_values()
# ceny_domu['sousedstvi_prum_cena'] = ceny_domu['sousedstvi'].map(prumery)
# print(ceny_domu["sousedstvi_prum_cena"])
# predictors = ['plocha_pozemku_pred_domem_m2','plocha_pozemku_m2', 'obytna_plocha_m2', 'celkova_kvalita','rok_vystavby', 'rok_rekonstrukce','plocha_garaze_m2','sousedstvi_prum_cena']
#
# mod = smf.ols(formula="prodejni_cena_mil ~ obytna_plocha_m2 + celkova_kvalita + rok_vystavby + rok_rekonstrukce "
#                       " + plocha_garaze_m2 + sousedstvi_prum_cena", data=ceny_domu)
# res = mod.fit()
# res.summary()
#
# data = pandas.DataFrame({"obytna_plocha_m2": [200],
#                          "celkova_kvalita": [8],
#                          "rok_vystavby": [1980],
#                          "rok_rekonstrukce": [2010],
#                          "sousedstvi_prum_cena": prumery["Mitchel"],
#                          "plocha_garaze_m2": [60]})
# print(res.predict(data))

#CIČENÍ
insurance = pandas.read_csv("insurance.csv")
print(insurance.head())


#Sestav regresní model, který bude na základě věku a pohlaví počítat výši pojistného. Rozhodni o kvalitě takto sestaveného modelu.
insurance["sex"] = insurance["sex"] == "male"
print(insurance["sex"])
mod = smf.ols(formula="charges ~ age + sex", data=insurance)
res = mod.fit()
print(res.summary())

#Přidej do modelu informace o tom, zda je pojištěnec kuřák. Zhodnoť, nakolik se tím zvýšila kvalita modelu.
mod = smf.ols(formula="charges ~ age + sex + smoker", data=insurance)
res = mod.fit()
print(res.summary())

#Nakonec přidej do modelu informaci o regionu. Použij metodu target encoding, kterou jsme si ukazovali během lekce.
insurance["region"].unique()
print(insurance["region"].unique().shape)

prumery_region = insurance.groupby('region')['charges'].mean().sort_values()
insurance['prum_charges_region'] = insurance['region'].map(prumery_region)
print(insurance["prum_charges_region"])

mod = smf.ols(formula="charges ~ age + sex + smoker + prum_charges_region", data=insurance)
res = mod.fit()
print(res.summary())