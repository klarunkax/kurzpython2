import requests
import pandas

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon = pandas.read_csv("lexikon-zvirat.csv", sep=";")
lexikon = lexikon.dropna(how='all', axis='columns')
lexikon = lexikon.dropna(how='all', axis='rows')
#print(lexikon.head())
lexikon = lexikon.set_index("id")
lexikon.info()

def check_url(radek):
    if isinstance(radek.image_src, str):
        if radek.image_src.startswith("https://zoopraha.cz/images/"):
            if radek.image_src.endswith(("JPG","jpg")):
                return True
neplatny_url = pandas.DataFrame()
for radek in lexikon.itertuples():
    if check_url(radek):
        False
        neplatny_url = neplatny_url.append({"nazev": radek.title}, ignore_index=True)
print(neplatny_url)

def popisek(radek):
    popis_zvirete =  f"{radek[0]}  preferuje následující typ stravy  {radek[11]}"
    return popis_zvirete

lexikon["popisek"] = lexikon.apply(popisek,axis=1)
print(lexikon.head())
