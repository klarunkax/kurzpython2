import requests
import pandas
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
  f.write(r.content)

#KVALITA CEMENTU
Concrete_Data_Yeh = pandas.read_csv("Concrete_Data_Yeh.csv")
print(Concrete_Data_Yeh.head())
Concrete_Data_Yeh.info()

#1.Vytvoř regresní model, který bude predikovat kompresní sílu betonu na základě všech množství jednotlivých složek a jeho stáří.
mod = smf.ols(formula="csMPa ~ cement + slag + flyash + water + superplasticizer + fineaggregate + age", data=Concrete_Data_Yeh)
res = mod.fit()
print(res.summary())
#2.Zhodnoť kvalitu modelu.
# R-squared:0,614 = kvalita modelu je 61,4%

#3.Tipni si, která ze složek betonu ovlivňuje sílu betonu negativní (tj. má záporný regresní koeficient). Napiš, o kterou složku jde, do komentáře svého programu.
# water

#RYBY
Fish = pandas.read_csv("Fish.csv")
print(Fish.head())
Fish.info()

#Vytvoř regresní model, který bude predikovat hmnotnost ryby na základě její diagonální délky (sloupec Length2).
mod = smf.ols(formula="Weight ~ Length2", data=Fish)
res = mod.fit()
print(res.summary())

#Zkus přidat do modelu výšku ryby (sloupec Height) a porovnej, jak se zvýšila kvalita modelu.
mod = smf.ols(formula="Weight ~ Length2 + Height", data=Fish)
res = mod.fit()
print(res.summary())
# kvalita modelu se o malinko zlepsila z 84,4% na 87,5%

# Nakonec pomocí metody target encoding zapracuj do modelu živočišný druh ryby.
Fish["Species"].unique()
print(Fish["Species"].unique().shape)

prumery_druh = Fish.groupby('Species')['Weight'].mean().sort_values()
Fish['prumerna_vaha_druh'] = Fish['Species'].map(prumery_druh)
print(Fish["prumerna_vaha_druh"])

mod = smf.ols(formula="Weight ~ Length2 + Height + prumerna_vaha_druh", data=Fish)
res = mod.fit()
print(res.summary())

# kvalita modelu se o malinko zlepsila na 90%
