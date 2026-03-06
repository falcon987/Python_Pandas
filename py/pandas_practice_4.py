#Combine winter and summer olympic medals
#Then fetch the population and GDP per capita using countries file and join it with the meds data
import pandas as pd
import os

os.chdir("C:/Users/HP/Downloads/")
fileslist = ["SummerSD.csv","WinterSD.csv"]
pd.set_option('display.max_columns', None)
frameslist =[]
for i in fileslist:
    df =  pd.read_csv(i)
    frameslist.append(df)

finaldf = pd.concat(frameslist,axis="rows",keys=fileslist)
finaldf = finaldf.loc[:,["Year","Athlete","Country"]]
countries = pd.read_csv("CountriesSD.csv")

finaldf_with_population = pd.merge(finaldf,countries,left_on="Country",right_on="Code",suffixes=["_main","_ref"])

print(finaldf_with_population.head())



# How did youconnect to SQL server
import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=SERVER_NAME;"
    "Database=DB_NAME;"
    "Trusted_Connection=yes;"
)

query = "SELECT * FROM sales_data"
df = pd.read_sql(query, conn)
