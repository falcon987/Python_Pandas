
# Combine two dataframes that are crated on top of two different csv files

import pandas as pd
import os
os.chdir("C:/Users/HP/Downloads/")
pd.set_option('display.max_columns', None)
fileslist = ["SummerSD.csv","WinterSD.csv"]
frameslist=[]
for m in fileslist:
    df = pd.read_csv(m)
    frameslist.append(df)

finaldf = pd.concat(frameslist,axis="rows",keys=fileslist)
print(finaldf.head())