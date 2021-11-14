import yfinance as yf
import pandas
import matplotlib.pyplot as plt
# CSCO = yf.Ticker("CSCO")
# CSCO_5 = CSCO.history(period="5y")
# print(CSCO_5.describe())
# print(CSCO_5)
#
# #Zobraz si graf autokorelace a podívej se, jak je hodnota ceny závislná na svých vlastních hodnotách v minulosti.
# CSCO_5["Close"].autocorr(lag=1)
# from statsmodels.graphics.tsaplots import plot_acf
# plot_acf(CSCO_5["Close"])
# plt.show()
# #Zkus použít AR model k predikci cen akcie na příštích 5 dní.
# from statsmodels.tsa.ar_model import AutoReg
# model = AutoReg(CSCO_5["Close"], lags=50, trend="t", seasonal=False)
# model_fit = model.fit()
#
# #Zobraz v grafu historické hodnoty (nikoli celou řadu, ale pro přehlednost např. hodnoty za posledních 50 dní) a tebou vypočítanou predikci.
# predictions = model_fit.predict(start=CSCO_5.shape[0], end=CSCO_5.shape[0] + 5)
# df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
# df_with_prediction = pandas.concat([CSCO_5, df_forecast])
# df_with_prediction[["Close", "Prediction"]].tail(50).plot()
# plt.show()

import requests
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
with open("MLTollsStackOverflow.csv", "wb") as f:
  f.write(r.content)

MLTOLLS = pandas.read_csv("MLTollsStackOverflow.csv")
print(MLTOLLS)
print(MLTOLLS.info())

#Vyber sloupec python.

#Proveď dekompozici této časové řady pomocí multiplikativního modelu. Dekompozici zobraz jako graf.
from statsmodels.tsa.seasonal import seasonal_decompose

decompose = seasonal_decompose(MLTOLLS['python'], model='multiplicative', period=12)
decompose.plot()
plt.show()
#Vytvoř predikci hodnot časové řady pomocí Holt-Wintersovy metody na 12 měsíců. Sezónnost nastav jako 12 a uvažuj multiplikativní model pro trend i sezónnost. Výsledek zobraz jako graf.
from statsmodels.tsa.holtwinters import ExponentialSmoothing
mod = ExponentialSmoothing(MLTOLLS["python"], seasonal_periods=12, trend="add", seasonal="add", use_boxcox=True, initialization_method="estimated",)
res = mod.fit()
MLTOLLS["HM"] = res.fittedvalues
MLTOLLS[["HM", "python"]].plot()
plt.show()