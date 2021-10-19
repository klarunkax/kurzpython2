import statistics
import matplotlib.pyplot as plt
#
# first_seven_days = [
#   5.1,
#   5,
#   4.8,
#   4.7,
#   63.7,
#   4.3,
#   7.1,
#   0.8,
# ]
#
# x = range(1, len(first_seven_days) + 1)
# #plt.bar(x, first_seven_days)
# #plt.show()
#
# #PRŮMĚR A MEDIÁN
# print(statistics.mean(first_seven_days))
# print(statistics.median(first_seven_days))
#
# second_seven_days = [
#   8.3,
#   16.5,
#   10.8,
#   7.5,
#   6.2,
#   6.4,
#   1.6,
#   1.7,
#   1.9,
#   1.9,
#   4,
#   1.8,
#   2.4,
#   2,
#   15.1,
#   11.2,
#   11.8,
#   21.9,
#   3.9
# ]
# #UKAZATELE VARIABILITY
# #rozptyl
# print(statistics.pvariance(first_seven_days))
# print(statistics.pvariance(second_seven_days))
# #smerodatna odchylka - odmocnina rozptylu (standard deviation)
# print(statistics.pstdev(first_seven_days))
# print(statistics.pstdev(second_seven_days))
# #rozdíl nejvyšší a nejnižší hodnoty (varianční rozpětí)
# print(max(first_seven_days) - min(first_seven_days))
# print(max(second_seven_days) - min(second_seven_days))
#
# #MODUS - nejčasteji se vyskytující hodnota (i pro použití pro řetězce a dokonce třeba pro dvojice)
# student_research_age = [
#   18,
#   17,
#   15,
#   15,
#   16,
#   16,
#   16,
#   17,
#   15,
#   15,
#   15,
#   15,
#   15,
#   15,
#   15,
#   16,
#   16,
#   16,
#   17,
#   16
# ]
#
# print(statistics.mode(student_research_age))
#
# student_research_age_gender = [
#   ("F", 18),
#   ("F", 17),
#   ("F", 15),
#   ("F", 15),
#   ("F", 16),
#   ("M", 16),
#   ("M", 16),
#   ("F", 17),
#   ("M", 15),
#   ("M", 15),
#   ("F", 15),
#   ("F", 15),
#   ("M", 15),
#   ("M", 15),
#   ("M", 15),
#   ("F", 16),
#   ("F", 16),
#   ("F", 16),
#   ("M", 17),
#   ("M", 16),
#   ("M", 15),
# ]
#
# print(statistics.mode(student_research_age_gender))
#
# #hash
# print(student_research_age_gender[0].__hash__())
# print(student_research_age_gender[2].__hash__())
# print(student_research_age_gender[3].__hash__())
#
# #prevedeni tuple na seznam
# #ntice = (10, 15, 20, 30)
# #seznam = list(ntice)
#
# #GEOMETRICKÝ PRŮMĚR
# gdp_growth_rate = [
#   2.435,
#   1.76,
#   -0.785,
#   -0.046,
#   2.262,
#   5.388,
#   2.537,
#   5.169,
#   3.199,
#   2.314
# ]
#
# gdp_growth = []
# for value in gdp_growth_rate:
#   gdp_growth.append(1 + value/100)
#
# print((statistics.geometric_mean(gdp_growth) - 1) * 100)

# import yfinance as yf
import pandas
#
#
# msft = yf.Ticker("MSFT")
# msft_df = msft.history(period="1y")
# print(msft_df.describe())
# print(msft_df)
#
# #KORELACE
# aapl = yf.Ticker("AAPL")
# aapl_df = aapl.history(period="1y")
#
# msft_close = msft_df["Close"]
# aapl_close = aapl_df["Close"]
#
# stock_data_df = pandas.merge(msft_close, aapl_close, on=["Date"], suffixes=["MSFT", "AAPL"])
# stock_data_df = stock_data_df.rename(columns={"CloseMSFT": "MSFT", "CloseAAPL": "AAPL"})
# stock_data_change_df = stock_data_df.pct_change()
#print(stock_data_change_df)

import seaborn
# seaborn.jointplot("MSFT", "AAPL", stock_data_change_df, kind='scatter', color='seagreen')
# #plt.show()


# tsn = yf.Ticker("TSN")
# tsn_df = tsn.history(period="1y")
# tsn_df = tsn_df.rename(columns={"Close": "TSN"})
# tsn_close = tsn_df["TSN"]
# stock_data_three_df = pandas.merge(stock_data_df, tsn_close, on=["Date"])
# stock_data_three_df.head()
# seaborn.jointplot("AAPL", "TSN", stock_data_three_df.pct_change(), kind='scatter', color='seagreen')
#plt.show()
#
# print(stock_data_three_df.corr())

#ITERTOOLS A KARTOUZSKY SOUČIN
import itertools

#suits = ("Club", "Diamond", "Heart", "Spade")
# suits = ("♣", "♦", "♥", "♠")
# ranks = (1, 2, 3, 4, 5, 7, 8, 9, "J", "Q", "K", "A")
#
# list_of_cards = list(itertools.product(suits, ranks))
#
# for item in list_of_cards:
#   print(f"{item[0]} {item[1]}")

#CVIČENÍ
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/UberDrives.csv")
open("UberDrives.csv", "wb").write(r.content)
uber_drives = pandas.read_csv("UberDrives.csv")
uber_drives = uber_drives.iloc[:-1]
print(uber_drives)
uber_drives.info()

#Pro ujetou vzdálenost (sloupec MILES) urči průměr, medián, rozptyl a varianční rozpětí podle typu jízdy (sloupec CATEGORY).
ber_drives_grouped = urban_drives.groupby(["CATEGORY"]).agg({"MILES":["mean","median","var","std","count","min","max"]})
print(statistics.mean(uber_drives.groupby(["MILES"]))
print(statistics.median(uber_drives["MILES"]))
print(statistics.pvariance(uber_drives["MILES"]))
print(max(uber_drives["MILES"]) - min(uber_drives["MILES"]))

#Vypočti délku jízdy (rozdíl časových údajů ve sloupcích END_DATE a START_DATE) v minutách nebo hodinách.
uber_drives["START_DATE"] = pandas.to_datetime(uber_drives["START_DATE"])
uber_drives["END_DATE"] = pandas.to_datetime(uber_drives["END_DATE"])
uber_drives["DELKA_JIZDY"] = uber_drives["END_DATE"] - uber_drives["START_DATE"]
#???uber_drives["DELKA_JIZDY"] = uber_drives["DELKA_JIZDY"].dt.minute
print(uber_drives["DELKA_JIZDY"])

#Zjisti, jaká je korelace mezi délkou jízdy a vzdáleností.
seaborn.jointplot("DELKA_JIZDY", "MILES", stock_data_three_df.pct_change(), kind='scatter', color='seagreen')
#plt.show()