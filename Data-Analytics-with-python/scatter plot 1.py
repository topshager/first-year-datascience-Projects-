import pandas as pd
import matplotlib.pyplot as plt

# Load both datasets
data1 = pd.read_csv('#CSV location file path dataset 1')
data2 = pd.read_csv('#CSV location file path dataset 2')

# Rename columns if necessary to ensure consistency
# For example, if 'Student mark achieved' in dataset 1 is called 'Marks' in dataset 2, you should rename it

# Merge both datasets
merged_data = pd.concat([data1, data2])

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(data1['Time taken on examination (minutes)'], data1['Student mark achieved'], label='Dataset 1')
plt.scatter(data2['Time taken on examination (minutes)'], data2['Student mark achieved'], label='Dataset 2')
plt.title('Marks vs Time Taken on Examination')
plt.xlabel('Time taken on examination (minutes)')
plt.ylabel('Student mark achieved')
plt.legend()
plt.grid(True)
plt.show()
