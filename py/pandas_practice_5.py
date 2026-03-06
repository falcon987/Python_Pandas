import pandas as pd
import os
os.chdir("C:/Users/HP/Downloads/")
pd.set_option('display.max_columns', None)
def raiseit(m:tuple) -> tuple:
    a,b = m
    return (a**b,b**a)

#print(raiseit((2,6)))

# Create a function to count word occurences in multiple columns of a dataframe
def count_tweets(mydf):
    mydic={}
    for col in mydf.columns:
        for word in mydf[col]:
            if word in mydic.keys():
                mydic[word]+=1
            else:
                mydic[word]=1
    return mydic

#mydf = pd.read_csv("movies.csv",header=0)[["year","genre"]]
#print(count_tweets(mydf))



#Create a function to accept an indefinite length of numbers as input and return their sum

def summer(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
#print(summer([89,90]))

#Create a function to get sum of all the lists passed
#output is list1:567,list2:666  etc

def listsummer(*lis):
    i=0
    mydic ={}
    for l in lis:
        sum=0
        for num in l:
            sum+=num
        i+=1
        mydic[i]=sum
    return mydic
#print(listsummer([1,1],[90,89],[2,2,2]))


# Create a function that accepts key value parameters such as list1=[343,44]
#and generates the corressponding sums
def listsummerkv(**listos):
    i=0

    mydic={}
    for k,v in listos.items():
        sum=0
        for m in v:
            sum+=m
        i+=1
        mydic[k]=sum
    return mydic
#print(listsummerkv(m=[12,34],darasingh=[34,55,66],khali=[99,99,99,99]))

#Create a function thtat allows us to generate a function to raise to a pre-set exponent.

def outerfun(y):
    def innerfun(x):
        return x**y
    return innerfun
m = outerfun(2)
#print(m(9))

#Same stuff using lambda

def outerfunlamb(y):
    return lambda x:x**y

op = outerfunlamb(2)
print(op(9))





