
import numpy as np
import pandas as pd
import os

os.chdir("C:/Users/HP/Downloads/")
pd.set_option('display.max_columns', None)
mydf = pd.read_csv("movies.csv",header=0)
mydf = mydf.loc[:,["name","genre","year","budget","gross","company"]]

#Print average mean of each year for drama movies
mydf["budget"]=mydf["budget"].fillna(0)
mydf["gross"]=mydf["gross"].fillna(0)
# Find the budget of Action movies in each year
#print(mydf[mydf["genre"]=="Drama"].groupby("year")["gross"].agg(np.mean))


#Print the average of each year for darama movies without aggregating rows
#mydf1 = mydf[mydf["genre"]=="Drama"]
#mydf1["avg_gross"]=mydf1.groupby("year")["gross"].transform('mean')
#print(mydf1.head(20))


#Find how many movies were released each year for every genre
#print(mydf.loc[:,["year","genre"]].value_counts().to_frame().sort_values(by="year"))

#Repeat the above without aggregating rows
#mydf["avg_movies_that_year"] = mydf.groupby(["year","genre"])["name"].transform('count')
#print(mydf.head())

#Set a multi level index and retrieve the index based filteredrecords (Below may be incomplete)
mydf = mydf.set_index(["year","genre"])
print(mydf.loc[20,:].head())



