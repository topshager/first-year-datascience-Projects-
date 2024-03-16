import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("#CSV location file path")

df = pd.DataFrame(data)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')

# Extract year from 'Date' column
df['Year'] = df['Date'].dt.year

# Count the occurrences of each year
year_counts = df['Year'].value_counts()

# Convert Series to DataFrame
year_counts_df = year_counts.reset_index()
year_counts_df.columns = ['Year', 'Count']


# Create the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Year', y='Count', data=year_counts_df, palette='viridis')
plt.ylim(250, 255)
# Set plot title and labels
plt.title('Count of Values for Each Year')
plt.xlabel('Year')
plt.ylabel('Count')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()
