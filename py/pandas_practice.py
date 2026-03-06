

import pandas as pd
import os

os.chdir("C:/Users/HP/Downloads/")

mydf = pd.read_csv("WinterSD.csv",header=0,index_col=0)
mydf.columns = ['Year', 'City', 'Game', 'Discipline', 'Athlete', 'Country', 'Gender',
       'Event', 'Medal']

#print(mydf[:2])
# Get first 3 bronze medalists
#print(mydf.loc[mydf["Medal"]=="Bronze",:].head(3))


# Latest 10 gold medalists
#print(mydf.loc[mydf["Medal"]=="Gold",:].sort_values("Year",ascending = False)[:10])

# Report women % against the all participants for the year 2000-2014
#finaldf = mydf.loc[mydf["Year"]>=2000,["Year","Gender"]].groupby("Year").value_counts(normalize=True)*100
#print(finaldf)

#Create a dummy amount. Report sum,min,max of this amount against the combination of Year,Medal and Gender
#mydf["dummy_amount"] = mydf["Year"] -45
#mydfnew = pd.DataFrame(mydf.groupby(["Year","Medal","Gender"])["dummy_amount"].agg([min,max,sum]))

#Print it in reverse order of year,medal and Gender
#print(mydfnew.sort_values(["Year","Medal","Gender"],ascending=False))

#Get first medal from each year
mydfnew = mydf.drop_duplicates(subset=["Year"],keep = "first")
#print(mydfnew)

#Get the rows that re having only one event in a year
print(mydfnew.drop_duplicates(subset=["Year","Event"],keep = False))





