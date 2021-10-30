import requests
import pandas
import statistics
import matplotlib.pyplot as plt

#KRYPTOMĚNY
#1.Použij zavírací cenu kryptoměny (sloupec Close) a vypočti procentuální změnu jednotlivých kryptoměn. Pozor na to, ať se ti nepočítají ceny mezi jednotlivými měnami. Ošetřit to můžeš pomocí metody groupby(), jako jsme to dělali např. u metody shift().
import seaborn

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

crypto_prices = pandas.read_csv("crypto_prices.csv")
print(crypto_prices)

crypto_prices["change"] = crypto_prices.groupby(["Name"])["Close"].pct_change()
print(crypto_prices)

#2.Vytvoř korelační matici změn cen jednotlivých kryptoměn a zobraz je jako tabulku.
crypto_prices = crypto_prices.pivot(index="Date",columns="Name",values="change")
crypto_prices = pandas.DataFrame(crypto_prices)
print(crypto_prices.corr())
#
# #3.V tabulce najdi nejvyšší hodnotu korelace a korelaci nejblíže 0. Změny cen pro dvojice měn, které jsou nejvíce a nejméně korelované, si zobraz jako bodový graf
# #sort.values()
# seaborn.heatmap(crypto_prices.corr(), annot=True, fmt=".1f")
# plt.show()
#
# seaborn.jointplot("Wrapped Bitcoin", "Litecoin", crypto_prices, kind='scatter', color='seagreen')
# plt.show()

##POKRAČOVÁNÍ
##1. Z datového souboru si vyber jednu kryptoměnu a urči průměrné denní tempo růstu měny za sledované období. Můžeš využít funkci geometric_mean z modulu statistics. Vyber si sloupec se změnou ceny, kterou máš vypočítanou z předchozího cvičení (případně si jej dopočti), přičti k němu 1 (nemusíš dělit stem jako v lekci, hodnoty jsou jako desetinná čísla, nikoli jako procenta) a převeď jej na seznam pomocí metody .tolist().

crypto_prices["Aave"] = crypto_prices["Aave"]+1
#crypto_aave = crypto_aave.iloc[1:]
print(crypto_prices)
crypto_aave_list = crypto_prices["Aave"].dropna().to_list()
print(crypto_aave_list)

#2. Následně vypočti geometrický průměr z těchto hodnot.
print(statistics.geometric_mean(crypto_aave_list))