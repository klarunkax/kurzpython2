import pandas
import psycopg2
from sqlalchemy import create_engine, inspect

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "klarunkax"
USERNAME = "klarunkax@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "eEXO9DiMwRYUtgl!"
engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)
#engine = create_engine("sqlite:///:memory:")

inspector = inspect(engine)
print(inspector.get_table_names())
#
#
# df = pandas.read_sql(f'uzivatele-{USER}', con=engine)
# print(df)

# Vyfiltrování dat pomocí SQL
# df = pandas.read_sql("SELECT age from \"uzivatele-klarunkax\" WHERE produkt = 'kávovar'", con=engine)
# print(df)

# Vyfiltrování dat pomocí klasického dotazu pandas
# df = pandas.read_sql('uzivatele-klarunkax', con=engine)
# df[df['produkt'] == 'kávovar']['age']
# print(df)

# def cena_produktu(radka):
#     ceny = {"šicí stroj": 5000, "sušička ovoce": 3000, "gril": 7000}
#     produkt = radka["produkt"]
#     return ceny.get(produkt, 2000)
#
# df["cena"] = df.apply(cena_produktu, axis=1)
#
# nova_data = pandas.DataFrame({"name":["Hana"], "country":["Czech Republic"], "adress_street":["Korunní"]})
# nova_data.to_sql(f"uzivatele-{USER}", con=engine, index=False, if_exists="append")
#
pocet_obyvatel = pandas.read_sql(f"pocet_obyvatel",con=engine)
print(pocet_obyvatel.head())

pocet_bytu = pandas.read_sql(f"pocet_bytu",con=engine)
print(pocet_bytu.head())

pocet_obyvatel_bytu = pocet_obyvatel.merge(pocet_bytu, on="obec")
print(pocet_obyvatel_bytu.head())

pocet_obyvatel_bytu = pocet_obyvatel_bytu[pocet_obyvatel_bytu["pocet_obyvatel"]>1000]
pocet_obyvatel_bytu["pomer"] = pocet_obyvatel_bytu["pocet_bytu"]/(pocet_obyvatel_bytu["pocet_obyvatel"]/100_000)
pocet_obyvatel_bytu = pocet_obyvatel_bytu.sort_values(["pomer"], ascending=False)
print(pocet_obyvatel_bytu.head())
