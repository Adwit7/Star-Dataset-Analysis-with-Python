#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv ('/kaggle/input/star-dataset/6 class csv.csv')

print (df.isnull().sum())
df = df.rename(columns={'Absolute magnitude(Mv)': 'Absolute_Magnitude'})
df['Star type'] = df['Star type'].astype('category')
print ( df.head())

print(df['Star type'].dtype) 
###################################################
star_color_red =  df[df['Star color'] == 'Red']
print (star_color_red )

red_count = len(df[df['Star color'] == 'Red'])
print(f"Number of red stars: {red_count}")

avg_temperature = star_color_red ['Temperature (K)'].mean() 
print ( avg_temperature )

###################################################

x = df['Temperature (K)']
y = df['Luminosity(L/Lo)']
# Create scatter plot
plt.figure(figsize=(3, 2))
plt.scatter( x , y )

# Add labels and title
plt.xlabel('Temperature (K)')
plt.ylabel('Luminosity(L/Lo)')
plt.title('Temperature vs Luminosity of Stars')
# Show the plot
plt.show()


star_color_counts = df['Star color'].value_counts()
print (star_color_counts)
print ( sns.barplot (x = star_color_counts.index,y = star_color_counts.values))
plt.xlabel('Star Color')
plt.ylabel('Count')
plt.title('Count of Stars by Color')
##########################################################

# Average
print(df['Radius(R/Ro)'].mean())

# Median
print(df['Radius(R/Ro)'].median())

print (df ['Temperature (K)'].min())  
print (df ['Absolute_Magnitude'].max()) 

###################################################

# Create Temperature_Category column
df['Temperature_Category'] = np.where(df['Temperature (K)'] > 10000, 'Hot', 'Cool')

# Verify the new column
print(df['Temperature_Category'])
print (df)

# Group by Temperature_Category and calculate mean
avg_magnitude = df.groupby('Temperature_Category')['Absolute_Magnitude'].mean()
print(avg_magnitude)
