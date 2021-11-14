import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/AirPassengers.csv")
with open("AirPassengers.csv", "wb") as f:
  f.write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/PJME_daily.csv")
with open("PJME_daily.csv", "wb") as f:
  f.write(r.content)


import pandas
import matplotlib.pyplot as plt

# df = pandas.read_csv("AirPassengers.csv")
# df = df.rename({"#Passengers": "Passengers"}, axis=1)
# df = df.set_index("Month")
# df.plot()
# #KLOUZAVÝ PRŮMĚR
# df["SMA_12"] = df["Passengers"].rolling(12).mean()
# #CENTROVANÝ KLOUZAVÝ PRŮMĚR
# df["CMA_12"] = df["Passengers"].rolling(12, center=True).mean()
# #EXPONENCIONÁLNÍ VYROVNÁNÍ
# df["EMA"] = df["Passengers"].ewm(alpha=0.1).mean()
#
# df[["SMA_12", "CMA_12","EMA", "Passengers"]].plot()
# print(df.head(n=15))
# #plt.show()
#
# #TROJITE EXPONENCIONALNÍ VYROVNÁNÍ
# from statsmodels.tsa.holtwinters import ExponentialSmoothing
# mod = ExponentialSmoothing(df["Passengers"], seasonal_periods=12, trend="add", seasonal="add", use_boxcox=True, initialization_method="estimated",)
# res = mod.fit()
# df["HM"] = res.fittedvalues
# df[["HM", "Passengers"]].plot()
# #plt.show()
#
# #PŘEDPOVED
# df_forecast = pandas.DataFrame(res.forecast(24), columns=["Prediction"])
# df_with_prediction = pandas.concat([df, df_forecast])
# df_with_prediction[["Passengers", "Prediction"]].plot()
# plt.show()
#
# #AUTOCORELACE -míru setrvačnosti časové řady, nebo přesněji lineární závislost hodnot časové řady na svých vlatních hodnotách v minulosti
# df["Passengers"].autocorr(lag=1)
#
from statsmodels.graphics.tsaplots import plot_acf
# plot_acf(df["Passengers"])
# plt.show()
#
# #AUTOREGRESIVNÍ MODELY - postavené na autokorelaci, tj. vycházejí z předpokladu, že hodnoty časové řady jsou závislé na jejích vlastních hodnotách v minulosti. používány pro stacionární časové řady, což jsou časové řady, které nemají žádný trend (nebo obecněji mají konstantní průměr).
# from statsmodels.tsa.ar_model import AutoReg
#
# model = AutoReg(df['Passengers'], lags=10, trend="t", seasonal=True, period=12)
# model_fit = model.fit()
#
# predictions = model_fit.predict(start=df.shape[0], end=df.shape[0] + 12)
# df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
# df_with_prediction = pandas.concat([df, df_forecast])
# df_with_prediction[["Passengers", "Prediction"]].plot()

#CVIČENÍ
PJME = pandas.read_csv("PJME_daily.csv")
print(PJME)
print(PJME.info())

#Vyber data za posledních 100 dní a pokus se řadu vyrovnat pomocí klouzavých průměrů. Vhodně nastav sezónnost dat. Výsledek si zobraz pomocí grafu.
PJME_100 = PJME.tail(n=100)
print(PJME_100)
PJME_100 = PJME_100.rename({"#PJME_MW": "PJME_MW"}, axis=1)
PJME_100 = PJME_100.set_index("Date")
PJME_100["SMA_7"] = PJME_100["PJME_MW"].rolling(7).mean()
#Použij exponenciální vyrovnávání k vyhlazení časové řady a výsledek si opět zobraz jako graf. Vyzkoušej několik hodnot parametru alpha.
PJME_100["EMA"] = PJME_100["PJME_MW"].ewm(alpha=0.1).mean()
#PJME_100[["SMA_7","EMA", "PJME_MW"]].plot()
#plt.show()
#Pomocí grafu si zobraz, jaká je autokorelace časové řady.
PJME_100["PJME_MW"].autocorr(lag=1)
from statsmodels.graphics.tsaplots import plot_acf
#plot_acf(PJME_100["PJME_MW"])
#plt.show()

#Agreguj data po měsících dat, aby hodnota za každý měsíc představovala průměrný odebíraný výkon za všechny dny měsíce. Opět aplikuj klouzavý průměr a výsledek si zobraz jako graf.
# PJME = PJME.reset_index()
# PJME["Month"] = pandas.to_datetime(PJME["Date"]).dt.strftime("%Y/%m")
# PJME_ag = PJME.groupby("Month")["PJME_MW"].mean()
# PJME_ag = pandas.DataFrame(PJME_ag)
# PJME_ag = PJME.groupby(["Month"])["PJME_MW"].mean()
# PJME_ag = pandas.DataFrame(PJME_ag)
# print(PJME_ag)
# PJME_ag["SMA_12"] = PJME_ag["PJME_MW"].rolling(12).mean()
# PJME_ag["CMA_12"] = PJME_ag["PJME_MW"].rolling(12, center=True).mean()
# PJME_ag[["SMA_12","CMA_12","PJME_MW"]].plot()
# plt.show()

#Na data agregovaná dle měsíce aplikuj dekompozici časové řady (aditivní model) a výsledek zobraz jako graf.
# from statsmodels.tsa.seasonal import seasonal_decompose
# decompose = seasonal_decompose(PJME_ag['PJME_MW'], model='additive', period=12)
# decompose.plot()
# plt.show()

#Vrať se k časové řadě s denními údaji. Pomocí autoregresního modelu zkus predikovat spotřebu na dva týdny dopředu.
from statsmodels.tsa.ar_model import AutoReg
model = AutoReg(PJME['PJME_MW'], lags=50, trend="t", seasonal=True, period=7)
model_fit = model.fit()
predictions = model_fit.predict(start=PJME.shape[0], end=PJME.shape[0] + 28)
df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
df_with_prediction = pandas.concat([PJME, df_forecast])
df_with_prediction[["PJME_MW", "Prediction"]].tail(200).plot()
plt.show()