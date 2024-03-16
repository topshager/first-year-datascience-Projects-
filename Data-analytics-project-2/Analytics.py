#Question 1.1

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime

# Read the CSV file into a DataFrame
df = pd.read_csv("#CSV location file path")
# Replace blank spaces with NaN (missing values)
df.replace(' ', np.nan, inplace=True)

# Display the first few rows of the DataFrame
print(df.head())

# Display the last few rows of the DataFrame
print(df.tail())

# Compute median for the specified columns
median_values = df[['Rtn..1.Day','Rtn..1.Day.1', 'Rtn..2.Day']].median()

print(median_values)
# Replace missing values with median
df[['Rtn..1.Day','Rtn..1.Day.1', 'Rtn..2.Day']] = df[['Rtn..1.Day','Rtn..1.Day.1', 'Rtn..2.Day']].fillna(median_values)


# Display the new summary of the dataset
print("\nNew summary of the dataset:")
print(df.info())

#Question 1.4

summary = df[['Date','Rtn..1.Day','Rtn..1.Day.1', 'Rtn..2.Day']]
columnCount = summary.count()
print(summary,columnCount )
print("\nNew summary of the dataset:")
print(summary.info())

#Question 1.5
df.reset_index(drop=True ,inplace=True)

print("DataFrame after resetting index:")
print(df)

# Display a summary of the new table
print("\nSummary of the new table:")
print(df.info())

#Question 1.6
df['Date'] = pd.to_datetime(df['Date'],format ='%Y-%m-%d')

df['year'] = df['Date'].dt.year

df['Month'] = df['Month'].dt.month

df['Day'] = df['Day'].dt.day

print("Updated dataset:")
print(df)

#Question 1.7
