import pandas as pd 
import matplotlib.pyplot as plt
path = "FlagData.csv" 
df = pd.read_csv(path)

#To print the first 5 rows of the flag dataset
z = df.head()
print(z)

#To print the countries in Asia from the flag dataset
x = df[df['landmass']==5]
x = x['name']
print("The countries in Asia are:\n",x)

#To print the country with  stripes greater than 2 in their flags along with the number of stripes
y = df[df['stripes']>2]
y = y['name']
print("The country with  stripes greater than 2 in their flags are",y)

#To print the country name with no red color in the flag and creating a new csv file with that list
w = df[df['red']==0]
q = w['name']
print("The country with no red color in the flag",q)
w.to_csv("flagnew.csv")

#To print the first 5 rows of the newly created file
df1 = pd.read_csv("flagnew.csv")
e = df1.head()
print (e)
