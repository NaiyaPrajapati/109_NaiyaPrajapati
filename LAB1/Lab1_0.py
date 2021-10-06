import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

data=pd.read_csv('/content/drive/My Drive/ML/Lab1/mtcars.csv')
d=pd.crosstab(index=data['cyl'],columns="count",dropna=True)
print(d)

print(data.info())

#Count Total Null values in each column
print("Total Null Data:",data.isnull().sum())

# Finding the Histogram
# From the given dataset ‘mtcars.csv’, plot a histogram to check the frequency distributi
on of the variable ‘mpg’ (Miles per gallon).
plt.hist(data['mpg'],bins=5)
plt.show()

#scatter plot of ‘mpg’ (Miles per gallon) vs ‘wt’ (Weight of car)
plt.scatter(data['mpg'],data['wt'])
plt.show()

#In the dataframe, under the variable gear count total records in each value
df=pd.DataFrame(data,columns=['gear'])
print("Count How many values:\n",df['gear'].value_counts())

"""Exercise:"""

import matplotlib.pyplot as plt
# Declare a figure with a custom size
fig = plt.figure(figsize=(5, 5))
# labels for the classes
labels = 'ML-BSB-Lec', 'ML-HAP-Lec', 'ML-HAP-Lab'
# Sizes for each slide
sizes = [40, 35, 25]
# Declare pie chart, where the slices will be ordered and plotted counter-clockwise:
plt.pie(sizes, labels=labels, autopct='%.2f%%',
        shadow=True, startangle=90)
# autopct enables you to display the percent value using Python string formatting.
# For example, if autopct='%.2f', then for each pie wedge, the format string is '%.2f' and

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
# Display the chart
plt.show()