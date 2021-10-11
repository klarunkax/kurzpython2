# ODSTRANENI DUPLICITY
import pandas
import requests
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/data_with_ids.csv")
# open("data_with_ids.csv", 'wb').write(r.content)
#
# data_with_ids = pandas.read_csv("data_with_ids.csv")
# print(data_with_ids.head(n=10))
# print(data_with_ids.shape)
#
# print(f"Počet řádků: {data_with_ids.shape[0]}")
# print(f"Počet unikátních řádků {data_with_ids['bank_id'].nunique()}")
#
# data_with_ids = data_with_ids.drop_duplicates(ignore_index=True)
# print(data_with_ids.head(n=10))
# print(data_with_ids.shape)


# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/covid_data.csv")
# open("covid_data.csv", 'wb').write(r.content)
# covid_data = pandas.read_csv("covid_data.csv")
# print(covid_data.head())
# print(covid_data.shape)
# covid_data = covid_data.drop_duplicates(subset=["date"], keep="last")
# print(covid_data.head())
# print(covid_data.shape)

# PRACE S DATEM A CASEM
import pandas
import matplotlib.pyplot as plt
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/invoices.csv")
# open("invoices.csv", 'wb').write(r.content)
# invoices = pandas.read_csv("invoices.csv")
# print(invoices.head())
# print(invoices.dtypes)

#prevod datumu do noveho sloupce ve formatu datetime a funkce day first
# invoices["invoice_date_converted"] = pandas.to_datetime(invoices["invoice_date"], dayfirst=True)
# print(invoices.head())
# print(invoices.dtypes)

#nebo spíš - prevod datumu takto
#invoices["invoice_date_converted"] = pandas.to_datetime(invoices["invoice_date"], format="%d. %m. %Y")

#pricitaní a porovnaní
# invoices["due_date"] = invoices["invoice_date_converted"] + pandas.Timedelta("60 days")
# print(invoices.head())

#overdue
import numpy
import datetime
# today_date = datetime.datetime(2021, 9, 1)
# invoices["status"] = numpy.where(invoices["due_date"] < today_date, "overdue", "before due date")
# print(invoices.head())
# print(invoices.groupby("status")["amount"].sum())


#  vypocty s daty
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/invoices_2.csv")
# open("invoices_2.csv", 'wb').write(r.content)
# invoices_2 = pandas.read_csv("invoices_2.csv")
# print(invoices_2.head())
# invoices_2["invoice_date"] = pandas.to_datetime(invoices_2["invoice_date"], format="%d. %m. %Y")
# print(invoices_2.head())
#
# invoices_2_paid = invoices_2.dropna().reset_index(drop=True)
# invoices_2_paid["payment_date"] = pandas.to_datetime(invoices_2_paid["payment_date"], format="%d. %m. %Y")
# invoices_2_paid["paid_in"] = invoices_2_paid["payment_date"] - invoices_2_paid["invoice_date"]
# print(invoices_2_paid.head())
#
# print(invoices_2_paid.dtypes)
#
# average_payment_data = pandas.DataFrame(invoices_2_paid.groupby(["customer"])["paid_in"].mean())
# print(average_payment_data.head())

#nesplacene faktury a prictení prumerne doby splatnosti - predikce cashflow
# invoices_2_not_paid = invoices_2[invoices_2["payment_date"].isna()]
# invoices_2_not_paid = pandas.merge(invoices_2_not_paid, average_payment_data, on=["customer"], how="outer")
# invoices_2_not_paid["expected_payment_date"] = invoices_2_not_paid["invoice_date"] + pandas.to_timedelta(invoices_2_not_paid["paid_in"], unit="D")
# invoices_2_not_paid["expected_payment_date"] = invoices_2_not_paid["expected_payment_date"].dt.date
# print(invoices_2_not_paid.head())

#použití metody shift - DOKOCIT
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/signal_monitoring.csv")
# open("signal_monitoring.csv", 'wb').write(r.content)
# signal_monitoring = pandas.read_csv("signal_monitoring.csv")
# signal_monitoring["event_date_time"] = pandas.to_datetime(signal_monitoring["event_date_time"])
# signal_monitoring.head()
# print(signal_monitoring.head())
#
#
# signal_monitoring["event_end_date_time"] = signal_monitoring["event_date_time"].shift(periods=-1)
# signal_monitoring.head()


# #metoda rank
# r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/ioef.csv")
# open("ioef.csv", 'wb').write(r.content)
# ioef = pandas.read_csv("ioef.csv")
# print(ioef.head())
#
#
# ioef["Rank"] = ioef.groupby(["Index Year"])["Overall Score"].rank(method="min", ascending=False)
# ioef_2021 = ioef[ioef["Index Year"] == 2021]
# print(ioef_2021.head())
# print(ioef_2021.sort_values(["Rank"]).head())
#
# ioef_sorted = ioef.sort_values(["Name", "Index Year"])
# ioef_sorted["Rank Previous Year"] = ioef_sorted.groupby(["Name"])["Rank"].shift()
# print(ioef_sorted.head())
# #
# #
# ioef_sorted["Rank Change"] = ioef_sorted["Rank"] - ioef_sorted["Rank Previous Year"]
# ioef_sorted_czech = ioef_sorted[ioef_sorted["Name"] == "Czech Republic"]
# print(ioef_sorted_czech.tail())

#CVIČENÍ

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/baroko_half_marathon.csv")
open("baroko_half_marathon.csv", 'wb').write(r.content)
baroko_half_marathon = pandas.read_csv("baroko_half_marathon.csv")
baroko_half_marathon = baroko_half_marathon[["Jméno závodníka", "Ročník", "Rok závodu","FINISH"]]
print(baroko_half_marathon.head())


baroko_half_marathon_sorted = baroko_half_marathon.sort_values(["Jméno závodníka", "Ročník", "Rok závodu"])
print(baroko_half_marathon_sorted)
baroko_half_marathon_sorted["FINISH"]=pandas.to_datetime(baroko_half_marathon_sorted["FINISH"])
print(baroko_half_marathon_sorted)

t()
import pandas as pd
pd.options.display.max_columns = Nonebaroko_half_marathon_sorted["FINISH2"] = baroko_half_marathon_sorted.groupby(["Jméno závodníka"])["FINISH"].shif
print(baroko_half_marathon_sorted.head())

baroko_half_marathon_2zavody = baroko_half_marathon_sorted.dropna().reset_index(drop=True)


baroko_half_marathon_2zavody["rozdíl"] = baroko_half_marathon_2zavody["FINISH2"]-baroko_half_marathon_2zavody["FINISH"]
baroko_half_marathon_2zavody["rozdíl_text"] = numpy.where(baroko_half_marathon_2zavody["rozdíl"] > pandas.Timedelta("0 days"), "zhoršení", "zlepšení")
print(baroko_half_marathon_2zavody.head())
