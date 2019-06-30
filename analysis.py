import pandas as pd 
import matplotlib.pyplot as plt
path = "Desktop\Sahla github\To be uploaded\python\FlagData.csv" 
df = pd.read_csv(path)
#To print the first 5 rows of the csv file
z = df.head()
print(z)

#To print the countries in Asia from the csv file
x = df[df['landmass']==5]
x = x['name']
print("The countries in Asia are:\n",x)

#To print the country with  stripes greater than 2 in their flags along with the number of stripes
y = df[df['stripes']>2]
y = y['name']
print("The country with  stripes greater than 2 in their flags are",y)
