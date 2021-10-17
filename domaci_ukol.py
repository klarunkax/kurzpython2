import requests
import pandas
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/user_registration.json")
open("user_registration.json", 'wb').write(r.content)
df_registration = pandas.read_json("user_registration.json")
pandas.set_option('display.max_columns', None)
print(df_registration.head())


