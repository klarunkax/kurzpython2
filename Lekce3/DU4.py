import numpy
import pandas
import psycopg2
from sqlalchemy import create_engine, inspect
import math
import matplotlib.pyplot as plt

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "klarunkax"
USERNAME = "klarunkax@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "eEXO9DiMwRYUtgl!"
engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)
#engine = create_engine("sqlite:///:memory:")

inspector = inspect(engine)
#print(inspector.get_table_names())

# dreviny = pandas.read_sql(f"dreviny",con=engine)
# print(dreviny.head())

#tabulka smrk bude obsahovat řádky, které mají v sloupci dd_txt hodnotu "Smrk, jedle, douglaska"
#VARIANTA 1
# smrk = pandas.DataFrame()
# smrk = dreviny[dreviny['dd_txt']=="Smrk, jedle, douglaska"]
#print(smrk)
#smrk.info()

#VARIANTA 2
# dreviny = pandas.read_sql("SELECT * FROM dreviny WHERE dd_txt = 'Smrk, jedle, douglaska'", con=engine)
# print(dreviny)

#tabulka nahodila_tezba bude obsahovat řádky, které mají v sloupci druhtez_txt hodnotu "Nahodilá těžba dřeva"
# nahodila_tezba = pandas.DataFrame()
# nahodila_tezba = dreviny[dreviny['druhtez_txt']=="Nahodilá těžba dřeva"]
# print(nahodila_tezba)


#vytvoř graf, který ukáže vývoj objemu těžby pro tabulku smrk. Pozor, řádky nemusí být seřazené podle roku.
# smrk.sort_values(by="rok").plot(
# x="rok", y="hodnota", title="vývoj objemu těžby"
# )
# plt.show()

#Vytvoř graf, který ukáže vývoj objemu těžby pro různé typy nahodilé těžby: Agreguj tabulku nahodila_tezba podle sloupce prictez_txt a na výsledek operace groupby zavolej metodu plot s parametrem legend=True
# nahodila_tezba.pivot_table(index="rok",columns="prictez_txt", values="hodnota",aggfunc=numpy.sum).plot(
# title="vývoj objemu těžby2", legend=True
# )
# plt.show()

# DRUHÝ UKOL CRIME
crime = pandas.read_sql(f"crime",con=engine)
# print(crime.head())

#1.Pomocí SQL dotazu si připrav tabulku o krádeži motorových vozidel (sloupec PRIMARY_DESCRIPTION by měl mít hodnotu "MOTOR VEHICLE THEFT").

crime_motor_vehicle = pandas.read_sql("SELECT * FROM crime WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT'", con=engine)
print(crime_motor_vehicle)
# crime_motor_vehicle = pandas.DataFrame()
# crime_motor_vehicle = crime[crime['PRIMARY_DESCRIPTION']=="MOTOR VEHICLE THEFT"]
#print(crime_motor_vehicle)
#
# #2.Tabulku dále pomocí pandasu vyfiltruj tak, aby obsahovala jen informace o krádeži aut (hodnota "AUTOMOBILE" ve sloupci SECONDARY_DESCRIPTION).
crime_motor_vehicle_auto = pandas.DataFrame()
crime_motor_vehicle_auto = crime_motor_vehicle[crime_motor_vehicle['SECONDARY_DESCRIPTION']=="AUTOMOBILE"]
print(crime_motor_vehicle_auto["DATE_OF_OCCURRENCE"])
#crime_motor_vehicle_auto.info()
# #3.Ve kterém měsíci dochází nejčastěji ke krádeži auta?
crime_motor_vehicle_auto["month"] = crime_motor_vehicle_auto["DATE_OF_OCCURRENCE"].dt.month
crime_motor_vehicle_auto = crime_motor_vehicle_auto.groupby(["month"]).size()
print(crime_motor_vehicle_auto)
