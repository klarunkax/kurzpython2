import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/covid_data.csv")
open("covid_data.csv", 'wb').write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/data_with_ids.csv")
open("data_with_ids.csv", 'wb').write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/data_without_ids.csv")
open("data_without_ids.csv", 'wb').write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_actual.csv")
open("sales_actual.csv", 'wb').write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_plan.csv")
open("sales_plan.csv", 'wb').write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/user_registration.json")
open("user_registration.json", 'wb').write(r.content)

df_plan = pandas.read_csv("data/sales_plan.csv")
df_plan.head()