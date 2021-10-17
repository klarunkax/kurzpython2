import requests
import pandas
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_plan.csv")
open("sales_plan.csv", 'wb').write(r.content)
df_plan = pandas.read_csv("sales_plan.csv")
df_plan.head()

df_plan["sales_plan_cumsum"] = df_plan.groupby("year")["sales"].cumsum()

#
#
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_actual.csv")
open("sales_actual.csv", 'wb').write(r.content)
df_actual = pandas.read_csv("sales_actual.csv")


df_actual["date"] = pandas.to_datetime(df_actual["date"])
df_actual["month"] = df_actual["date"].dt.month
df_actual["year"] = df_actual["date"].dt.year


df_actual_grouped = df_actual.groupby(["month", "year"]).sum()
df_actual_grouped["sales_actual_cumsum"] = df_actual_grouped["contract_value"].cumsum()

#
df_actual_grouped = df_actual_grouped.reset_index()
#
df_plan = df_plan[["month", "year", "sales_plan_cumsum"]]
df_actual_grouped = df_actual_grouped[["month", "year", "sales_actual_cumsum"]]
df_joined = df_plan.merge(df_actual_grouped, on=["month", "year"])


df_joined["period"] = df_joined["month"].astype(str) + "/" + df_joined["year"].astype(str)
df_joined = df_joined.set_index("period")

#
#
import matplotlib.pyplot as plt
ax = df_joined.plot(color="red", y="sales_plan_cumsum", title="Skutečné vs plánované tržby")
df_joined.plot(kind="bar", y="sales_actual_cumsum", ax=ax)
plt.legend(['Plán tržeb', "Skutečné tržby"])
plt.show()
#
#
# df_joined.plot(kind="bar", y=["sales_plan_cumsum", "sales_actual_cumsum"],
#                      color=["grey", "orange"], title="Skutečné vs plánované tržby")
# plt.legend(['Plán tržeb', "Skutečné tržby"])
# plt.show()
#
#
#
#
#
#
#
df_actual["contract_value"] = df_actual["contract_value"] / 1_000_000
df_actual_aggregated = df_actual.groupby(["sales_manager", "country"])["contract_value"].sum()
df_actual_aggregated = pandas.DataFrame(df_actual_aggregated)
#
import numpy
df_actual_pivot = pandas.pivot_table(df_actual, values="contract_value", index="country", columns="sales_manager", aggfunc=numpy.sum, margins=True)
print(df_actual_pivot)